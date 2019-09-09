# -*- coding: utf-8 -*-
"""
BERT-GAN.
Code references:
* Pytorch DCGAN example:  https://github.com/pytorch/examples/blob/master/dcgan/main.py
* BERT fine-tuning tutorial:    https://mccormickml.com/2019/07/22/BERT-fine-tuning/
"""
import os
from collections import defaultdict

import torch
from pytorch_pretrained_bert import BertAdam
from torch import nn
from tqdm import tqdm

from pytorch_transformers.modeling_bert import (BertForMaskedLM,
                                                BertForSequenceClassification)
from pytorch_transformers.tokenization_bert import BertTokenizer
from utils import (fixed_append_pred, fixed_write_orig, load_data, get_gan_path,
                   plot, predict_l2r, save_gan, test_write_mwps)


class Instructor:
    def __init__(self, args):
        torch.manual_seed(args.seed)
        self.args = args

        # Tokenizer, Generator, Discriminator
        if args.load_epoch > -1: # NOTE: 0-indexed. Load from trained
            gen_path, dis_path = get_gan_path(self.args.model_out, self.args.load_epoch)
        else:
            gen_path, dis_path = args.bert_model, args.bert_model
        self.tokenizer = BertTokenizer.from_pretrained(gen_path) # TODO requires_grad = False?
        self.generator = BertForMaskedLM.from_pretrained(gen_path)
        self.discriminator = BertForSequenceClassification.from_pretrained(dis_path, num_labels=self.args.num_labels)

        # Optimizer
        self.optimizerG = self._get_optimizer_(self.generator)
        self.optimizerD = self._get_optimizer_(self.discriminator)

        # DataLoader
        self.msk_data = load_data(args.data_in, args.maxlen, args.batch_size, self.tokenizer, args.seed, 'masked')
        self.org_data = load_data(args.data_in, args.maxlen, args.batch_size, self.tokenizer, args.seed, 'original')

        self.mask_id = self.tokenizer.convert_tokens_to_ids(['[MASK]'])[0]
        self.device = torch.device("cuda:0" if args.cuda else "cpu")
        self.generator.to(self.device)
        self.discriminator.to(self.device)
    
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
        # TODO allow diff lr for G & D
        return BertAdam(optimizer_grouped_parameters,lr=self.args.lr,warmup=self.args.warmup)

    def train(self):
        # NOTE bert input was a pair of sents but the number may differ here
        # NOTE # epochs for finetuning bert is suggested to be 2 to 4

        # Constants
        real_label = 1 #0
        fake_label = 0 #1
        
        # Store loss for plotting; fix input for debugging
        train_loss_set = defaultdict(list)
        fixed_input = None

        if not os.path.exists(self.args.model_out):
            os.makedirs(self.args.model_out)

        for i_epoch in range(self.args.load_epoch+1, self.args.epochs):
            for i, (msk_batch, org_batch) in enumerate(zip(self.msk_data, self.org_data), 0): # 0 for 0-indexed
                msk_batch = tuple(t.to(self.device) for t in msk_batch)
                org_batch = tuple(t.to(self.device) for t in org_batch)

                ###############################################################
                # Update Discriminator: maximize log(D(x)) + log(1 - D(G(z))) #
                ###############################################################
                
                #====== Train with real ======
                self.generator.eval()
                self.discriminator.train()
                
                org_input_ids, org_input_mask, org_input_cat = org_batch
                #labels = torch.full((self.args.batch_size,), real_label, device=self.device).long()
                labels = org_input_cat
                lossD_real,_ = self.discriminator(org_input_ids, token_type_ids=None, attention_mask=org_input_mask, labels=labels) #_: logits
                lossD_real.backward()
                train_loss_set["lossD_real"].append(lossD_real.item())

                # ====== Train with fake ======
                msk_input_ids, msk_input_mask, msk_input_cat, msk_input_seg = msk_batch
                labels.fill_(fake_label)
                
                if not fixed_input:
                    fixed_input = (msk_input_ids[:1].clone(), msk_input_seg[:1].clone())
                    fixed_write_orig(self.tokenizer, self.args.result_out, fixed_input[0])
                    
                # Predict [MASK]s and replace them autoregressively
                fake_ids = predict_l2r(self.generator, msk_input_ids, msk_input_seg, self.mask_id)

                lossD_fake,_ = self.discriminator(fake_ids.detach(), token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossD_fake.backward()
                train_loss_set["lossD_fake"].append(lossD_fake.item())

                self.optimizerD.step()

                ###############################################################
                # Update Generator: maximize log(D(G(z)))                     #
                ###############################################################
                self.generator.train()
                self.discriminator.eval()

                #labels.fill_(real_label)  # fake labels are real for generator cost (???)
                labels = msk_input_cat
                lossG,_ = self.discriminator(fake_ids, token_type_ids=None, attention_mask=msk_input_mask, labels=labels)
                lossG.backward()
                train_loss_set["lossG"].append(lossG.item())

                self.optimizerG.step()

                print('[%d/%d][%d/%d] LossD_real: %.4f LossD_fake: %.4f LossG: %.4f'
                    % (i_epoch, self.args.epochs, i, len(self.msk_data),
                        train_loss_set['lossD_real'][i], train_loss_set['lossD_fake'][i], train_loss_set['lossG'][i]))
                if i % 100 == 0:
                    with torch.no_grad():
                        fixed_output = predict_l2r(self.generator, fixed_input[0], fixed_input[1], self.mask_id)
                        fixed_append_pred(self.tokenizer, self.args.result_out, fixed_input[0], fixed_output, i_epoch, i)
        
            # do checkpointing
            save_gan(self.tokenizer, self.generator, self.discriminator, self.args.model_out, i_epoch)
        
        # plot loss
        plot(train_loss_set, self.args.loss_dir)

    def test(self):
        with torch.no_grad():
            # load only the first training batch # TODO use validation data
            msk_input_ids, _, msk_input_seg = tuple(t.to(self.device) for t in next(iter(self.msk_data)))
            fixed_inputs = (msk_input_ids.clone(), msk_input_seg.clone())

            fixed_outputs = predict_l2r(self.generator, fixed_inputs[0], fixed_inputs[1], self.mask_id)
            test_write_mwps(self.args, self.tokenizer, self.args.result_out, fixed_inputs[0], fixed_outputs)
