# -*- coding: utf-8 -*-
from tqdm import tqdm

import torch
from torch import nn
from pytorch_transformers.modeling_bert import (BertForMaskedLM,
                                                BertForSequenceClassification)
from pytorch_pretrained_bert import BertAdam, BertTokenizer
from utils import load_data
from collections import defaultdict

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
        # TODO configure/tune lr?
        self.optimizerG = _get_optimizer_(self.generator.named_parameters(),lr=2e-5,warmup=.1)
        self.optimizerD = _get_optimizer_(self.discriminator.named_parameters(),lr=2e-5,warmup=.1)

        # DataLoader
        self.msk_data = load_data(args.data_path, args.maxlen, args.batch_size, self.tokenizer, 'masked')
        self.org_data = load_data(args.data_path, args.maxlen, args.batch_size, self.tokenizer, 'original')
    
    def _get_optimizer_(paras, lr, warmup):
        no_decay = ['bias', 'gamma', 'beta']
        param_optimizer = list(paras)
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer \
                if not any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.01},
            {'params': [p for n, p in param_optimizer \
                if any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.0}
        ]
        return BertAdam(optimizer_grouped_parameters,lr=lr,warmup=warmup)

    def _flat_accuracy_(preds, labels):
        pred_flat = np.argmax(preds, axis=1).flatten()
        labels_flat = labels.flatten()
        return np.sum(pred_flat == labels_flat) / len(labels_flat)

    def train(self):
        # NOTE bert input is a pair of sents but it should be more ones in our case
        # NOTE # epochs for finetuning bert is suggested to be 2 to 4

        # Constants
        real_label = 0
        fake_label = 1
        mask_id = self.tokenizer.convert_tokens_to_ids(['[MASK]'])[0]

        # Store loss for plotting
        train_loss_set = defaultdict(list)

        for i_epoch in range(self.args.epochs):
            for i, (msk_batch, org_batch) in tqdm(enumerate(zip(self.msk_data, self.org_data), 0)): # 0 for 0-indexed
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
                lossD_real,_ = self.discriminator(org_input_ids, token_type_ids=None, attention_mask=org_input_mask, labels=labels)
                lossD_real.backward()
                train_loss_set["lossD_real"].append(lossD_real.item())

                # ====== Train with fake ======
                msk_input_ids, msk_input_mask, msk_input_seg = msk_batch
                labels.fill_(fake_label)
                
                # Predict [MASK]s and replace them simultaneously # TODO autoregressively
                fake_ids = msk_input_ids #.clone() Soft copy to save space
                preds,_ = self.generator(fake_ids, msk_input_seg)     # batch_size x max_seq_len x vocab_size
                preds = torch.tensor(preds)
                fake_ids[msk_input_ids==mask_id] = preds[msk_input_ids==mask_id].argmax(dim=-1).clone()
                
                lossD_fake = self.discriminator(fake_ids.detach(), token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossD_fake.backward()
                train_loss_set["lossD_fake"].append(lossD_fake.item())

                self.optimizerD.step()

                ###############################################################
                # (2) Update G network: maximize log(D(G(z)))                 #
                ###############################################################
                self.generator.train()
                self.discriminator.eval()

                label.fill_(real_label)  # fake labels are real for generator cost
                lossG = self.discriminator(fake_ids, token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossG.backward()
                train_loss_set["lossG"].append(lossG.item())

                optimizerG.step()

                print('[%d/%d][%d/%d] LossD_real: %.4f LossD_fake: %.4f LossG: %.4f'
                    % (i_epoch, self.args.epochs, i, len(self.msk_data),
                        train_loss_set['lossD_real'], train_loss_set['lossD_fake'], train_loss_set['lossG']))
                if i % 100 == 0:
                    tokens = tokenizer.convert_ids_to_tokens(fake_ids.detach())
                    print(' '.join(tokens))
        
        # do checkpointing
        torch.save(self.generator.state_dict(), '%s/gen_epoch_%d.pth' % (self.args.model_out, epoch))
        torch.save(self.discriminator.state_dict(), '%s/dis_epoch_%d.pth' % (self.args.model_out, epoch))
