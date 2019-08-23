FROM_TAG=bt_nn_3k
BERT_MODEL=~/ntg2/lm_finetuning/$FROM_TAG-finetuned_lm/ #bert-base-uncased
GENERAL_IN=~/Datasets/$FROM_TAG-mathqa-train-valid/general_in_rand_mask.txt
MAXLEN=256
BATCH_SIZE=16
EPOCHS=10
MODEL_OUT=models
RESULT_OUT=results
CUDA=-cuda

CUDA_VISIBLE_DEVICES=3 python main.py -bert_model $BERT_MODEL -general_in $GENERAL_IN -maxlen $MAXLEN -batch_size $BATCH_SIZE -epochs $EPOCHS -model_out $MODEL_OUT -result_out $RESULT_OUT $CUDA
