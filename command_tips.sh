echo '# Viterbi Segmentation/Template Extraction'
scp shangling@140.109.19.51:~/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt ~/mwp/ntg2/segs
open ~/mwp/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt
echo '# Generation'
scp shangling@140.109.19.51:~/ntg2/gens/gen-ai2-cmds-100-55-5-far-NER.md ~/mwp/ntg2/gens
open ~/mwp/ntg2/gens/gen-ai2-cmds-100-55-5-far-NER.md
