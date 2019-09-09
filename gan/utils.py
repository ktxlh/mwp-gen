import os
import pprint
import time
import numpy as np
import matplotlib.pyplot as plt
import torch
from keras.preprocessing.sequence import pad_sequences
from torch.utils.data import (DataLoader, Dataset, RandomSampler,
                              SequentialSampler, TensorDataset)

pp = pprint.PrettyPrinter(indent=4)

def load_data(mathqa_rand_mask, maxlen, batch_size, tokenizer, seed, role):
    """
    Load input data into dataloader
    * No real/fake labels here
    * GAN -> no validation set
    Parameters:
        mathqa_rand_mask   path to mathqa_rand_mask.txt (from random_mask in make_gan_data.py)
    """
    torch.manual_seed(seed)
    mask_id = tokenizer.convert_tokens_to_ids(['[MASK]'])[0]
    assert role in {'masked','original'}

    categories = ['fake', 'gain', 'general', 'geometry', 'physics', 'probability', 'other']
    cat2id = dict([(c,i) for (i,c) in enumerate(categories)])

    mwps, cats = [],[]
    with open(mathqa_rand_mask, encoding='utf-8') as f:
        lines = [line.strip().split('@@@') for line in f.readlines()]
        for (question, answer, category) in lines:
            try:
                cats.append(cat2id[category])
            except Exception as e:
                print("Exception",e)
                print("question ",question)
                print("answer   ",answer)
                print("category ",category)
                continue
            if role == 'original':
                answer = answer.split()
                mwps.append(' '.join([(answer.pop(0) if w=='[MASK]' else w) \
                    for wid,w in enumerate(question.split())]))
            elif role == 'masked':
                mwps.append(question)
    assert len(mwps) > 0

    input_ids = pad_sequences([tokenizer.convert_tokens_to_ids(mwp[0].split()) for mwp in mwps], \
        maxlen=maxlen, dtype="long", truncating="post", padding="post")
    attention_masks = [[float(i>0 and i!=mask_id) for i in seq] for seq in input_ids]
    
    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)
    segs = torch.zeros_like(input_ids) # HACK 'cuz tensor must be fix-len in each dimension
    cats = torch.tensor(cats)

    if role == 'masked':
        data = TensorDataset(input_ids, attention_masks, cats, segs)
    elif role == 'original':
        data = TensorDataset(input_ids, attention_masks, cats)
    dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=batch_size)
    return dataloader


def test_write_mwps(args, tokenizer, result_out, orig_tensors, pred_tensors):
    print("Files written:",result_out+'_test.txt', result_out+'_test.md')
    with open(result_out+'_test.txt','w',encoding='utf-8') as fi:
        fi.writelines(str(args)+'\n')
        for orig_tensor, pred_tensor in zip(orig_tensors, pred_tensors):
            fi.writelines('IN:\t'+_id2prettyStr(tokenizer, orig_tensor)+'\n')
            fi.writelines(f'OUT:\t '+_id2prettyStr(tokenizer, pred_tensor)+'\n')
    with open(result_out+'_test.md','w',encoding='utf-8') as fi:
        fi.writelines(str(args)+'\n')
        for orig_tensor, pred_tensor in zip(orig_tensors, pred_tensors):
            fi.writelines('IN:\n'+_id2prettyStr(tokenizer, orig_tensor).replace('[MASK]','_').replace(' [SEP]','\n')+'\n')
            fi.writelines(f'OUT:\n'+_id2prettyStr_styled(tokenizer, orig_tensor, pred_tensor).replace(' [SEP]','\n')+'\n')

def fixed_write_orig(tokenizer, result_out, orig_tensor):
    print("Files written:",result_out+'.txt', result_out+'.md')
    with open(result_out+'.txt','w',encoding='utf-8') as fi:
        fi.writelines('IN:\t '+_id2prettyStr(tokenizer, orig_tensor)+'\n')
    with open(result_out+'.md','w',encoding='utf-8') as fi:
        fi.writelines('IN:\n'+_id2prettyStr(tokenizer, orig_tensor).replace('[MASK]','_').replace(' [SEP]','\n')+'\n')

def fixed_append_pred(tokenizer, result_out, orig_tensor, pred_tensor, i_epoch, i):
    with open(result_out+'.txt','a',encoding='utf-8') as fi:
        fi.writelines(f'OUT({i_epoch},{i}):\t '+_id2prettyStr(tokenizer, pred_tensor)+'\n')
    with open(result_out+'.md','a',encoding='utf-8') as fi:
        fi.writelines(f'OUT({i_epoch},{i}):\n'+_id2prettyStr_styled(tokenizer, orig_tensor, pred_tensor).replace(' [SEP]','\n')+'\n')

