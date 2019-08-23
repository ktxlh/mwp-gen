FROM_TAG=bt_nn_3k
CORPUS=~/Datasets/$FROM_TAG-mathqa-train-valid/tunebert.txt
DATA_PATH=~/Datasets/$FROM_TAG-mathqa-train-valid
PREGENERATE=$DATA_PATH/orig_bert_pregen
MAX_SEQLEN=256

CUDA_VISIBLE_DEVICES=3 python pregenerate_training_data.py --train_corpus $CORPUS --bert_model bert-base-uncased --do_lower_case --output_dir $PREGENERATE/ --epochs_to_generate 3 --max_seq_len $MAX_SEQLEN

CUDA_VISIBLE_DEVICES=3 python finetune_on_pregenerated.py --pregenerated_data $PREGENERATE/ --bert_model bert-base-uncased --do_lower_case --output_dir $PREGENERATE/models/ --epochs 3 --train_batch_size 32 --gradient_accumulation_steps 4 | tee output.txt

# Instructions fixing run-out-of-memory error when finetuning on single GPU
# https://github.com/huggingface/pytorch-transformers/tree/master/examples/lm_finetuning
