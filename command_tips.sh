echo '# Viterbi Segmentation/Template Extraction'
scp shangling@140.109.19.51:~/ntg2/segs/seg-e2e-300-55-5-far.txt ~/mwp/ntg2/segs
scp shangling@140.109.19.51:~/ntg2/analyses/a-seg-e2e-300-55-5-far.md ~/mwp/ntg2/analyses
open ~/mwp/ntg2/analyses/a-seg-e2e-300-55-5-far.md
echo '# Generation'
scp shangling@140.109.19.51:~/ntg2/gens/gen-e2e-300-55-5-far.md ~/mwp/ntg2/gens
open ~/mwp/ntg2/segs/seg-e2e-300-55-5-far.txt
open ~/mwp/ntg2/gens/gen-e2e-300-55-5-far.md
scp shangling@140.109.19.51:~/ntg2/analyses/a-gen-e2e-300-55-5-far.md ~/mwp/ntg2/analyses
open ~/mwp/ntg2/analyses/a-gen-e2e-300-55-5-far.md
