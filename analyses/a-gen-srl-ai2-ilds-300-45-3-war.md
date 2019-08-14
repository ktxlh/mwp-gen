Namespace(a_gen=True, a_seg=False, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='gens/gen-srl-ai2-ilds-300-45-3-war.md', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-45-3-war.txt')
# Analysis of generation
data=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_valid.tsv
gen_path=gens/gen-srl-ai2-ilds-300-45-3-war.md
### Top-1 (19 samples using it): (119, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are (c) | <num> | dogwood (c) | . Each | plant (c) | for $ <num> | . How many | trees (c) | will (c) | the | have (c) | to | ? <eos> | V:are plant have will finished  ARG1:park dogwood workers trees  ARG0:park workers  ARGM-TMP:today workers tomorrow   |
| <PER_1> | baking (c) | <num> | cups (c) | . Each | is (c) | for <num> more | . How many | flour (c) | does (c) | <PER_1> | need (c) | to | ? <eos> | V:is need put wants add baking does  ARG1:cake flour cups  ARG0:recipe   |
| <PER_1> | had (c) | <num> | mile (c) | . <PER_1> | got (c) | for $ <num> | . How many | mile (c) | did (c) | <PER_1> | walk (c) | to | ? <eos> | V:did walked had went walk got rides  ARG4:fair county  ARGM-TMP:weekend  ARG1:car mile rides carnival  ARG3:carnival   |
| <PER_1> | had (c) | <num> | quarters (c) | . Each | borrowed (c) | <num> more | . How many | quarters (c) | does (c) | <PER_1> | have (c) | to | ? <eos> | V:does had borrowed have  ARG1:quarters  ARGM-LOC:bank  ARG0:sister   |
| <PER_1> | found (c) | <num> | seashells (c) | . <PER_2> | found (c) | <num> more | . How many | seashells (c) | did (c) | <PER_1> | find (c) | to | ? <eos> | V:did find broken found were  ARG1:seashells   |
| <PER_1> | hiked (c) | <num> | miles (c) | . <PER_2> | hiked (c) | <num> more | . How many | miles (c) | did (c) | <PER_1> | hiked (c) | to | ? <eos> | V:did hiked  ARG1:miles   |
| <PER_1> | are (c) | <num> | houses (c) | . Each | built (c) | for <num> more | . How many | houses (c) | are (c) | the | built (c) | to | ? <eos> | V:built were are  ARG1:houses  ARGM-TMP:housing boom  ARG0:developers   |
| <PER_1> | had (c) | <num> | oak (c) | . Each | cut (c) | for $ <num> | . How many | trees (c) | will (c) | the | cut (c) | to | ? <eos> | V:are had will were finished be damaged cut  ARG1:park trees oak workers  ARG0:workers  ARG2:park  ARGM-TMP:workers   |
| <PER_1> | had (c) | <num> | walnut (c) | . Each | cut (c) | for $ <num> | . How many | trees (c) | will (c) | the | cut (c) | to | ? <eos> | V:are had will were finished be damaged cut  ARG1:park walnut orange trees workers  ARG0:workers  ARG2:park  ARGM-TMP:workers   |
| <PER_1> | grew (c) | <num> | cantelopes (c) | . <PER_2> | grew (c) | <num> more | . How many | cantelopes (c) | did (c) | <PER_1> | grow (c) | to | ? <eos> | V:did grow grew  ARG2:cantelopes  ARG1:cantelopes   |
| <PER_1> | grew (c) | <num> | watermelons (c) | . Each | ate (c) | <num> more | . How many | watermelons (c) | does (c) | <PER_1> | have (c) | to | ? <eos> | V:does ate grew have  ARG2:watermelons  ARG0:rabbits  ARG1:watermelons   |
| <PER_1> | has (c) | <num> | fruit (c) | . Each | sold (c) | for $ <num> | . How many | fruit (c) | been (c) | <PER_1> | have (c) | to | ? <eos> | V:sold have has been combined  ARG0:orchard  ARG1:total pounds fruit  ARGM-TMP:season  ARG3:total   |
| <PER_1> | picked (c) | <num> | plums (c) | . <PER_1> | picked (c) | for $ <num> | . How many | pears (c) | were (c) | <PER_1> | picked (c) | to | ? <eos> | V:picked were  ARG1:pears plums   |
| <PER_1> | bought (c) | <num> | peppers (c) | . <PER_2> | bought (c) | for <num> more | . How many | peppers (c) | did (c) | <PER_1> | buy (c) | to | ? <eos> | V:did buy bought  ARG1:peppers pounds   |
| <PER_1> | had (c) | <num> | pennies (c) | . Each | gave (c) | <num> more | . How many | quarters (c) | does (c) | <PER_1> | have (c) | to | ? <eos> | V:gave had does have  ARG1:pennies quarters  ARGM-LOC:bank  ARG0:mother dad   |
| <PER_1> | were (c) | <num> | cakes (c) | . Each | served (c) | for <num> more | . How many | cakes (c) | were (c) | <PER_1> | served (c) | to | ? <eos> | ARG0:restaurant  V:were served  ARG1:cakes  ARGM-TMP:yesterday lunch   |
| <PER_1> | served (c) | <num> | lemonade (c) | . <PER_1> | served (c) | for $ <num> | . How many | bar (c) | did (c) | <PER_1> | staffed (c) | to | ? <eos> | ARGM-TMP:school play  V:did pour staffed served  ARG1:pitcher pitchers bar snack lemonade  ARG2:pitcher lemonade intermission   |
| <PER_1> | had (c) | <num> | dollars (c) | . <PER_1> | washed (c) | for <num> more | . How many | cars (c) | did (c) | <PER_1> | make (c) | to | ? <eos> | ARGM-TMP:weekend week  V:did make has had washed  ARG1:cars dollars   |
| <PER_1> | bought (c) | <num> | kilograms (c) | . If there | bought (c) | for $ <num> | . How many | nuts (c) | did (c) | the | buy (c) | to | ? <eos> | ARG0:chef  V:did buy bought  ARG1:almonds kilograms nuts pecans   |

### Top-2 (2 samples using it): (119, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 62 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew (c) | <num> | turnips (c) | . <PER_2> | grew (c) | <num> more | . How many | turnips (c) | did (c) | <PER_1> | grow (c) | ? <eos> | V:did grow grew  ARG2:turnips  ARG1:turnips   |
| <PER_1> | has (c) | <num> | balloons (c) | . <PER_2> | gave (c) | <num> more | . How many | balloons (c) | does (c) | <PER_1> | have (c) | ? <eos> | V:has gave does have  ARG1:balloons   |


