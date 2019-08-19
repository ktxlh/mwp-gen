# -*- coding: utf-8 -*-
"""
TODO: [UNK],[SEP],[PAD]
"""
import argparse
import os
from random import choice, random, shuffle

#import names
names = [line.strip() for line in open('names.txt','r').readlines()]

#from sklearn.cluster import SpectralClustering, AgglomerativeClustering
import numpy as np
from nltk.tokenize import sent_tokenize
from pyclustering.cluster.kmedoids import kmedoids
from pytorch_pretrained_bert import BertForMaskedLM, BertTokenizer

from generate import get_seed_sent, load_model, masked_decoding
from my_utils import parse_seg_file, re_sort_metadata

#import textdistance # .lcsstr for consecutive; otherwise; .lcsseq


EOS = "<eos>"
NUMBER = "<num>"    
UNK_IN = "<unk>"    # TODO: unified this token
UNK_BERT = "[UNK]"
SEP = "[SEP]"
MASK = "[MASK]"
CLS = "[CLS]"
#seqs=None #debug only

def get_bert(bert_version):
    print(f"Loading BERT ({bert_version})...")
    tokenizer = BertTokenizer.from_pretrained(bert_version)
    model = load_model(bert_version)
    print("BERT loaded.")
    return tokenizer,model

def compute_lcs(X, Y): 
    UP_LEFT,UP,LEFT = 0,1,2
    m,n = len(X),len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)] # L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    V = [[None]*(n + 1) for i in range(m + 1)] # for recovering lcs
    
    def recover_lcs():
        lcs = []
        i,j = m,n
        while i > 0 and j > 0:
            if V[i][j] == UP_LEFT:
                lcs = [X[i-1]] + lcs
                i,j = i-1,j-1
            else:
                (i,j) = (i-1,j) if V[i][j] == UP else (i,j-1)
        return lcs

    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
                V[i][j] = UP_LEFT
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
                V[i][j] = UP if L[i][j]==L[i-1][j] else LEFT
    
    return L[m][n], recover_lcs()

def get_lcs_sim_mat(seqs):
    """
    Get longest common subsequence similarity matrix.

    Paramters:
    ---------
        seqs    list of list
            e.g. [[0,1,2],[3,1]] is for 2 MWPs and variable-length input
    Returns:
    ---------
        len(seqs) x len(seqs) numpy similarity matrix
    """
    print("Computing lcs similarity matrix...")
    sim = np.zeros((len(seqs),len(seqs)))
    lcss = [[None]*len(seqs) for _ in range(len(seqs))]
    for si1,s1 in enumerate(seqs):
        for si2,s2 in enumerate(seqs):
            if si2 >= si1:  # Lower triangular, id2 < id1
                break
            lcs_len,lcs = compute_lcs(s1, s2)
            sim[si1,si2] = lcs_len +1 # connected graph
            lcss[si1][si2] = lcs
    sim = sim + sim.transpose() # Full
    return sim,lcss
    

def get_template_seqs(seg_path):
    linenos, temps2sents, top_temps = parse_seg_file(seg_path)  
    # The seg_path was from train.txt unless specified 
    # when training neural tempplate (so using the same split of data from all models!)
    return top_temps, linenos, temps2sents

def get_mwp_seqs(data_path):    
    seqs= None
    with open(os.path.join(data_path,'train.txt'),'r',encoding='utf-8') as f:
        # HACK avoid duplicated
        seqs = [s for s in set([tuple(line.split('|||')[0].split()) for line in list(f.readlines())])]
    return seqs

