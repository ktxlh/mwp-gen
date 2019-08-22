BERT_MODEL=~/ntg2/lm_finetuning/bt_nn_300-finetuned_lm/ #bert-base-uncased
DATA_PATH=~/Datasets/bt_nn_300-mathqa-train-valid
MAXLEN=256
BATCH_SIZE=8
EPOCHS=3
MODEL_OUT=models
RESULT_OUT=results
CUDA=-cuda

CUDA_VISIBLE_DEVICES=3 python main.py -bert_model $BERT_MODEL -data_path $DATA_PATH -maxlen $MAXLEN -batch_size $BATCH_SIZE -epochs $EPOCHS -model_out $MODEL_OUT -result_out $RESULT_OUT $CUDA
