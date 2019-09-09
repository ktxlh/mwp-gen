"""
Produce data tailored for GAN, i.e.
1. with solution type
2. custom mask scheme
NOTE: For simplification, make_bert_data is not used here
as it is from train.txt, which is for templates
and does not contain solution type; it was also too small (2.4k train)

Desired configuration:
* NER tag: <PER_#> & <num>?
* Size of subset
* Where to mask
* How many masks
"""
import json
import os
import random
from random import sample
from nltk.tokenize import sent_tokenize
from tqdm import trange

from pytorch_transformers.tokenization_bert import BertTokenizer
random.seed(53)
CLS='[CLS]'
SEP='[SEP]'

def make_gan_data(mathqa_train, out_dir, 
        bert_model, do_lower_case, subset=1e8):
    print('ma')
    """
    Parameters:
        mathqa_train    str
            path to MathQA train.json
        out_dir str
            path to output dir
        subset  int
            size of subset adopted
    NOTE: use the whole train set rather than 3k 
    (actually 2.4k) for training
    """
    def is_bad(sent):
        # 21476 out of 29837 MWPs used (0.7198)
        if any([s in '+-*/|@' for s in sent]):
            return True 
        return True if sum([1 for s in sent if s.isalpha()]) < len(sent)/2 else False
    
    obj = []
    with open(mathqa_train,'r') as jsonfile:
        obj = json.load(jsonfile)
        print(f'{len(obj)} MWPs from {mathqa_train}')

    good_mwps,bad_mwps = [],[]
    for imwp in trange(len(obj)):
        mwp = obj[imwp]
        if is_bad(mwp['Problem']): #or mwp['category'] == 'other':#TODO
            bad_mwps.append(mwp)
            continue # 27688 out of 29837, i.e. 92.8% kept
        
        good_mwps.append(mwp)
        if len(good_mwps) == subset:
            break

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    tokenizer = BertTokenizer.from_pretrained(bert_model, do_lower_case=do_lower_case)
    with open(os.path.join(out_dir,'mathqa.txt'), 'w') as fout:
        for imwp in trange(len(good_mwps)):
            mwp = good_mwps[imwp]
            problem = ' [SEP]'.join(sent_tokenize(mwp['Problem']))+' [SEP]'
            toks = [CLS]
            for tok in problem.split():
                if tok is not SEP:
                    toks.extend(tokenizer.tokenize(tok))
                    #if random() > 0.5:
                    #    toks.extend(['[MASK]']*len(tokenizer.tokenize(tok)))
                else:
                    toks.append(SEP)
            fout.writelines(' '.join(toks)+'@@@'+mwp['category']+'\n')

def random_mask(make_gan_data_out, rand_mask):
    # similar to write_general_in_rand_mask(data_path, rand_mask)

    train_lines = open(os.path.join(make_gan_data_out,'mathqa.txt')).readlines()
    new_mwps, ans = [], []
    unmaskables = {CLS, SEP}
    min_nb_tok_kept = 3 # Keep at least 3 tokens unmasked in each MWP
    
    cats = []
    for iline in trange(len(train_lines)):
        line,cat = train_lines[iline].strip().split('@@@')
        tokens = line.split()

        mwp_ans = []
        maskable_idx = sorted([i for i in range(len(tokens)) if tokens[i] not in unmaskables])
        for idx in sample(maskable_idx, min(rand_mask,max(len(maskable_idx)-min_nb_tok_kept,1))):
            mwp_ans.append(tokens[idx])
            tokens[idx] = '[MASK]'  
        new_mwps.append(' '.join(tokens))
        ans.append(' '.join(mwp_ans))
        cats.append(cat)
    
    print("Catetories:",set(cats))
    # {'general', 'gain', 'other', 'physics', 'probability', 'geometry'}

    lines = [f"{m}@@@{a}@@@{c}\n" for m,a,c in zip(new_mwps, ans, cats)]
    with open(os.path.join(make_gan_data_out,'mathqa_rand_mask.txt'), 'w', encoding='utf-8') as fout:
        fout.writelines(lines)

if __name__ == '__main__':
    mathqa_train = '/home/shangling/Datasets/mathqa/train.json'
    out_dir = 'data'
    rand_mask = 5

    make_gan_data(mathqa_train, out_dir, 'bert-base-uncased', True)
    random_mask(out_dir, rand_mask)