def update_lcs_sim_mat(ids, new_seqs, matrix, lcss):
    """
    * ids[0] > ids[1]
    * lcss is lower triangular
    """
    # Delete 2 rows & cols
    for o in [0,1]:
        del lcss[ids[o]] # row
        for lcs in lcss: # col
            if len(lcs) > ids[o]:
                del lcs[ids[o]]

        for a in [0,1]: # row & col
            matrix = np.delete(arr=matrix,obj=ids[o], axis=a)

    # Add 1 row & col
    new_mat = np.zeros((len(new_seqs),len(new_seqs)))
    new_mat[:-1,:-1] = matrix
    lcss.append([0 for i in range(len(new_seqs)-1)])
    for si,seq in enumerate(new_seqs[:-1]):
        lcs_len,lcs = compute_lcs(new_seqs[-1], seq)
        new_mat[-1,si] = lcs_len +1 # connected graph
        new_mat[si,-1] = new_mat[-1,si] # symmetry full matrix
        lcss[-1][si] = lcs # keep lower triangular
    return new_mat, lcss

def cluster(seqs, spls, matrix, lcss): 
    # heapq so extract-max O(n) -> O(log n)? 
    # No, you modify O(n) elements. heapify does not help.

    print("len seqs:",len(seqs))
    ids = sorted([matrix.argmax(None)//len(seqs), matrix.argmax(None)%len(seqs)],reverse=True)  # [greater,less]
    new_seqs = [s for si,s in enumerate(seqs) if si not in ids]
    new_spls = [s for si,s in enumerate(spls) if si not in ids]
    new_seqs.append(lcss[ids[0]][ids[1]])  # Newest cluster last
    new_spls.append(spls[ids[0]] + spls[ids[1]])

    print(f"{seqs[ids[0]]}, {seqs[ids[1]]} -> {new_seqs[-1]}")

    # Update sim matrix
    matrix, lcss = update_lcs_sim_mat(ids, new_seqs, matrix, lcss)
    # [[0],[1,5],[2],[3,4]] is 4 clusters, 
    # each of several indices corresponding to seqs
    return new_seqs,new_spls,matrix,lcss 

def temp2masked(seqs, spls, temps2sents):
    """
    Parameters:
    ----------
        seqs    list of template lcs
        spls    list of set of temps using of which their lcs is seqs
        temps2sents     dict temp -> [([phrases],lineno)]
    Returns:
    ----------
        new_sents   list of "[CLS] hello [MASK] ! [SEP]"
        ans         list of "world"
    """
    # TODO: Counter() for most common list of phrases 
    # in the fixed positions, and use the most common combination only
    # For now, it's simply hollowing out the non-fixed segments
    OTHER_CODE = -1
    new_sents,ans = [],[]
    for seq,spl in zip(seqs,spls):          # iterate lcs
        for sp in spl:                      # iterate sample templates set
            for segs,_ in temps2sents[sp]:  # iterate mwps using that sample templates # (_ is lineno)

                # TODO doesn't make sense to use more than two sentences
                # See https://github.com/google-research/bert/issues/395 for details
                # Suggestion: use unused1 (See vocab.txt) if needed => but it requires extra training :3
                old_states = [ state for state,seg in zip(sp,segs) for _ in range(len(seg.split()))]
                mwp = f'{CLS} '+f' {SEP} '.join(sent_tokenize(' '.join(segs).replace(' '+EOS,'')))+f' {SEP}'
                new_states = [OTHER_CODE if word in {SEP,CLS} else old_states.pop(0) for word in mwp.split()]
                
                new_tokes,new_maskeds = [],[]
                seq_copied = list(seq)
                for s,w in zip(new_states,mwp.split()): # iterate words
                    if len(seq_copied) > 0 and s == seq_copied[0]:
                        new_tokes.append(w)
                        del seq_copied[0]
                    elif s == OTHER_CODE:
                        new_tokes.append(w)
                    #elif s == EOS: # should've been avoided
                    #    continue
                    else:
                        new_tokes.append(MASK)
                        new_maskeds.append(w)
                new_sents.append(' '.join(new_tokes))
                ans.append(' '.join(new_maskeds))
    return new_sents,ans

def mwp2masked(seqs, spls):
    # Baseline model: not using tempalte at all
    new_sents,ans = [],[]
    for seq,spl in zip(seqs,spls):          # iterate lcs
        for sp in spl:                      # iterate sample templates set
            mwp = f'{CLS} '+f' {SEP} '.join(sent_tokenize(' '.join(sp).replace(' '+EOS,'')))+f' {SEP}'
            new_tokes,new_maskeds = [],[]
            seq_copied = list(seq)
            for w in mwp.split(): # iterate words
                if len(seq_copied) > 0 and w == seq_copied[0]:
                    new_tokes.append(w)
                    del seq_copied[0]
                elif w in {CLS, SEP}:
                    new_tokes.append(w)
                else:
                    new_tokes.append(MASK)
                    new_maskeds.append(w)
            new_sents.append(' '.join(new_tokes))
            ans.append(' '.join(new_maskeds))
    return new_sents,ans

def read_ner_file(nerf_path):
    """
    Read the ners & nums from training data to recover them
    # Not necessary. Do it later.
    """
    ners = []
    with open(nerf_path,'r') as f:
        pass

def fill_tags(tokens,nums,nams,must_mask):
    n_preds = len(nams)
    fixed_rand = random()
    new_mwps = []
    for pid in range(n_preds):
        numid,n_masks = 0,0
        new_tokens = []
        for token in tokens:  # Handle: <PER_i>, <unk>, <num>
            if token == NUMBER:
                token = nums[numid] # Assume each number is different
                numid += 1
            elif token.startswith('<PER_'):
                namid = int(token[5:-1])-1   # 1-indexed to 0-indexed
                token = nams[pid][namid]
            elif token == UNK_IN:
                token = MASK #UNK_BERT
            elif token == MASK:
                n_masks += 1
            elif token == EOS:
                break
            new_tokens.append(token)
        # TODO so what do i want to mask??? nouns?
        # Read the src_ and randomly mask some word for now
        if n_masks == 0 and must_mask:
            try:
                new_tokens[ int(fixed_rand*len(new_tokens)) ] = MASK
            except Exception as e:
                print(e)
                continue
        new_mwps.append(" ".join(new_tokens))
    return new_mwps
    

def bert_prediction(pathin,pathout,bert_version,gibbs):
    lines_in = list((open(pathin, 'r',encoding='utf-8')).readlines())
    with open(pathout,'w',encoding='utf-8') as fout:
        tokenizer,model = get_bert(bert_version)
        for seed_sentence in lines_in:
            toks, seg_tensor, mask_ids = get_seed_sent(
                seed_sentence, tokenizer, masking="none", n_append_mask=0)
            
            # Gibbs Sampling (from left to right == auto-regression?)
            #enum = [i for i in range(len(toks)) if toks[i] not in {'[SEP]','[CLS]'} ] # and i not in mask_ids
            mask_ids = mask_ids * gibbs #+ enum * gibbs

            toks = masked_decoding(toks, seg_tensor, mask_ids, model, tokenizer, "argmax")
            toks = [tok.replace(' ##','') for tok in toks]
            print("Final: %s\n" % (" ".join(toks)))
            fout.writelines("IN\t"+seed_sentence)
            fout.writelines("OUT\t"+" ".join(toks)+'\n\n')
                        

def fi_tag_filling(sents, new_gen_fi, n_preds, n_items,must_mask):
    """
    Fill in the <num> and <PER_#> and write it to new_gen_fi
    Parameters:
    ----------
        sents   list of list
        new_gen_fi  if set to '', does not write file
    Returns:
    ---------
        new_mwps    a list of n_preds*len(sents) new MWPs
    """
    
    def get_num_nam(n_preds, n_items):
        nums = [str(i+1) for i in range(n_items)]  # Different preds shares same numbers
        shuffle(nums)
        #nams = [[names.get_first_name() for i in range(n_items)] for j in range(n_preds)]
        nams = [names[:n_items] for j in range(n_preds)]
        return nums, nams

    nums, nams = get_num_nam(n_preds, n_items)
    new_mwps = [fill_tags(sent.split(),nums,nams,must_mask) for sent in sents]
    new_mwps = [t for s in new_mwps for t in s] # because n_preds MWPs were grouped together
    lines = '\n'.join(new_mwps)+'\n'

    if new_gen_fi != '':
        with open(new_gen_fi,'w',encoding='utf-8') as fout:
            fout.writelines(lines)        
        fout.writelines(lines)
            fout.writelines(lines)        
    return new_mwps

def substitute_seg(seg_path, data_path, bert_in, n_preds, n_items):
    """
    Replace <num>, <PER_#> in segmentation file with [MASK]
    * Not required. 
    """
    linenos, temps2sents, top_temps = parse_seg_file(seg_path)
    #metadata = re_sort_metadata(os.path.join(data_path,'metadata_train.tsv'), linenos, new_idxname='seg_linenos')

    train_tagged = list((open(os.path.join(data_path,"train.txt"),'r',encoding='utf-8')).readlines())
    tags = [[tuple(int(a) for a in t.split(',')) for t in line.strip().split('|||')[1].split()] for line in train_tagged]

    sents = [" ".join(segments).split() for temp in top_temps for (segments,_) in temps2sents[temp]]
    fi_tag_filling(sents, bert_in, n_preds, n_items, must_mask=True)

    # TODO use tags (& metadata?) for substitution
    # src: know which tag
    # metadata: know where to tag   

def gen_fi_tag_filling(old_fi_path,new_gen_fi,n_preds, n_items):
    """
    """
    with open(old_fi_path,'r', encoding='utf-8') as fin:
        sents = [line.split('|||')[0].replace('(c) ','').split()  for line in fin.readlines() if '|||' in line]
        fi_tag_filling(sents, new_gen_fi, n_preds, n_items, must_mask=False)
   

parser = argparse.ArgumentParser(description='')
parser.add_argument('-seg_path', type=str, default='', help='path to seg file')
parser.add_argument('-data_path', type=str, default='', help='path to data dir')
parser.add_argument('-bert_in', type=str, default='', help='path to bert in file (may be generated)')
parser.add_argument('-bert_out', type=str, default='', help='path to bert out file')
parser.add_argument('-bert_version', type=str, default='',help='bert-(base|large)-(un)?cased(-whole-word-masking(-finetuned-squad)?)?')
parser.add_argument('-write_bert_in', action='store_true', help='')
parser.add_argument('-word_level', action='store_true', help='for word_level baseline')
parser.add_argument('-n_clusters', type=int, default='', help='number of clusters desired')
parser.add_argument('-gibbs', type=int, default='1', help='number of bert prediction iteration (gibbs sampling)')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    n_preds = 1
    n_items = 20 # How many <PER_i>, <num>, ...?
    n_sequences = int(1e7) # 100K = 1e5 samples in the current largest dataset => 1e7 means infinity

    def write_bert_in():
        
        #substitute_seg(args.seg_path, args.data_path, args.bert_in, n_preds, n_items)

        if args.word_level:
            seqs = get_mwp_seqs(args.data_path) # Simple non-template baseline
        else:
            seqs, linenos, temps2sents = get_template_seqs(args.seg_path)
        
        seqs = seqs[:n_sequences]
        spls = [[t,] for t in seqs] # spls: list(samples using the seqs)    # NOTE the comma matters a lot!!!
        matrix, lcss = get_lcs_sim_mat(seqs)
        
        print(f"len(seqs)={len(seqs)}; args.n_clusters={args.n_clusters}")
        while len(seqs) > args.n_clusters:
            seqs, spls, matrix, lcss = cluster(seqs, spls, matrix, lcss)
        print(f"len(seqs)={len(seqs)}; args.n_clusters={args.n_clusters} (clustered)")
        #print(seqs) # NOTE for temps, lists are merged; tuples aren't.
        
        sents,_ = mwp2masked(seqs, spls) if args.word_level else temp2masked(seqs, spls, temps2sents)
        sents = sorted(list(set(sents)))

        fi_tag_filling(sents, args.bert_in, n_preds, n_items, must_mask=True)
    
    if args.write_bert_in:
        write_bert_in()
    bert_prediction(args.bert_in, args.bert_out, args.bert_version, args.gibbs)
