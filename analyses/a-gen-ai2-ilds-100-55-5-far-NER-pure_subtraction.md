# Analysis on generation
data=/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated
metadata_path=/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_valid.tsv
gen_path=/Users/shanglinghsu/mwp/ntg2/gens/gen-ai2-ilds-100-55-5-far-NER-pure_subtraction.md
### Top-1 (19 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 196 | 0 | 107 | 45 | 214 | 139 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | apple (c) | and <num> | apple (c) | in the | apple (c) | . Each | apple (c) | has <num> | apple (c) | to <PER_2> | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | banana (c) | has <num> | banana (c) | to <PER_2> | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | watermelon (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | fruit (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | apples (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | bananas (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | watermelons (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas  noun6:watermelons   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | banana (c) | has <num> | banana (c) | to <PER_2> | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | watermelon (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | fruit (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun0:apple  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | apples (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | bananas (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | watermelons (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas  noun6:watermelons  solution_type:Addition   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | banana (c) | has <num> | banana (c) | to <PER_2> | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | watermelon (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | watermelon (c) | to <PER_2> | . How many | fruit (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | apples (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | bananas (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas  solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | and <num> | banana (c) | in the | banana (c) | . Each | watermelon (c) | has <num> | apples (c) | to <PER_2> | . How many | watermelons (c) | does <PER_1> have now | ? <eos> | noun0:apple  noun1:banana  noun2:watermelon  noun3:fruit  noun4:apples  noun5:bananas  noun6:watermelons  solution_type:Subtraction   |

### Top-2 (4 samples using it): (271, 40, 186, 132, 13, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 13 | 92 | 172 | 107 | 45 | 214 | 139 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | <MISC_1> | in the | _noun0 | . <PER_2> has <num> | of the | _noun0 | . How many | _noun0 | does <PER_1> have | ? <eos> | solution_type:Addition   |
| <PER_1> has <num> | apple (c) | in the | apple (c) | . <PER_2> has <num> | of the | apple (c) | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple  solution_type:Addition   |
| <PER_1> has <num> | <MISC_1> | in the | _noun0 | . <PER_2> has <num> | of the | _noun0 | . How many | _noun0 | does <PER_1> have | ? <eos> | solution_type:Subtraction   |
| <PER_1> has <num> | apple (c) | in the | apple (c) | . <PER_2> has <num> | of the | apple (c) | . How many | apple (c) | does <PER_1> have now | ? <eos> | noun0:apple  solution_type:Subtraction   |


