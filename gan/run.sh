FROM_TAG=bt_nn_3k
BERT_MODEL=~/ntg2/lm_finetuning/$FROM_TAG-finetuned_lm/ #bert-base-uncased
GENERAL_IN=~/Datasets/$FROM_TAG-mathqa-train-valid/general_in_rand_mask.txt
MAXLEN=256
BATCH_SIZE=8 # if 16, RuntimeError: CUDA out of memory.
LR=1e-5 #2e-5
WARMUP=.1
EPOCHS=10
MODEL_OUT=models
RESULT_OUT=results
CUDA=-cuda

CUDA_VISIBLE_DEVICES=3 python main.py -bert_model $BERT_MODEL -general_in $GENERAL_IN -maxlen $MAXLEN -batch_size $BATCH_SIZE -epochs $EPOCHS -lr $LR -warmup $WARMUP -model_out $MODEL_OUT -result_out $RESULT_OUT $CUDA
