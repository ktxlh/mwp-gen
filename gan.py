from pytorch_transformers.modeling_bert import BertForPreTraining

def train(bert_model):
    # Train discriminator
    # Modify funetune_on_pregenerated.py rather than generate.py
    discriminator = BertForPreTraining.from_pretrained(bert_model)
    # NOTE data used from D diff from G
    batch = [] # suppose it's a batch of data in some epoch
    input_ids, input_mask, segment_ids, lm_label_ids, is_next = batch # is_next for next sentence prediction
    # NOTE input was a pair of sents; should be more
    outputs = discriminator(input_ids, segment_ids, input_mask, lm_label_ids, is_next)
    loss = outputs[0]

    # Train generator
    # Same
    generator = BertForPreTraining.from_pretrained(bert_model)
