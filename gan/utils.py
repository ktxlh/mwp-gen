import os
import torch
from torch.utils.data import  Dataset, TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences

def load_data(general_in, maxlen, batch_size, tokenizer, role):
    """
    Load general_in into dataloader
    * No real/fake labels here
    * GAN -> no validation set
    Parameters:
        general_in   path to general_in*.txt (bert-tokenized in make_bert_data.py)
    """
    assert role in {'masked','original'}

    mwps,segs = [],[]
    with open(general_in, encoding='utf-8') as f:
        if role == 'original':
            q_as = [line.strip().split('$$$') for line in f.readlines()]
            for (question, answer) in q_as:
                answer = answer.split()
                mwps.append(' '.join([(answer.pop(0) if w=='[MASK]' else w) \
                    for wid,w in enumerate(question.split())]))
        elif role == 'masked':
            mwps = [line.strip().split('$$$')[0] for line in f.readlines()]
    assert len(mwps) > 0

    input_ids = pad_sequences([tokenizer.convert_tokens_to_ids(mwp.split()) for mwp in mwps], \
        maxlen=maxlen, dtype="long", truncating="post", padding="post")
    attention_masks = [[float(i>0) for i in seq] for seq in input_ids]
    
    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)
    segs = torch.zeros_like(input_ids) # HACK 'cuz tensor must be fix-len in each dimension

    if role == 'masked':
        data = TensorDataset(input_ids, attention_masks, segs)
    elif role == 'original':
        data = TensorDataset(input_ids, attention_masks)
    dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=batch_size)
    return dataloader
    