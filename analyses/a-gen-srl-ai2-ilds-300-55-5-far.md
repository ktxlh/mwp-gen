Namespace(a_gen=True, a_seg=False, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='gens/gen-srl-ai2-ilds-300-55-5-far.md', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-55-5-far.txt')
# Analysis on generation
data=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_valid.tsv
gen_path=gens/gen-srl-ai2-ilds-300-55-5-far.md
### Top-1 (28 samples using it): (200, 44, 129, 197, 118, 210, 261, 239, 187, 257, 234, 18, 219, 198)
| 200 | 44 | 129 | 197 | 118 | 210 | 261 | 239 | 187 | 257 | 234 | 18 | 219 | 198 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> starts with <num> | soup (c) | in a | salad (c) | . If he | and <num> | bill (c) | in a | salad (c) | . How many | bill (c) | are there in the | salad (c) | ? <eos> | ARG1:soup  ARG2:salad   |
| <PER_1> has <num> | dollars (c) | in a | week (c) | . If he | and <num> | dollars (c) | in a | cars (c) | . How many | dollars (c) | are there in the | week (c) | ? <eos> | ARGM-TMP:weekend  ARG1:cars   |
| <PER_1> has <num> | dimes (c) | in a | bank (c) | . If went | and <num> | dimes (c) | in a | bank (c) | . How many | dimes (c) | are there in the | bank (c) | ? <eos> | ARG1:dimes  ARGM-LOC:bank  ARG0:sister   |
| <PER_1> has <num> | potatoes (c) | in a | garden (c) | . If he | and <num> | potatoes (c) | in a | garden (c) | . How many | potatoes (c) | are there in the | garden (c) | ? <eos> | ARG1:cantelopes  ARGM-LOC:garden  ARG0:rabbits   |
| <PER_1> has <num> | pizzas (c) | in a | lunch (c) | . If there | and <num> | pizzas (c) | in a | today (c) | . How many | pizzas (c) | are there in the | today (c) | ? <eos> | ARG0:restaurant  ARG1:pizzas  ARGM-TMP:today   |
| <PER_1> has <num> | dimes (c) | in a | bank (c) | . If went | and <num> | dimes (c) | in a | bank (c) | . How many | dimes (c) | are there in the | bank (c) | ? <eos> | ARG1:dimes  ARGM-LOC:bank  ARG0:dad   |
| <PER_1> has <num> | plums (c) | in a | plums (c) | . If he | and <num> | plums (c) | in a | pears (c) | . How many | plums (c) | are there in the | pears (c) | ? <eos> | ARG1:pears   |
| <PER_1> starts with <num> | pencils (c) | in a | desk (c) | . If there | and <num> | pencils (c) | in a | desk (c) | . How many | pencils (c) | are there in the | desk (c) | ? <eos> | ARG1:drawer  ARG2:desk   |
| <PER_1> starts with <num> | bales (c) | in a | barn (c) | . If he | and <num> | bales (c) | in a | barn (c) | . How many | bales (c) | are there in the | today (c) | ? <eos> | ARG1:shed  ARG2:barn  ARGM-TMP:today  ARGM-LOC:barn   |
| <PER_1> starts with <num> | garments (c) | in a | trunks (c) | . If there | and <num> | garments (c) | in a | bikinis (c) | . How many | fraction (c) | are there in the | bikinis (c) | ? <eos> | ARG1:fraction  ARG2:bikinis   |
| <PER_1> has <num> | balloons (c) | in a | balloons (c) | . If went | and <num> | balloons (c) | in a | balloons (c) | . How many | balloons (c) | are there in the | balloons (c) | ? <eos> | ARG1:balloons   |
| <PER_1> has <num> | bushes (c) | in a | park (c) | . If he | and <num> | plant (c) | in a | park (c) | . How many | plant (c) | are there in the | today (c) | ? <eos> | ARG1:today  ARGM-LOC:park  ARG0:workers  V:plant  ARGM-TMP:workers   |
| <PER_1> starts with <num> | balls (c) | in a | scale (c) | . If she | and <num> | scale (c) | in a | scale (c) | . How many | pounds (c) | are there in the | class (c) | ? <eos> | ARG1:balls  ARGM-TMP:class  ARG3:pounds  ARG2:scale  V:read   |
| <PER_1> starts with <num> | miles (c) | in a | home (c) | . If he | and <num> | miles (c) | in a | ride (c) | . How many | miles (c) | are there in the | walk (c) | ? <eos> | ARGM-TMP:afternoon  ARG1:miles  ARG2:home  V:ride   |
| <PER_1> has <num> | peppers (c) | in a | peppers (c) | . If went | and <num> | peppers (c) | in a | buy (c) | . How many | pounds (c) | are there in the | buy (c) | ? <eos> | ARG1:peppers  V:buy   |
| <PER_1> has <num> | nickels (c) | in a | bank (c) | . If went | and <num> | nickels (c) | in a | bank (c) | . How many | nickels (c) | are there in the | bank (c) | ? <eos> | ARG1:nickels  ARGM-LOC:bank  ARG0:dad   |
| <PER_1> starts with <num> | caterpillar (c) | in a | backyard (c) | . If went | and <num> | orange (c) | in a | backyard (c) | . How many | inches (c) | are there in the | backyard (c) | ? <eos> | ARG1:caterpillar  ARGM-LOC:backyard  ARG2:inches   |
| <PER_1> has <num> | trees (c) | in a | park (c) | . If there | and <num> | trees (c) | in a | today (c) | . How many | dogwood (c) | are there in the | today (c) | ? <eos> | ARG1:workers  ARG0:workers  V:plant  ARGM-TMP:workers   |
| <PER_1> starts with <num> | bucket (c) | in a | water (c) | . If she | and <num> | gallon (c) | in a | water (c) | . How many | gallon (c) | are there in the | water (c) | ? <eos> | ARG1:water  ARG2:water   |
| <PER_1> has <num> | trees (c) | in a | park (c) | . If there | and <num> | trees (c) | in a | today (c) | . How many | dogwood (c) | are there in the | today (c) | ? <eos> | ARG1:workers  ARG0:workers  V:plant  ARGM-TMP:workers   |
| <PER_1> starts with <num> | roses (c) | in a | garden (c) | . If there | and <num> | roses (c) | in a | garden (c) | . How many | roses (c) | are there in the | garden (c) | ? <eos> | ARG1:vase  ARG2:garden   |
| <PER_1> has <num> | marbles (c) | in a | violet (c) | . If she | and <num> | marbles (c) | in a | marbles (c) | . How many | marbles (c) | are there in the | marbles (c) | ? <eos> | ARG1:marbles   |
| <PER_1> has <num> | seashells (c) | in a | beach (c) | . If there | and <num> | seashells (c) | in a | seashells (c) | . How many | seashells (c) | are there in the | seashells (c) | ? <eos> | ARG1:seashells   |
| <PER_1> starts with <num> | ounces (c) | in a | floor (c) | . If she | and <num> | sugar (c) | in a | floor (c) | . How many | sugar (c) | are there in the | floor (c) | ? <eos> | ARG1:ounces  ARG2:floor   |
| <PER_1> starts with <num> | part (c) | in a | corporation (c) | . If she | and <num> | part (c) | in a | corporation (c) | . How many | time (c) | are there in the | corporation (c) | ? <eos> | ARG0:multi  ARG1:employees  ARG2:corporation   |
| <PER_1> starts with <num> | pencils (c) | in a | drawer (c) | . If there | and <num> | pencils (c) | in a | drawer (c) | . How many | pencils (c) | are there in the | drawer (c) | ? <eos> | ARG1:drawer  ARG2:drawer   |
| <PER_1> starts with <num> | yen (c) | in a | yen (c) | . If she | and <num> | yen (c) | in a | yen (c) | . How many | money (c) | are there in the | account (c) | ? <eos> | ARG1:money  ARG2:yen  ARG0:savings  V:account   |
| <PER_1> starts with <num> | bales (c) | in a | barn (c) | . If there | and <num> | bales (c) | in a | barn (c) | . How many | bales (c) | are there in the | today (c) | ? <eos> | ARG1:barn  ARGM-LOC:barn  ARG2:barn  ARGM-TMP:today   |

### Top-2 (12 samples using it): (90, 21, 45, 44, 129, 197, 192, 97, 169, 147, 117, 165, 198)
| 90 | 21 | 45 | 44 | 129 | 197 | 192 | 97 | 169 | 147 | 117 | 165 | 198 | conditions |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> starts with <num> | kittens (c) | and <num> | kittens (c) | in a | friends (c) | . <PER_2> has <num> | cat (c) | to <PER_2> | . How many | kittens (c) | does <PER_1> have | ? <eos> | ARG0:cat  ARG1:spots  ARG2:friends   |
| <PER_1> starts with <num> | band (c) | and <num> | students (c) | in a | trombone (c) | . <PER_2> has <num> | students (c) | to <PER_2> | . How many | band (c) | does <PER_1> have | ? <eos> | ARG1:fraction  ARG2:section   |
| <PER_1> starts with <num> | bar (c) | and <num> | pitcher (c) | in a | lemonade (c) | . <PER_2> has <num> | snack (c) | to <PER_2> | . How many | bar (c) | does <PER_1> have | ? <eos> | ARGM-TMP:play  ARG1:bar  ARG2:intermission  V:pour   |
| <PER_1> has <num> | neighboring (c) | and <num> | cornfields (c) | in a | cornfields (c) | . <PER_2> has <num> | corn (c) | to <PER_2> | . How many | neighboring (c) | does <PER_1> have | ? <eos> | ARG1:cornfields   |
| <PER_1> has <num> | mile (c) | and <num> | rides (c) | in a | car (c) | . <PER_2> has <num> | carnival (c) | to <PER_2> | . How many | mile (c) | does <PER_1> have | ? <eos> | ARG4:county  ARGM-TMP:weekend  ARG1:car  ARG3:carnival  V:walk   |
| <PER_1> has <num> | trees (c) | and <num> | trees (c) | in a | park (c) | . <PER_2> has <num> | workers (c) | to <PER_2> | . How many | trees (c) | does <PER_1> have | ? <eos> | ARG1:workers  ARG0:workers  V:plant  ARGM-TMP:workers   |
| <PER_1> has <num> | trees (c) | and <num> | trees (c) | in a | park (c) | . <PER_2> has <num> | workers (c) | to <PER_2> | . How many | trees (c) | does <PER_1> have | ? <eos> | ARG1:workers  ARG0:workers  V:plant  ARGM-TMP:workers   |
| <PER_1> has <num> | game (c) | and <num> | game (c) | in a | basketball (c) | . <PER_2> has <num> | game (c) | to <PER_2> | . How many | games (c) | does <PER_1> have | ? <eos> | ARG1:basketball   |
| <PER_1> has <num> | light (c) | and <num> | light (c) | in a | years (c) | . <PER_2> has <num> | spaceship (c) | to <PER_2> | . How many | year (c) | does <PER_1> have | ? <eos> | ARG0:spaceship  ARG1:light  ARGM-TMP:years  V:travel   |
| <PER_1> starts with <num> | pies (c) | and <num> | pies (c) | in a | pies (c) | . <PER_2> has <num> | employees (c) | to <PER_2> | . How many | pies (c) | does <PER_1> have | ? <eos> | ARGM-TMP:morning  ARG0:employees  ARG1:pies  ARG2:pies   |
| <PER_1> starts with <num> | miles (c) | and <num> | running (c) | in a | soccer (c) | . <PER_2> has <num> | drill (c) | to <PER_2> | . How many | miles (c) | does <PER_1> have | ? <eos> | ARG1:running  V:running  ARG0:drill  ARG2:season   |
| <PER_1> has <num> | fish (c) | and <num> | salmon (c) | in a | fish (c) | . <PER_2> has <num> | bear (c) | to <PER_2> | . How many | fish (c) | does <PER_1> have | ? <eos> | ARGM-TMP:day  ARG0:zoo  ARG1:salmon  V:eat   |


