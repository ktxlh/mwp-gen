# -*- coding: utf-8 -*-
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

    def _flat_accuracy_(self, preds, labels):
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

        # Store loss for plotting; fix input for debugging
        train_loss_set = defaultdict(list)
        fixed_input = None

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
                
                fixed_input = (msk_input_ids[:1].clone(), msk_input_seg[:1].clone()) if not fixed_input else fixed_input

                # Predict [MASK]s and replace them simultaneously # TODO autoregressively
                fake_ids = msk_input_ids #.clone() Soft copy to save space
                preds = self.generator(fake_ids, msk_input_seg)[0]  # (batch_size x max_seq_len x vocab_size,) note the comma
                fake_ids[msk_input_ids==mask_id] = preds[msk_input_ids==mask_id].argmax(dim=-1).clone()

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
                if i % 100 == 0:
                    self.generator.eval()
                    fix_ids = fixed_input[0].clone()
                    preds_idx = self.generator(*fixed_input)[0]
                    fix_ids[fix_ids==mask_id] = preds_idx[fix_ids==mask_id].argmax(dim=-1)
                    tokens = self.tokenizer.convert_ids_to_tokens(fix_ids.tolist()[0])
                    print('[Sample]',' '.join(tokens).replace(' [PAD]',''))
        
            # do checkpointing
            torch.save(self.generator.state_dict(), '%s/gen_epoch_%d.pth' % (self.args.model_out, i_epoch))
            torch.save(self.discriminator.state_dict(), '%s/dis_epoch_%d.pth' % (self.args.model_out, i_epoch))
