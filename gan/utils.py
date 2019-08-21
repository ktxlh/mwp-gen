from torch.utils.data import  Dataset, TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences

def load_data(data_path, maxlen, batch_size, tokenizer, role):
    """
    Load general_in into dataloader
    * No real/fake labels here
    * GAN -> no validation set
    Parameters:
        data_path   path to dir with general_in.txt (bert-tokenized in make_bert_data.py)
    """
    assert role in {'masked','original'}

    mwps,segs = [],[]
    with open(os.path.join(data_path,'general_in.txt', encoding='utf-8')) as f:
        if role == 'original':
            q_as = [line.strip().split('$$$') for line in f.readlines()]
            for (question, answer) in q_as:
                answer = answer.split()
                mwps.append(' '.join([(answer.pop(0) if w=='[MASK]' else w) \
                    for wid,w in enumerate(question.split())]))
        elif role == 'masked':
            mwps = [line.strip().split('$$$')[0] for line in f.readlines()]
            segs = [[0] * len(mwp.split()) for mwp in mwps]

    input_ids = pad_sequences([tokenizer.convert_tokens_to_ids(mwp.split()) for mwp in mwps], \
        maxlen=maxlen, dtype="long", truncating="post", padding="post")
    attention_masks = [[float(i>0) for i in seq] for seq in input_ids]
    
    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)
    segs = torch.tensor(segs)

    if role == 'masked':
        data = TensorDataset(input_ids, attention_masks, segs)
    elif role == 'original':
        data = TensorDataset(input_ids, attention_masks)
    dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=batch_size)
    return dataloader
    