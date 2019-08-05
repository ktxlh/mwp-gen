# -*- coding: utf-8 -*-
import os
import argparse
import names
from random import shuffle, choice
from my_utils import parse_seg_file, re_sort_metadata
from generate import load_model, get_seed_sent, masked_decoding
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM, BertForMaskedLM

bert_version = "bert-large-uncased" # bert-(base|large)-(un)?cased
print(f"Loading BERT ({bert_version})...")
tokenizer = BertTokenizer.from_pretrained(bert_version)
model = load_model(bert_version)
print("BERT loaded.")

EOS = "<eos>"
NUMBER = "<num>"    
UNK = "<unk>"
MASK = "[MASK]"

def get_sim_mat(lines, scheme='lcsseq'):
    """
    Returns:
    ---------
    len(lines) x len(lines) numpy similarity matrix
    """
    import numpy as np
    import textdistance # .lcsstr for consecutive; otherwise; .lcsseq
    from nltk import word_tokenize
    sim = None
    def compute_sim(func, inpts):
        sim = [[ func(line1, line2) for lid2,line2 in enumerate(seqs) if lid2 < lid1] for lid1,line1 in enumerate(inpts)]
        # Lower triangular matrix for similarity. i.e. indices: sim[biger][smaller]
        # x x
        # o x   
        for a in range(len(sim)):
            for b in range(a,len(sim)):
                sim[a].append(sim[b][a] if a!=b else 0)
                # 0 o
                # o 0
        return sim
    if scheme == 'lcsseq':
        seqs = [word_tokenize(line) for line in lines]
        ##### HACK: neg dis for now
        sim = compute_sim( (lambda l1,l2: -len(textdistance.lcsseq(l1,l2))), seqs)
        #sim = [[ - len(textdistance.lcsseq(line1,line2)) for lid2,line2 in enumerate(seqs) if lid2 < lid1] for lid1,line1 in enumerate(seqs)]
    elif scheme == 'editdist':
        sim = [[ ]  for lid1,line1 in enumerate(seqs)]
    return sim #np.array(sim) 
    

def lcs_subtemplate(seg_path):  #, metadata_path
    linenos, temps2sents, top_temps = parse_seg_file(seg_path)
    #metadata = re_sort_metadata(metadata_path, linenos, new_idxname='seg_linenos')

    # Get subtemplate
    

def lcs_subsentence(data_path):
    """
    Baseline. Cluster the training data directly.
    """
    with open(os.path.join(data_path,'train.txt'),'r') as f:
        lines = f.readlines()
        sim = get_sim_mat(lines, 'lcsseq')
        
        # Hierarchical Clustering



        


def read_ner_file(nerf_path):
    """
    Read the ners & nums from training data to recover them
    # Not necessary. Do it later.
    """
    ners = []
    with open(nerf_path,'r') as f:
        pass

def substitute_seg(seg_path, data_path):
    n_preds = 5
    n_items = 30 # How many <PER_i>, <num>, ...?
    # TODO: Get nums & names (only) from training data
    nums = [str(i) for i in range(n_items)]  # Different preds shares same numbers
    shuffle(nums)
    nams = [[names.get_first_name() for i in range(n_items)] for j in range(n_preds)]
    
    fout = open("berttest.in",'w',encoding='utf-8')
    linenos, temps2sents, top_temps = parse_seg_file(seg_path)
    metadata = re_sort_metadata(os.path.join(data_path,'metadata_train.tsv'), linenos, new_idxname='seg_linenos')

    train_tagged = list((open(os.path.join(data_path,"train.txt"),'r',encoding='utf-8')).readlines())
    tags = [[tuple(int(a) for a in t.split(',')) for t in line.strip().split('|||')[1].split()] for line in train_tagged]

    for temp in top_temps:
        for (segments,lineno) in temps2sents[temp]:
            
            #print("IN:"," ".join(segments),lineno)
            fixed_rand_wid = choice(tags[linenos[lineno]][:-1])[0]
            for pid in range(n_preds):
                # Handle: <PER_i>, <unk>, <num>
                numid,n_masks = 0,0
                new_tokens = []
                for segment in segments:
                    tokens = segment.split()
                    for token in tokens:
                        if token == NUMBER:
                            token = nums[numid] # Assume each number is different
                            numid += 1
                        elif token.startswith('<PER_'):
                            namid = int(token[5:-1])-1   # 1-indexed to 0-indexed
                            token = nams[pid][namid]
                        elif token == UNK:
                            token = MASK
                        elif token == EOS:
                            break
                        new_tokens.append(token)
                # TODO so what do i want to mask??? nouns?
                # Read the src_ and randomly mask some word for now
                if n_masks == 0:
                    try:
                        new_tokens[ fixed_rand_wid ] = MASK
                    except Exception as e:
                        print(e)
                        continue
                new_sent = " ".join(new_tokens)
                #print("OUT:",new_sent)
                fout.writelines(new_sent+"\n")
    fout.close()
    

def test_bert():#seed_sentence, masking):
    #seed_sentence = "Two [MASK] weighs 3 [MASK] . How much do 3 [MASK] weigh ?"
    #seed_sentence = "There are <num> candies in <PER_1> 's candy collection . If the candies are organized into <num> groups , how big is each group ?"
    #seed_sentence = "There are 3 [MASK] in Mary 's [MASK] collection . If the [MASK] are organized into 3 groups , how big is each group ?"
    #seed_sentence = "<PER_1> has <num>|271 books|40 . <num> are <unk>|215 school|180 and the|148 rest|42 are <unk>|182 <unk>|53 . How many|162 books|251 <unk>|72 <unk>|222 does <PER_1> have|214 ? <eos>|139 "
    #masking = "none" #','.join([str(sid) for sid,s in enumerate(seed_sentence.split()) if s.startswith('<')])
    lines_in = list((open("berttest.in", 'r',encoding='utf-8')).readlines())
    fout = open("berttest.out",'w',encoding='utf-8')
    for seed_sentence in lines_in:
        toks, seg_tensor, mask_ids = get_seed_sent(seed_sentence, tokenizer, masking="none", n_append_mask=0)
        toks = masked_decoding(toks, seg_tensor, mask_ids, model, tokenizer, "argmax")
        print("Final: %s" % (" ".join(toks)))
        fout.writelines(" ".join(toks)+'\n')
    fout.close()

parser = argparse.ArgumentParser(description='')
parser.add_argument('-seg_path', type=str, default='', help='path to seg file')
parser.add_argument('-data_path', type=str, default='', help='path to data dir')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    seg_path = args.seg_path
    substitute_seg(seg_path, args.data_path)
    test_bert()#seed_sentence, masking) 
    