# 講HSMM生成字的細節(pipeline?)
# 更系統化地做實驗
# output .md directly
# .sh
# tune hyper-parameters
# github repo for code review
# keep the line no; program a separate "line no -> equation / problem type" for showing results automatically
# Data-parameter ratio: 600*7/(55*5)?
# Refine the experiment process

THRESH=3
N_TEMPLATES=100
EMB_SIZE=100
HID_SIZE=$EMB_SIZE
LAYERS=1
DROPOUT=0.3
K=55
KMUL=5
L=4
LR=0.5

DATA_DIR=~/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/
GEN_FROM=~/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/src_valid.txt

TAG=ai2-cmds-$EMB_SIZE–$K-$KMUL-far-NER

# Dynamically generate meaningful filename str
MODEL=models/chsmm-$TAG.pt
TAGGED_FI=segs/seg-$TAG.txt
GEN_FI=gens/gen-$TAG.md

# Training
## +Autoregressive
#CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen 55 -lr $LR -sep_attn -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -seed 1111 -save $MODEL -ar_after_decay -verbose

MODEL="$MODEL.0"
KMUL=1
> "command_tips.sh"

# Viterbi Segmentation/Template Extraction
## +Autoregressive
echo "echo '# Viterbi Segmentation/Template Extraction'" >> "command_tips.sh"
echo "scp shangling@140.109.19.51:~/ntg2/$TAGGED_FI ~/mwp/ntg2/segs" >> "command_tips.sh"
echo "open ~/mwp/ntg2/$TAGGED_FI" >> "command_tips.sh"
#CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen 55 -lr $LR  -sep_attn -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -load $MODEL -label_train -ar_after_decay -verbose | tee $TAGGED_FI

# Generation
# 10 templates
echo "echo '# Generation'" >> "command_tips.sh"
echo "scp shangling@140.109.19.51:~/ntg2/$GEN_FI ~/mwp/ntg2/gens" >> "command_tips.sh"
echo "open ~/mwp/ntg2/$GEN_FI" >> "command_tips.sh"
CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -dropout $DROPOUT -K $K -L $L -log_interval 100 -thresh $THRESH -lr $LR -sep_attn -unif_lenps -emb_drop -mlpinp -onmt_decay -one_rnn -max_pool -gen_from_fi $GEN_FROM -load $MODEL -tagged_fi $TAGGED_FI -beamsz 5 -ntemplates $N_TEMPLATES -gen_wts '1,1' -cuda -min_gen_tokes 0 -verbose > $GEN_FI
