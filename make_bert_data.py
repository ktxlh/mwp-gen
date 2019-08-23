"""
Finetuned BERT for our task directly

Targeted data format:
[CLS] this [MASK] [MASK] sample sent . [SEP] what do you think ? [SEP]$$$is a

Procedure:
1. Generate the above data. One MWP per line. Split. [modify write_bert_in]
    1. Tokenize w/ BERT
    2. Mask w/ LCS & Hierarchical clustering
2. Generate json ds from #1 for finetuning BERT [Don’t add mask here? Or finetuned on both in order?]
3. Read the data directly for new MWP generation

TODO Modify the read-in part of blank_filling
"""
import argparse
import collections
import json
import os
import shelve
from argparse import ArgumentParser
from multiprocessing import Pool
from pathlib import Path
from random import choice, randint, random, randrange, sample, shuffle
from tempfile import TemporaryDirectory

import numpy as np
from nltk.tokenize import sent_tokenize
from tqdm import tqdm, trange

from blank_filling import (cluster, fi_tag_filling, get_lcs_sim_mat,
                           get_mwp_seqs, get_template_seqs, mwp2masked,
                           temp2masked)
from lm_finetuning.pregenerate_training_data import DocumentDatabase
from pytorch_transformers.tokenization_bert import BertTokenizer

n_preds = 1
n_items = 20 # How many <PER_i>, <num>, ...?
n_sequences = int(1e7) # 100K = 1e5 samples in the current largest dataset => 1e7 means infinity
CLS = '[CLS]'
SEP = '[SEP]'
EOS = '<eos>'

def is_bad(sent):
    """
    Definition of "bad MWPs" skipped for all experiments (including valid/test!)
    (HACK a copy in Datasets/make_data.py)
    """
    return True if sum([1 for s in sent if s.isalpha()]) < len(sent)/2 else False

def write_general_in_rand_mask(data_path, rand_mask):
    print(f"\nwrite_general_in_rand_mask({data_path}, {rand_mask})\n")
    train_lines = [line.strip().split('|||')[0] \
        for line in (open(os.path.join(data_path,'train.txt'),'r',encoding='utf-8')).readlines()]
    new_mwps, ans = [], []
    unmaskables = {CLS, SEP}
    min_nb_tok_kept = 3 # Keep at least 3 tokens unmasked in each MWP
    
    for line in train_lines:
        line = f'{CLS} '+f' {SEP} '.join(sent_tokenize(line.replace(' '+EOS,'')))+f' {SEP}'
        tokens = line.split()

        mwp_ans = []
        maskable_idx = sorted([i for i in range(len(tokens)) if tokens[i] not in unmaskables])
        for idx in sample(maskable_idx, min(rand_mask,max(len(maskable_idx)-min_nb_tok_kept,1))):
            mwp_ans.append(tokens[idx])
            tokens[idx] = '[MASK]'  
        new_mwps.append(' '.join(tokens))
        ans.append(' '.join(mwp_ans))

    lines = [f"{m}$$${a}\n" for m,a in zip(new_mwps, ans)]
    with open(os.path.join(data_path,'general_in_rand_mask.txt'), 'w', encoding='utf-8') as fout:
        fout.writelines(lines)

def write_general_in_lcs(word_level, data_path, seg_path, n_clusters):
    print(f"\nwrite_general_in_lcs({word_level}, {data_path}, {seg_path}, {n_clusters})\n")
    """
    [CLS] this [MASK] [MASK] sample sent . [SEP] what do you think ? [SEP]$$$is a
    Key difference from write_bert_in: w/ answers
    """
    linenos = []
    if word_level:
        seqs = get_mwp_seqs(data_path) # Simple non-template baseline
    else:
        seqs, linenos, temps2sents = get_template_seqs(seg_path)
    
    seqs = seqs[:n_sequences]
    spls = [[t,] for t in seqs] # spls: list(samples using the seqs)    # NOTE the comma matters a lot!!!
    matrix, lcss = get_lcs_sim_mat(seqs)
    
    print(f"len(seqs)={len(seqs)}; n_clusters={n_clusters}")
    while len(seqs) > n_clusters:
        seqs, spls, matrix, lcss = cluster(seqs, spls, matrix, lcss)
    print(f"len(seqs)={len(seqs)}; n_clusters={n_clusters} (clustered)")
    
    sents,ans = mwp2masked(seqs, spls) if word_level else temp2masked(seqs, spls, temps2sents, data_path, linenos)
    sents_ans = sorted(list(set(zip(sents, ans))))
    sents = [s for s,_ in sents_ans]
    ans = [a for _,a in sents_ans for __ in range(n_preds)]

    new_mwps = fi_tag_filling(sents, '', n_preds, n_items, must_mask=True)

    for m,a in zip(new_mwps, ans):
        assert m.split().count('[MASK]') == len(a.split())

    lines = [f"{m}$$${a}\n" for m,a in zip(new_mwps, ans)]
    with open(os.path.join(data_path,'general_in_lcs.txt'), 'w', encoding='utf-8') as fout:
        fout.writelines(lines)


