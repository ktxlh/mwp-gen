# -*- coding: utf-8 -*-

"""
TODO:
[*] loss
[*] debug lines >> file
[*] more samples
    [*] make_data
    [*] make_bert_data
[*] fine-tuned bert
[ ] less masks
[*] autoregressive
"""

import os
from collections import defaultdict

import torch
from pytorch_pretrained_bert import BertAdam, BertTokenizer
from torch import nn
from tqdm import tqdm

from pytorch_transformers.modeling_bert import (BertForMaskedLM,
                                                BertForSequenceClassification)
from utils import load_data


class Instructor:
    def __init__(self, args):
        # TODO requires_grad = False?
        self.args = args
        self.device = torch.device("cuda:0" if args.cuda else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(args.bert_model)

        # Generator, Discriminator
        self.generator = BertForMaskedLM.from_pretrained(args.bert_model)
        self.generator.to(self.device)
        self.discriminator = BertForSequenceClassification.from_pretrained(
            args.bert_model, num_labels=2)
        self.discriminator.to(self.device)
        
        # Optimizer
        self.optimizerG = self._get_optimizer_(self.generator)
        self.optimizerD = self._get_optimizer_(self.discriminator)

        # DataLoader
        self.msk_data = load_data(args.data_path, args.maxlen, args.batch_size, self.tokenizer, 'masked')
        self.org_data = load_data(args.data_path, args.maxlen, args.batch_size, self.tokenizer, 'original')
    
    def _get_optimizer_(self, model):
        no_decay = ['bias', 'gamma', 'beta']
        param_optimizer = list(model.named_parameters())
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer \
                if not any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.01},
            {'params': [p for n, p in param_optimizer \
                if any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.0}
        ]
        # TODO config/tune lr
        return BertAdam(optimizer_grouped_parameters,lr=2e-5,warmup=.1)

    def _id2prettyStr_helper_(self, id_tensor):
        tokens = self.tokenizer.convert_ids_to_tokens(id_tensor.tolist()[0])
        return ' '.join(tokens).replace(' [PAD]','').replace('[CLS] ','')

    def _predict_l2r_(self, fake_ids, msk_input_seg, mask_id):
        # predict the [MASK]s and fill them back in from left to right
        # fake_ids: mutable
        while True:
            mask_poses = [(fid==mask_id).nonzero().tolist() for fid in fake_ids] # [[[1]], []] # first mask in each mwp
            if sum([len(pos) for pos in mask_poses]) == 0:
                break
            preds = self.generator(fake_ids, msk_input_seg)[0]  # (batch_size x max_seq_len x vocab_size,) note the comma
            for p1,p2 in enumerate(mask_poses):
                if len(p2) == 0:
                    continue
                else:
                    p2 = p2[0][0]
                fake_ids[p1,p2] = preds[p1,p2].argmax(dim=-1).clone()

    def train(self):
        # NOTE bert input is a pair of sents but it should be more ones in our case
        # NOTE # epochs for finetuning bert is suggested to be 2 to 4

        # Constants
        real_label = 0
        fake_label = 1
        mask_id = self.tokenizer.convert_tokens_to_ids(['[MASK]'])[0]

        # Store loss for plotting; fix input for debugging
        train_loss_set = defaultdict(list)
        fixed_input = None

        for i_epoch in range(self.args.epochs):
            for i, (msk_batch, org_batch) in enumerate(zip(self.msk_data, self.org_data), 0): # 0 for 0-indexed
                msk_batch = tuple(t.to(self.device) for t in msk_batch)
                org_batch = tuple(t.to(self.device) for t in org_batch)

                ###############################################################
                # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z))) #
                ###############################################################
                
                #====== Train with real ======
                self.generator.eval()
                self.discriminator.train()
                
                org_input_ids, org_input_mask = org_batch
                labels = torch.full((self.args.batch_size,), real_label, device=self.device).long()
                lossD_real,_ = self.discriminator(org_input_ids, token_type_ids=None, attention_mask=org_input_mask, labels=labels) #_: logits
                lossD_real.backward()
                train_loss_set["lossD_real"].append(lossD_real.item())

                # ====== Train with fake ======
                msk_input_ids, msk_input_mask, msk_input_seg = msk_batch
                labels.fill_(fake_label)
                
                if not fixed_input:
                    fixed_input = (msk_input_ids[:1].clone(), msk_input_seg[:1].clone())
                    with open(os.path.join(self.args.result_out,'foo.txt'),'w',encoding='utf-8') as result_out_f:
                        result_out_f.writelines('IN:\t '+self._id2prettyStr_helper_(fixed_input[0])+'\n')

                # Predict [MASK]s and replace them simultaneously
                fake_ids = msk_input_ids #.clone() Soft copy to save space
                self._predict_l2r_(fake_ids, msk_input_seg, mask_id)

                lossD_fake,_ = self.discriminator(fake_ids.detach(), token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossD_fake.backward()
                train_loss_set["lossD_fake"].append(lossD_fake.item())

                self.optimizerD.step()

                ###############################################################
                # (2) Update G network: maximize log(D(G(z)))                 #
                ###############################################################
                self.generator.train()
                self.discriminator.eval()

                labels.fill_(real_label)  # fake labels are real for generator cost
                lossG,_ = self.discriminator(fake_ids, token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossG.backward()
                train_loss_set["lossG"].append(lossG.item())

                self.optimizerG.step()

                print('[%d/%d][%d/%d] LossD_real: %.4f LossD_fake: %.4f LossG: %.4f'
                    % (i_epoch, self.args.epochs, i, len(self.msk_data),
                        train_loss_set['lossD_real'][i], train_loss_set['lossD_fake'][i], train_loss_set['lossG'][i]))
                if i % 5 == 0: #100
                    self.generator.eval()

                    fixed_output = fixed_input[0].clone()                
                    self._predict_l2r_(fixed_output, fixed_input[1], mask_id)
                    with open(os.path.join(self.args.result_out,'foo.txt'),'a',encoding='utf-8') as result_out_f:
                        result_out_f.writelines(f'OUT({i_epoch},{i}):\t '+self._id2prettyStr_helper_(fixed_output)+'\n')
        
            # do checkpointing
            torch.save(self.generator.state_dict(), '%s/gen_epoch_%d.pth' % (self.args.model_out, i_epoch))
            torch.save(self.discriminator.state_dict(), '%s/dis_epoch_%d.pth' % (self.args.model_out, i_epoch))
