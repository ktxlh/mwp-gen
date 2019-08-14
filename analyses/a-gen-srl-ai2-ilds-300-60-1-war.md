Namespace(a_gen=True, a_seg=False, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='gens/gen-srl-ai2-ilds-300-60-1-war.md', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-60-1-war.txt')
# Analysis of generation
data=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_valid.tsv
gen_path=gens/gen-srl-ai2-ilds-300-60-1-war.md
### Top-1 (9 samples using it): (2, 46, 42, 18, 28, 32, 13, 28, 32, 13, 28, 32, 13)
| 2 | 46 | 42 | 18 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew (c) | <num> | turnips (c) | . How many | turnips (c) | . How many | . How many | turnips (c) | . How many | . How many | turnips (c) | in all ? <eos> | V:did grow grew  ARG2:turnips  ARG1:turnips   |
| <PER_1> | had (c) | <num> | quarters (c) | . How many | have (c) | . How many | . How many | have (c) | . How many | . How many | have (c) | in all ? <eos> | V:does had borrowed have  ARG1:quarters  ARGM-LOC:bank  ARG0:sister   |
| <PER_1> | has (c) | <num> | balloons (c) | . How many | have (c) | balloons (c) | . How many | have (c) | balloons (c) | . How many | have (c) | in all ? <eos> | V:has gave does have  ARG1:balloons   |
| <PER_1> | found (c) | <num> | seashells (c) | . How many | seashells (c) | . How many | . How many | seashells (c) | . How many | . How many | seashells (c) | in all ? <eos> | V:did find broken found were  ARG1:seashells   |
| <PER_1> | grew (c) | <num> | cantelopes (c) | . How many | cantelopes (c) | . How many | . How many | cantelopes (c) | . How many | . How many | cantelopes (c) | in all ? <eos> | V:did grow grew  ARG2:cantelopes  ARG1:cantelopes   |
| <PER_1> | grew (c) | <num> | watermelons (c) | . How many | watermelons (c) | . How many | . How many | watermelons (c) | . How many | . How many | watermelons (c) | in all ? <eos> | V:does ate grew have  ARG2:watermelons  ARG0:rabbits  ARG1:watermelons   |
| <PER_1> | picked (c) | <num> | plums (c) | . How many | <num> | . How many | . How many | . How much | . How many | . How many | <num> | in all ? <eos> | V:picked were  ARG1:pears plums   |
| <PER_1> | bought (c) | <num> | pounds (c) | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | in all ? <eos> | V:did buy bought  ARG1:peppers pounds   |
| <PER_1> | had (c) | <num> | dollars (c) | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | in all ? <eos> | ARGM-TMP:weekend week  V:did make has had washed  ARG1:cars dollars   |

### Top-2 (1 samples using it): (2, 46, 42, 18, 28, 32, 13, 28, 32, 13, 28, 32, 13, 28, 32, 13, 28, 32, 13, 28, 32, 13, 28, 32, 13, 28, 32, 13)
| 2 | 46 | 42 | 18 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | 28 | 32 | 13 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | hiked (c) | <num> | miles (c) | . How many | . How much | . How many | . How many | . How much | in all ? many | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | . How many | . How many | . How much | in all ? <eos> | V:did hiked  ARG1:miles   |

### Top-3 (1 samples using it): (51, 50, 27, 50, 48, 46, 42, 18, 28)
| 51 | 50 | 27 | 50 | 48 | 46 | 42 | 18 | 28 | conditions |
| - | - | - | - | - | - | - | - | - | - |
| A | restaurant (c) | <num> | restaurant (c) | restaurant (c) | served (c) | <num> | cakes (c) | in all ? <eos> | ARG0:restaurant  V:were served  ARG1:cakes  ARGM-TMP:yesterday lunch   |


