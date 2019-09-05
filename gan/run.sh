########### IN ###########
FROM_TAG=bt_nn_300
DATA_PATH=~/Datasets/$FROM_TAG-mathqa-train-valid

GENERAL_IN=$DATA_PATH/general_in_rand_mask.txt
#$DATA_PATH/general_in_lcs.txt

BERT_MODEL=~/ntg2/lm_finetuning/$FROM_TAG-finetuned_lm/ 
#~/ntg2/lm_finetuning/$FROM_TAG-finetuned_lm/ 
#bert-base-uncased
#$DATA_PATH/rand_mask_bert_pregen/models/
#$DATA_PATH/lcs_bert_pregen/models/
#$DATA_PATH/orig_bert_pregen/models/ 

########### TRAIN ###########
MAXLEN=256
BATCH_SIZE=8 # if 16, RuntimeError: CUDA out of memory.
LR=1e-3 #2e-5 ##########################################
############################ How to tune it? Diff for G/D?
WARMUP=.1
EPOCHS=2
CUDA=-cuda

########### OUT ###########
MODEL_OUT=models
RESULT_OUT=results/$FROM_TAG # NOTE: no file extension
LOSS_DIR=results/$FROM_TAG/

########### TEST ###########
TEST= #-test
LOAD= #-load=$MODEL_OUT

########### COMMAND ###########
CUDA_VISIBLE_DEVICES=3 python main.py -bert_model $BERT_MODEL -general_in $GENERAL_IN -maxlen $MAXLEN -batch_size $BATCH_SIZE -epochs $EPOCHS -lr $LR -warmup $WARMUP -model_out $MODEL_OUT -result_out $RESULT_OUT -loss_dir $LOSS_DIR $LOAD $TEST $CUDA