def my_truncate_seq_pair(tokens_a, ans_a, tokens_b, ans_b, max_num_tokens):
    """
    Truncates a pair of sequences to a maximum sequence length. Lifted from Google's BERT repo.
    * Consider [MASK]s
    """
    while True:
        total_length = len(tokens_a) + len(tokens_b)
        if total_length <= max_num_tokens:
            break

        (trunc_tokens,trunc_ans) = (tokens_a,ans_a) if len(tokens_a) > len(tokens_b) else (tokens_b,ans_b)
        assert len(trunc_tokens) >= 1

        # We want to sometimes truncate from the front and sometimes from the
        # back to add more randomness and avoid biases.
        if random() < 0.5:
            if trunc_tokens[0] == '[MASK]':
                del trunc_ans[0]
            del trunc_tokens[0]
        else:
            if trunc_tokens[-1] == '[MASK]':
                trunc_ans.pop()
            trunc_tokens.pop()

        
def my_create_instances_from_document(
        doc_database, doc_idx, max_seq_length, short_seq_prob,
        masked_lm_prob, max_predictions_per_seq, whole_word_mask, vocab_list):
    """This code is mostly a duplicate of the equivalent function from Google BERT's repo.
    However, we make some changes and improvements. Sampling is improved and no longer requires a loop in this function.
    Also, documents are sampled proportionally to the number of sentences they contain, which means each sentence
    (rather than each document) has an equal chance of being sampled as a false example for the NextSentence task."""
    document = doc_database[doc_idx] # document: a list of (sentence, answer)
    # Account for [CLS], [SEP], [SEP]
    max_num_tokens = max_seq_length - 3

    # We *usually* want to fill up the entire sequence since we are padding
    # to `max_seq_length` anyways, so short sequences are generally wasted
    # computation. However, we *sometimes*
    # (i.e., short_seq_prob == 0.1 == 10% of the time) want to use shorter
    # sequences to minimize the mismatch between pre-training and fine-tuning.
    # The `target_seq_length` is just a rough target however, whereas
    # `max_seq_length` is a hard limit.
    target_seq_length = max_num_tokens
    if random() < short_seq_prob:
        target_seq_length = randint(2, max_num_tokens)

    # We DON'T just concatenate all of the tokens from a document into a long
    # sequence and choose an arbitrary split point because this would make the
    # next sentence prediction task too easy. Instead, we split the input into
    # segments "A" and "B" based on the actual "sentences" provided by the user
    # input.
    instances = []
    current_chunk,current_chunk_ans = [],[]
    current_length = 0
    i = 0
    while i < len(document):
        segment, answer = document[i] # document[i]: the ith sentence
        current_chunk.append(segment)
        current_chunk_ans.append(answer)
        current_length += len(segment)
        if i == len(document) - 1 or current_length >= target_seq_length:
            if current_chunk:
                # `a_end` is how many segments from `current_chunk` go into the `A`
                # (first) sentence.
                a_end = 1
                if len(current_chunk) >= 2:
                    a_end = randrange(1, len(current_chunk))

                tokens_a,ans_a = [],[]
                for j in range(a_end):
                    tokens_a.extend(current_chunk[j]) # Tokens in some sentences go to A
                    ans_a.extend(current_chunk_ans[j])

                tokens_b,ans_b = [],[]

                # Random next
                if len(current_chunk) == 1 or random() < 0.5:
                    is_random_next = True
                    target_b_length = target_seq_length - len(tokens_a)

                    # Sample a random document, with longer docs being sampled more frequently
                    random_document = doc_database.sample_doc(current_idx=doc_idx, sentence_weighted=True)

                    random_start = randrange(0, len(random_document))
                    for j in range(random_start, len(random_document)):
                        tokens_b.extend(random_document[j][0]) # The others go to B
                        ans_b.extend(random_document[j][1])
                        if len(tokens_b) >= target_b_length:
                            break
                    # We didn't actually use these segments so we "put them back" so
                    # they don't go to waste.
                    num_unused_segments = len(current_chunk) - a_end
                    i -= num_unused_segments
                # Actual next
                else:
                    is_random_next = False
                    for j in range(a_end, len(current_chunk)):
                        tokens_b.extend(current_chunk[j])
                        ans_b.extend(current_chunk_ans[j])
                my_truncate_seq_pair(tokens_a, ans_a, tokens_b, ans_b, max_num_tokens)

                assert len(tokens_a) >= 1
                assert len(tokens_b) >= 1

                tokens = ["[CLS]"] + tokens_a + ["[SEP]"] + tokens_b + ["[SEP]"]
                masked_lm_labels = ans_a + ans_b # answer. Name changed to prevent confusion
                # The segment IDs are 0 for the [CLS] token, the A tokens and the first [SEP]
                # They are 1 for the B tokens and the final [SEP]
                segment_ids = [0 for _ in range(len(tokens_a) + 2)] + [1 for _ in range(len(tokens_b) + 1)]

                masked_lm_positions = [i for i,w in enumerate(tokens) if w == '[MASK]']
                #tokens, masked_lm_positions, masked_lm_labels = create_masked_lm_predictions(
                #    tokens, masked_lm_prob, max_predictions_per_seq, whole_word_mask, vocab_list)

                instance = {
                    "tokens": tokens,
                    "segment_ids": segment_ids,
                    "is_random_next": is_random_next,
                    "masked_lm_positions": masked_lm_positions,
                    "masked_lm_labels": masked_lm_labels}
                instances.append(instance)
            current_chunk = []
            current_chunk_ans = []
            current_length = 0
        i += 1

    return instances


