BERT_MODEL=bert-base-uncased
DATA_PATH=~/Datasets/bt_nn-mathqa-train-valid
MAXLEN=256
BATCH_SIZE=4
EPOCHS=3
MODEL_OUT=models
CUDA=-cuda

CUDA_VISIBLE_DEVICES=3 python main.py -bert_model $BERT_MODEL -data_path $DATA_PATH -maxlen $MAXLEN -batch_size $BATCH_SIZE -epochs $EPOCHS -model_out $MODEL_OUT $CUDA