def _id2prettyStr(tokenizer, id_tensor):
    # from words' id_tensor to a string for printing
    tokens = tokenizer.convert_ids_to_tokens(id_tensor.squeeze().tolist())
    return ' '.join(tokens).replace(' [PAD]','').replace('[CLS] ','')

def _id2prettyStr_styled(tokenizer, orig_tensor, pred_tensor):
    # from words' id_tensor to a string for md making (blue predicted tokens)
    origs = tokenizer.convert_ids_to_tokens(orig_tensor.squeeze().tolist())
    preds = tokenizer.convert_ids_to_tokens(pred_tensor.squeeze().tolist())
    assert len(origs) == len(preds)
    for i,orig in enumerate(origs):
        if orig == '[MASK]':
            preds[i] = '<span style="color:blue"> '+preds[i]+' </span>'
    return ' '.join(preds).replace(' [PAD]','').replace('[CLS] ','')

def predict_l2r(generator, msk_input_ids, msk_input_seg, mask_id):
    # replace [MASK]s with predictions from left to right
    fake_ids = msk_input_ids.clone()
    while True:
        mask_poses = [(fid==mask_id).nonzero().tolist() for fid in fake_ids] # [[[1]], []] # first mask in each mwp
        if sum([len(pos) for pos in mask_poses]) == 0:
            break
        preds = generator(fake_ids, msk_input_seg)[0]  # (batch_size x max_seq_len x vocab_size,) note the comma
        for p1,p2 in enumerate(mask_poses):
            if len(p2) == 0:
                continue
            else:
                p2 = p2[0][0]
            fake_ids[p1,p2] = preds[p1,p2].argmax(dim=-1)
    return fake_ids

"""
# TODO 5~10 should be named 5~10 rather than 10
loss_paths = ['results/bt_nn_3k-5','results/bt_nn_3k-10']
new_dir = 'results/bt_nn_3k-5-10'
losses = plot_combined_losses(loss_paths,new_dir)
"""
def plot_combined_losses(loss_paths,new_dir):
    from collections import defaultdict
    losses = defaultdict(list)
    for path in loss_paths:
        loss_dict = eval(open(os.path.join(path,'loss_.txt')).read())
        for k,v in loss_dict.items():
            losses[k].extend(v)
    plot(losses,new_dir)
    return losses

def plot(losses, loss_dir):
    try:
        if not os.path.exists(loss_dir):
            os.makedirs(loss_dir)

        print(f"Plotting loss to {loss_dir}...")
        fname_time = '' #time.time()
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        xlabel = 'batches' #'iteration times'
        ylabel = 'loss'

        losses['iteration'] = [i for i in range(len(list(losses.values())[0]))]
        open(os.path.join(loss_dir,f'loss_{fname_time}.txt'),'w').writelines(pp.pformat(dict(losses))+'\n')

        plt.title('Result Analysis: Real/Fake')
        plt.plot('iteration','lossD_real',color=colors[0],data=losses)
        plt.plot('iteration','lossD_fake',color=colors[1],data=losses)
        plt.plot('iteration','lossG',color=colors[2],data=losses)
        plt.legend(['lossD_real','lossD_fake','lossG'])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f"{loss_dir}/lossSrc_{fname_time}.png")
        plt.clf()

        plt.title('Result Analysis: Generator')
        plt.plot('iteration','lossG',color=colors[2],data=losses)
        plt.legend(['lossG'])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f"{loss_dir}/lossG_{fname_time}.png")
        plt.clf()

        plt.title('Result Analysis: Discriminator')
        plt.plot('iteration','lossD_real',color=colors[0],data=losses)
        plt.plot('iteration','lossD_fake',color=colors[1],data=losses)
        plt.legend(['lossD_real','lossD_fake'])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f"{loss_dir}/lossD_{fname_time}.png")
        plt.clf()

        print(f"Loss plots saved to {loss_dir}")

    except Exception as e:
        print(str(e))

def get_gan_path(model_out, i_epoch):
    gen_save_dir = '%stok-gen_epoch_%d/' % (model_out, i_epoch)
    dis_save_dir = '%sdis_epoch_%d/' % (model_out, i_epoch)
    return gen_save_dir, dis_save_dir

def save_gan(tok,gen,dis,model_out,i_epoch):
    gen_save_dir, dis_save_dir = get_gan_path(model_out, i_epoch)
    for save_dir in [gen_save_dir,dis_save_dir]:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    tok.save_pretrained(gen_save_dir)
    gen.save_pretrained(gen_save_dir)
    dis.save_pretrained(dis_save_dir)
    print(f"GAN models saved to {gen_save_dir} and {dis_save_dir}")