def my_create_training_file(docs, vocab_list, args, epoch_num):
    epoch_filename = args.output_dir / "epoch_{}.json".format(epoch_num)
    num_instances = 0
    with epoch_filename.open('w') as epoch_file:
        for doc_idx in trange(len(docs), desc="Document"):
            doc_instances = my_create_instances_from_document(
                docs, doc_idx, max_seq_length=args.max_seq_len, short_seq_prob=args.short_seq_prob,
                masked_lm_prob=args.masked_lm_prob, max_predictions_per_seq=args.max_predictions_per_seq,
                whole_word_mask=args.do_whole_word_mask, vocab_list=vocab_list)
            doc_instances = [json.dumps(instance) for instance in doc_instances]
            for instance in doc_instances:
                epoch_file.write(instance + '\n')
                num_instances += 1
    metrics_file = args.output_dir / "epoch_{}_metrics.json".format(epoch_num)
    with metrics_file.open('w') as metrics_file:
        metrics = {
            "num_training_examples": num_instances,
            "max_seq_len": args.max_seq_len
        }
        metrics_file.write(json.dumps(metrics))


def main(args):
    print(f"\nmain({args})\n")
    tokenizer = BertTokenizer.from_pretrained(args.bert_model, do_lower_case=args.do_lower_case)
    vocab_list = list(tokenizer.vocab.keys())
    if args.rand_mask > 0:
        fin_name = 'general_in_rand_mask.txt'  
        args.output_dir = args.output_dir / 'rand_mask_bert_pregen'
    else:
        fin_name = 'general_in_lcs.txt'
        args.output_dir = args.output_dir / 'lcs_bert_pregen'

    with DocumentDatabase(reduce_memory=args.reduce_memory) as docs:
        with open(os.path.join(args.data_path,fin_name)) as f:
            for line in tqdm(f, desc="Loading Dataset", unit=" lines"):
                # mwp_ans is a list of tuples ('hello [MASK] ! [SEP] how are you ? [SEP]', 'world')
                mwp, ans = line[6:].strip().split('$$$')   # [6:] to avoid "[CLS] "
                sents = mwp.split(' [SEP]')[:-1]
                ans = ans.split()
                ans = [[ans.pop(0) for _ in range(s.count('[MASK]'))] for s in sents]
                #docs.add_document(list(zip([tokenizer.tokenize(s) for s in sents], ans)))
                docs.add_document(list(zip([s.split() for s in sents], ans))) # It's bert-tokenized in make_data
        assert len(docs) > 1
        args.output_dir.mkdir(exist_ok=True)
        for epoch in range(args.epochs_to_generate):
            my_create_training_file(docs, vocab_list, args, epoch)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    
    parser.add_argument('-data_path', type=str, default='', help='path to data dir')
    parser.add_argument('-rand_mask', type=int, default=0, help='ignore any masking scheme and randomly mask some')

    parser.add_argument('-seg_path', type=str, default='', help='path to seg file')
    parser.add_argument('-word_level', action='store_true', help='for word_level baseline')
    parser.add_argument('-n_clusters', type=int, default='', help='number of clusters desired')
    
    #parser.add_argument('--train_corpus', type=Path, required=True)
    parser.add_argument("--output_dir", type=Path, required=True)
    parser.add_argument("--bert_model", type=str, required=True)
    parser.add_argument("--do_lower_case", action="store_true")
    parser.add_argument("--do_whole_word_mask", action="store_true",
                        help="Whether to use whole word masking rather than per-WordPiece masking.")
    parser.add_argument("--reduce_memory", action="store_true",
                        help="Reduce memory usage for large datasets by keeping data on disc rather than in memory")

    #parser.add_argument("--num_workers", type=int, default=1,
    #                    help="The number of workers to use to write the files")
    parser.add_argument("--epochs_to_generate", type=int, default=3,
                        help="Number of epochs of data to pregenerate")
    parser.add_argument("--max_seq_len", type=int, default=128)
    parser.add_argument("--short_seq_prob", type=float, default=0.1,
                        help="Probability of making a short sentence as a training example")
    parser.add_argument("--masked_lm_prob", type=float, default=0.15,
                        help="Probability of masking each token for the LM task")
    parser.add_argument("--max_predictions_per_seq", type=int, default=20,
                        help="Maximum number of tokens to mask in each sequence")
    args = parser.parse_args()
    print(args)

    if args.rand_mask > 0:
        write_general_in_rand_mask(args.data_path, args.rand_mask)
    else:
        write_general_in_lcs(args.word_level, args.data_path, args.seg_path, args.n_clusters)
    main(args)
