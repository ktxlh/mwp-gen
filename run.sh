#Can't use whole-word-masking bert for now for no reason @@
THRESH=3    # Tune this according to the dataset!
N_TEMPLATES=100
EMB_SIZE=300
HID_SIZE=$EMB_SIZE
LAYERS=1
DROPOUT=0   # Why do we need dropout at generation time @@
K=45
KMUL=3
L=4
LR=0.5
SEED=1111
MAX_SEQLEN=256
SEP_ATTN=-sep_attn
WORD_AR= #-word_ar    # QwQ   # 33404 pars using word_ar OAO
PURE=   #-pure   # TODO
CPFRCED= #-copy_forced

DATA_DIR=~/Datasets/bt_nn_300-mathqa-train-valid
GEN_FROM=$DATA_DIR/src_valid.txt
CMDS=command_tips.sh

BERT_VERSION=lm_finetuning/finetuned_lm/ #bert-large-uncased #-whole-word-masking 
# bert-(base|large)-(un)?cased(-whole-word-masking(-finetuned-squad)?)? # only some of them have shortcuts s.t. we can use it by simply specify the name
WRITE_BERT_IN=-write_bert_in
WORD_LEVEL= #-word_level
N_CLSTR=1000 # number of clusters
N_GIBBS=1   # number of iteration (prediction; Gibbs sampling)

format () {
    if [ ${#CPFRCED} -gt 0 ]; then   # greater than
        CP_TAG=-cp
    else
        CP_TAG=
    fi
    if [ "$WORD_AR" = "-word_ar" ]; then   # greater than
        AR_TAG=-war
    else
        AR_TAG=-far
    fi
    #########################################################
    TAG=bt_nn_300-mathqa-$EMB_SIZE-$K-$KMUL$AR_TAG$CP_TAG$WORD_LEVEL
    EXTRA=-$N_CLSTR-finetuned_bert-3 #3epochs
    #########################################################

    # Generate meaningful filename str
    MODEL=models/chsmm-$TAG.pt
    TAGGED_FI=segs/seg-$TAG.txt
    GEN_FI=gens/gen-$TAG$EXTRA.md
    ANS=analyses/a-seg-$TAG$EXTRA.md
    ANG=analyses/a-gen-$TAG$EXTRA.md

    BERT_IN=bertio/bert_$TAG$EXTRA.in
    BERT_OUT=bertio/bert_$TAG$EXTRA-$N_GIBBS.out
}

# Training  +Autoregressive
train () {
    start=$SECONDS
    CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen $MAX_SEQLEN -lr $LR $SEP_ATTN -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -seed $SEED -save $MODEL -ar_after_decay -verbose $CPFRCED $WORD_AR
    echo $(( SECONDS - start ))
}

# Viterbi Segmentation/Template Extraction  +Autoregressive
segment () {
    start=$SECONDS
    echo "echo '# Viterbi Segmentation/Template Extraction'" >> $CMDS
    echo "scp shangling@140.109.19.51:~/ntg2/$TAGGED_FI ~/mwp/ntg2/segs" >> $CMDS
    CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -K $K -L $L -log_interval 200 -thresh $THRESH -emb_drop -bsz 15 -max_seqlen $MAX_SEQLEN -lr $LR  $SEP_ATTN -max_pool -unif_lenps -one_rnn -Kmul $KMUL -mlpinp -onmt_decay -cuda -load $MODEL -label_train -ar_after_decay -verbose $CPFRCED $WORD_AR > $TAGGED_FI #| tee $TAGGED_FI
    echo $(( SECONDS - start ))
}
analyze_seg () {
    start=$SECONDS
    CUDA_VISIBLE_DEVICES=3 python my_utils.py -a_seg -data $DATA_DIR -tagged_fi $TAGGED_FI $PURE > $ANS
    echo "echo '# Segmentation Analysis'" >> $CMDS
    echo "scp shangling@140.109.19.51:~/ntg2/$ANS ~/mwp/ntg2/analyses" >> $CMDS
    echo "open ~/mwp/ntg2/$ANS" >> $CMDS
    echo $(( SECONDS - start ))
}

# Generate with neural templates
generate () {
    start=$SECONDS
    echo "echo '# Generation'" >> $CMDS
    echo "scp shangling@140.109.19.51:~/ntg2/$GEN_FI ~/mwp/ntg2/gens" >> $CMDS
    #echo "open ~/mwp/ntg2/$TAGGED_FI" >> $CMDS
    echo "open ~/mwp/ntg2/$GEN_FI" >> $CMDS
    
    #GEN_FROM='toy_valid.txt'
    CUDA_VISIBLE_DEVICES=3 python chsmm.py -data $DATA_DIR -emb_size $EMB_SIZE -hid_size $HID_SIZE -layers $LAYERS -dropout $DROPOUT -K $K -L $L -log_interval 100 -thresh $THRESH -lr $LR $SEP_ATTN -unif_lenps -emb_drop -mlpinp -onmt_decay -one_rnn -max_pool -gen_from_fi $GEN_FROM -load $MODEL -tagged_fi $TAGGED_FI -beamsz 5 -ntemplates $N_TEMPLATES -gen_wts '1,1' -cuda -min_gen_tokes 0 -verbose $CPFRCED $WORD_AR > $GEN_FI
    echo $(( SECONDS - start ))
}
analyze_gen () {
    start=$SECONDS
    CUDA_VISIBLE_DEVICES=3 python my_utils.py -a_gen -data $DATA_DIR -tagged_fi $TAGGED_FI -gen_fi $GEN_FI > $ANG
    echo "scp shangling@140.109.19.51:~/ntg2/$ANG ~/mwp/ntg2/analyses" >> $CMDS
    echo "open ~/mwp/ntg2/$ANG" >> $CMDS
    echo $(( SECONDS - start ))
}

# Generate with BERT
blank_filling() {
    start=$SECONDS
    echo "echo '# Blank filling'" >> $CMDS
    echo "scp shangling@140.109.19.51:~/ntg2/{$BERT_IN,$BERT_OUT} ~/mwp/ntg2/bertio" >> $CMDS
    CUDA_VISIBLE_DEVICES=3 python blank_filling.py -seg_path $TAGGED_FI -data_path $DATA_DIR -bert_in $BERT_IN -bert_out $BERT_OUT -bert_version $BERT_VERSION -n_clusters $N_CLSTR -gibbs $N_GIBBS $WORD_LEVEL $WRITE_BERT_IN
    echo $(( SECONDS - start ))
}
> $CMDS

make_bert_data(){
    # HAAAAAAAAAAAAACK!!! (arbitrary paras.)
    CUDA_VISIBLE_DEVICES=3 python make_bert_data.py -seg_path $TAGGED_FI -data_path $DATA_DIR --output_dir $DATA_DIR -n_clusters $N_CLSTR --bert_model "bert-base-uncased" --do_lower_case --reduce_memory $WORD_LEVEL 
}

with_gpu(){ # To run on server
    #for K in 35 55 75
    #do
    #    for KMUL in 1 5 9
    #    do
            kkstart=$SECONDS
            echo "TAGs=$TAG$EXTRA"

            #train
            MODEL=$MODEL.0
            #segment
            #analyze_seg
            #generate
            #analyze_gen
            #blank_filling
            make_bert_data

            echo "TAGs=$TAG$EXTRA, took "$(( SECONDS - kkstart ))" seconds in total"
    #    done
    #done
}
without_gpu(){  # To run locally
    DATA_DIR=/Users/shanglinghsu/mwp/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated
    blank_filling
}

format
#without_gpu
with_gpu