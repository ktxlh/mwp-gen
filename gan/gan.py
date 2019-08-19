# -*- coding: utf-8 -*-

from pytorch_transformers.modeling_bert import BertForSequenceClassification, BertForPreTraining
from utils import load_data

class Instructor(Object):
    def __init__(self, args):
        # Generator, Discriminator
        self.generator = BertForPreTraining.from_pretrained(args.bert_model)
        self.generator.cuda()
        self.discriminator = BertForSequenceClassification.from_pretrained(args.bert_model, num_labels=2)
        self.discriminator.cuda()
        
        # Optimizer
        param_optimizer = list(model.named_parameters())
        no_decay = ['bias', 'gamma', 'beta']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.01},
            {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.0}
        ]
        self.optimizer = BertAdam(optimizer_grouped_parameters,lr=2e-5,warmup=.1)

        # DataLoader
        self.gen_data = load_data(args.data_path, 'G') # masked mwp
        self.dis_data = load_data(args.data_path, 'D') # full mwp


    def train(n_epochs):
        # NOTE data used for D diff from the one for G
        # NOTE bert input is a pair of sents but it should be more ones in our case
        # NOTE # epochs for finetuning bert is suggested to be 2 to 4

        train_loss_set = []
        
        # Generate
        

        # Discriminate
        
        batch = [] # suppose it's a batch of data in some epoch
        input_ids, input_mask, segment_ids, lm_label_ids, is_next = batch # is_next for next sentence prediction
        outputs = discriminator(input_ids, segment_ids, input_mask, lm_label_ids, is_next)
        loss = outputs[0]

        # Train

