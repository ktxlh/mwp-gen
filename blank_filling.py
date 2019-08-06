# -*- coding: utf-8 -*-
import os
import argparse
import names
from random import shuffle, choice, randint
from my_utils import parse_seg_file, re_sort_metadata
from generate import load_model, get_seed_sent, masked_decoding
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM
from pyclustering.cluster.kmedoids import kmedoids
#from sklearn.cluster import SpectralClustering, AgglomerativeClustering
import numpy as np
#import textdistance # .lcsstr for consecutive; otherwise; .lcsseq
    

bert_version = "bert-large-cased" # bert-(base|large)-(un)?cased

EOS = "<eos>"
NUMBER = "<num>"    
UNK = "<unk>"
MASK = "[MASK]"
#seqs=None #debug only

def get_bert():
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
    Paramters:
    ---------
        seqs    list of list
            e.g. [[0,1,2],[3,1]] is for 2 MWPs and variable-length input
    Returns:
    ---------
        len(seqs) x len(seqs) numpy similarity matrix
    """
    # TODO: Don't repeat computing for seen pairs! (For now, recompute for each level)
    print("Computing lcs similarity matrix...")
    sim = np.zeros((len(seqs),len(seqs)))
    lcss = [[None]*len(seqs) for _ in range(len(seqs))]
    for si1,s1 in enumerate(seqs):
        for si2,s2 in enumerate(seqs):
            if si2 < si1: # Lower triangular, id2 < id1
                lcs_len,lcs = compute_lcs(s1, s2)
                sim[si1,si2] = lcs_len +1 # connected graph
                lcss[si1][si2] = lcs
    sim = sim + sim.transpose() # Full
    #scheme == 'editdist': # hamming distance is only for comparing strings of the same length
    return sim,lcss
    

def get_template_seqs(seg_path):
    linenos, temps2sents, top_temps = parse_seg_file(seg_path)
    return top_temps, linenos, temps2sents

def get_mwp_seqs(data_path):
    seqs= None,None
    with open(os.path.join(data_path,'train.txt'),'r',encoding='utf-8') as f:
        seqs = [line.split('|||')[0].split() for line in list(f.readlines())]
    return seqs

def cluster(seqs, spls):#, n_clusters):#, scheme):
    ## Commented code doesn't make sense. '
    ## ab' and 'ac' is close; 'ab' and 'db' is close; 
    ## but 'ac' and 'db' should not be clustered together. 
    ## LCS does not imply mutual similarity of multiple strings.
    #clusters = None
    #if scheme == 'spectral':
    #    clustering = SpectralClustering(n_clusters=n_clusters,affinity='precomputed').fit(matrix)
    #elif scheme == 'hierarchical':
    #clustering = AgglomerativeClustering(n_clusters=n_clusters,affinity='precomputed',linkage='average').fit(matrix)
    ## clustering.labels_ is a list of labels indicating the cluster each seq belongs to
    #clusters = [[] for _ in range(n_clusters)]
    #for lid,l in enumerate(clustering.labels_):
    #   clusters[l].append(lid) 
    print("len seqs:",len(seqs))
    matrix,lcss = get_lcs_sim_mat(seqs)
    ids = sorted([matrix.argmax(None)//len(seqs), matrix.argmax(None)%len(seqs)],reverse=True)
    new_seqs = [s for si,s in enumerate(seqs) if si not in ids]
    new_spls = [s for si,s in enumerate(spls) if si not in ids]
    new_seqs.append(lcss[ids[0]][ids[1]])  # Newest cluster last
    new_spls.append(spls[ids[0]] + spls[ids[1]])
    return new_seqs,new_spls # [[0],[1,5],[2],[3,4]] is 4 clusters, each of several indices corresponding to seqs

def temp2masked(seqs, spls, temps2sents):
    """
    Parameters:
    ----------
        seqs    list of template lcs
        spls    list of set of temps using of which their lcs is seqs
        temps2sents     dict temp -> [([phrases],lineno)]
    Returns:
    ----------
        temps   list of masked sents
    """
    #MASK = '[MASK]'#'_'
    # TODO: Counter() for most common list of phrases in the fixed positions, and use the most common combination only
    # For now, it's simply hollowing out the non-fixed segments
    new_sents = []
    for seq,spl in zip(seqs,spls):          # iterate lcs
        for sp in spl:                      # iterate sample templates set
            for segs,_ in temps2sents[sp]:  # iterate mwps using that sample templates # (_ is lineno)
                new_tokes = []
                for s,g in zip(sp,segs):    # iterate segments
                    if s in seq:
                        new_tokes.append(g)
                    else:
                        new_tokes.extend([MASK]*len(g.split()))
                new_sent = ' '.join(' '.join(new_tokes).split()[:-1]) #HACK: exclude <eos>
                new_sents.append(new_sent)
    return new_sents

def mwp2masked(seqs, spls):
    # Baseline model: not using tempalte at all
    pass

def read_ner_file(nerf_path):
    """
    Read the ners & nums from training data to recover them
    # Not necessary. Do it later.
    """
    ners = []
    with open(nerf_path,'r') as f:
        pass

def fill_tags(tokens,nums,nams):
    n_preds = len(nams)
    fixed_rand_wid = randint(0,len(tokens)-1)
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
            elif token == UNK:
                token = MASK
                n_masks += 1
            elif token == MASK:
                n_masks += 1
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
        new_mwps.append(" ".join(new_tokens))
    return new_mwps

def substitute_seg(seg_path, data_path):
    n_preds = 5
    n_items = 10 # How many <PER_i>, <num>, ...?
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
            tokens = [s for segment in segments for s in segment.split()]
            #print("IN:"," ".join(segments),lineno)
            #fixed_rand_wid = choice(tags[linenos[lineno]][:-1])[0] # buggy here
            new_mwps = fill_tags(tokens,nums,nams)
            #print("OUT:",new_mwps)
            fout.writelines('\n'.join(new_mwps)+"\n")
    fout.close()

def test_bert(pathin,pathout):
    tokenizer,model = get_bert()
    lines_in = list((open(pathin, 'r',encoding='utf-8')).readlines())
    fout = open(pathout,'w',encoding='utf-8')
    for seed_sentence in lines_in:
        toks, seg_tensor, mask_ids = get_seed_sent(seed_sentence, tokenizer, masking="none", n_append_mask=0)
        toks = masked_decoding(toks, seg_tensor, mask_ids, model, tokenizer, "argmax")
        print("Final: %s\n" % (" ".join(toks)))
        fout.writelines("IN\t"+seed_sentence)
        fout.writelines("OUT\t"+" ".join(toks)+'\n\n')
    fout.close()

parser = argparse.ArgumentParser(description='')
parser.add_argument('-seg_path', type=str, default='', help='path to seg file')
parser.add_argument('-data_path', type=str, default='', help='path to data dir')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    bertin = 'bert_masklcs.in'
    bertout = bertin.split('.')[0]+'.out'
    
    n_preds = 1
    n_items = 10 # How many <PER_i>, <num>, ...?
    nums = [str(i+1) for i in range(n_items)]  # Different preds shares same numbers
    shuffle(nums)
    nams = [[names.get_first_name() for i in range(n_items)] for j in range(n_preds)]

    #substitute_seg(args.seg_path, args.data_path)

    seqs, linenos, temps2sents = get_template_seqs(args.seg_path)
    #seqs = get_mwp_seqs(args.data_path)
    seqs = seqs[:100]

    spls = [[t] for t in seqs] # spls: list(samples using the seqs)
    n_clusters = 40
    while len(seqs) > n_clusters:
        seqs, spls = cluster(seqs, spls)
    print(seqs)
    sents = temp2masked(seqs, spls, temps2sents)
    sents = sorted(list(set(sents)))
    new_mwps = [fill_tags(sent.split(),nums,nams) for sent in sents]
    new_mwps = [t for s in new_mwps for t in s]
    lines = '\n'.join(new_mwps)+'\n'

    with open(bertin,'w') as f:
        f.writelines(lines)
    
    test_bert(bertin, bertout)