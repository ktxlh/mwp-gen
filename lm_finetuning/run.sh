#CORPUS=~/Datasets/all-mathqa-train-valid/tunebert.txt
DATA_PATH=~/Datasets/bt_nn_300-mathqa-train-valid/
MAX_SEQLEN=256

#CUDA_VISIBLE_DEVICES=3 python pregenerate_training_data.py --train_corpus $CORPUS --bert_model bert-base-uncased --do_lower_case --output_dir training/ --epochs_to_generate 3 --max_seq_len $MAX_SEQLEN

CUDA_VISIBLE_DEVICES=3 python finetune_on_pregenerated.py --pregenerated_data $DATA_PATH --bert_model bert-base-uncased --do_lower_case --output_dir bt_nn_300-finetuned_lm/ --epochs 3 --train_batch_size 32 --gradient_accumulation_steps 4 | tee output.txt

# Instructions fixing run-out-of-memory error when finetuning on single GPU
# https://github.com/huggingface/pytorch-transformers/tree/master/examples/lm_finetuning
