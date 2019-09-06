"""
from test_bert_model import *
testers,sents = test()
"""
import torch
from blank_filling import *
class Tester:
    def __init__(self,bert_version):
        """
        bert_version    may be a path to dir
        """
        self.tokenizer, self.model = get_bert(bert_version)
        
    def predict(self, sent):
        if not self.tokenizer or not self.model:
            return 'not self.tokenizer or not self.model'
        
        # formatting
        sent=sent.replace('_','[MASK]').replace('\n',' [SEP]')
        if not sent.startswith('[CLS] '):
            sent = '[CLS] ' + sent
        if ' ##' not in sent:
            toks = self.tokenizer.tokenize(sent)
        else:
            toks = sent.split()

        mask_ids = []
        for i, tok in enumerate(toks):
            if tok == '[MASK]':
                mask_ids.append(i)
        seg = [0] * len(toks)
        seg_tensor = torch.tensor([seg])

        toks = masked_decoding(toks, seg_tensor, mask_ids, self.model, self.tokenizer, "argmax")
        toks2 = toks.copy()
        for i,orig in enumerate(sent.split()):
            if orig == '[MASK]':
                toks2[i] = '<span style="color:blue"> '+toks2[i]+' </span>'
        pr = " ".join(toks)
        md = " ".join(toks2).replace('[CLS] ','').replace(' [SEP]','\n')
        return pr,md

models={
    'ftd':'lm_finetuning/finetuned_lm/', #'lm_finetuning/bt_nn_3k-finetuned_lm/': This one sucks. Don't use it.
    'org':'bert-base-uncased',
    'gan':'gan/models/bt_nn_300-1/tok-gen_epoch_0/'}
sents=[
    "[CLS] a car drives 60 miles on local roads at [MASK] mph , and 195 miles [MASK] the [MASK] [MASK] 65 mph , what is [MASK] average speed of the entire trip ? [SEP]",
    "[CLS] [MASK] many numbers from 45 [MASK] [MASK] [MASK] [MASK] di ##vis ##ible by 12 ? [SEP]",
    "[CLS] if y exceeds x [MASK] 25 % , [MASK] [MASK] is less [MASK] y [MASK] ? [SEP]"]
def test(modellist=models,sentlist=sents):
    testers=dict([(k,Tester(v)) for (k,v) in models.items()])
    for s in sentlist:
        print()
        for k,v in testers.items():
            print(f'\n* {k}:')
            pr,md=v.predict(s)
            print('Pr:',pr)
            print('Md:',md)
    return testers,sents

