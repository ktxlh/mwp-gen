THRESH=9
N_TEMPLATES=100
EMB_SIZE=300
HID_SIZE=$EMB_SIZE
LAYERS=1
DROPOUT=0.3
K=55
KMUL=5
L=4
LR=0.5
SEED=1111

SEP_ATTN=   #-sep_attn  # Is $SEP_ATTN about [Constraint Learning]?

#DATA_DIR=~/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated
#GEN_FROM=~/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/src_valid.txt
DATA_DIR=data/labee2e
GEN_FROM=data/labee2e/src_uniq_valid.txt

TAG=e2e-$EMB_SIZE-$K-$KMUL-far

# Dynamically generate meaningful filename str
MODEL=models/chsmm-$TAG.pt
TAGGED_FI=segs/seg-$TAG.txt
GEN_FI=gens/gen-$TAG.md

# Training  +Autoregressive
CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen 55 -lr $LR $SEP_ATTN -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -seed $SEED -save $MODEL -ar_after_decay -verbose

#KMUL=1
MODEL=$MODEL.0
> "command_tips.sh"

# Viterbi Segmentation/Template Extraction  +Autoregressive
echo "echo '# Viterbi Segmentation/Template Extraction'" >> "command_tips.sh"
echo "scp shangling@140.109.19.51:~/ntg2/$TAGGED_FI ~/mwp/ntg2/segs" >> "command_tips.sh"
#CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen 55 -lr $LR  $SEP_ATTN -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -load $MODEL -label_train -ar_after_decay -verbose | tee $TAGGED_FI


ANS=analyses/a-seg-$TAG.md
#CUDA_VISIBLE_DEVICES=3 python my_utils.py -a_seg -data $DATA_DIR -tagged_fi $TAGGED_FI -gen_fi $GEN_FI > $ANS
echo "scp shangling@140.109.19.51:~/ntg2/$ANS ~/mwp/ntg2/analyses" >> "command_tips.sh"
echo "open ~/mwp/ntg2/$ANS" >> "command_tips.sh"


#GEN_FROM='toy_valid.txt'


# Generation
echo "echo '# Generation'" >> "command_tips.sh"
echo "scp shangling@140.109.19.51:~/ntg2/$GEN_FI ~/mwp/ntg2/gens" >> "command_tips.sh"

echo "open ~/mwp/ntg2/$TAGGED_FI" >> "command_tips.sh"
echo "open ~/mwp/ntg2/$GEN_FI" >> "command_tips.sh"

#CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -dropout $DROPOUT -K $K -L $L -log_interval 100 -thresh $THRESH -lr $LR $SEP_ATTN -unif_lenps -emb_drop -mlpinp -onmt_decay -one_rnn -max_pool -gen_from_fi $GEN_FROM -load $MODEL -tagged_fi $TAGGED_FI -beamsz 5 -ntemplates $N_TEMPLATES -gen_wts '1,1' -cuda -min_gen_tokes 0 -verbose > $GEN_FI

ANG=analyses/a-gen-$TAG.md
#CUDA_VISIBLE_DEVICES=3 python my_utils.py -a_gen -data $DATA_DIR -tagged_fi $TAGGED_FI -gen_fi $GEN_FI > $ANG
echo "scp shangling@140.109.19.51:~/ntg2/$ANG ~/mwp/ntg2/analyses" >> "command_tips.sh"
echo "open ~/mwp/ntg2/$ANG" >> "command_tips.sh"
