from torch.utils.data import  Dataset, TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences

 # TODO configure
MAX_LEN = 256
batch_size = 32

def load_data(data_path, role):
    """
    Load general_in into dataloader
    * No real/fake labels here
    * GAN -> no validation set
    Parameters:
        data_path   path to general_in.txt (supposed to be bert-tokenized in make_bert_data
    """
    assert role in {'G','D'}

    mwps = []
    with open(os.path.join(data_path,'general_in.txt', encoding='utf-8')) as f:
        if role == 'G':
            q_as = [line.strip().split('$$$') for line in f.readlines()]
            for (question, answer) in q_as:
                answer = answer.split()
                mwps.append(' '.join([(answer.pop(0) if w=='[MASK]' else w) \
                    for wid,w in enumerate(question.split())]))
        elif role == 'D':
            mwps = [line.strip().split('$$$')[0] for line in f.readlines()]

    input_ids = pad_sequences([tokenizer.convert_tokens_to_ids(mwp) for mwp in mwps], \
        maxlen=MAX_LEN, dtype="long", truncating="post", padding="post")
    attention_masks = [[float(i>0) for i in seq] for seq in input_ids]
    
    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)

    data = TensorDataset(input_ids, attention_masks)
    dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=batch_size)
    return dataloader
    