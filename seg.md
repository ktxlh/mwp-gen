# Analysis on segmentation
metadata_path=/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=/Users/shanglinghsu/mwp/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt
k=5
n=1
# 1. top templates
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds | Heather has 60 oranges. Russell takes 35 away. How many oranges will Heather have? |

### Distribution of solution type, source using this template
| Subtraction | Addition |
| -------- | -------- |
| 13 (0.765) |4 (0.235) |

| ilds |
| -------- |
| 17 (1.000) |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds | Christopher strolled 5 miles at 4 miles per hour. How long did Christopher stroll? |

### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 7 (0.875) |1 (0.125) |

| ilds |
| -------- |
| 8 (1.000) |

### Top-3 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 | Keith has 20 books . Jason has 21 books . How many books do they have together ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-4 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds | Lillian collects 88 candies. Lillian's father gives Lillian 5 more. How many candies does Lillian have? |

### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-5 (7 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| I walk <num> | mile | every <num> | minutes | . I walked <num> | miles | . How many | minutes | did it take | <unk> | ? <eos> | Multiplication | ilds | I walk 1 mile every 15 minutes. I walked 3 miles. How many minutes did it take me ? |

### Distribution of solution type, source using this template
| Addition | Multiplication |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ai2 | ilds |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |



# 2. solution type - top templates
## Addition (258)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 | Keith has 20 books . Jason has 21 books . How many books do they have together ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-2 (6 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds | Lillian collects 88 candies. Lillian's father gives Lillian 5 more. How many candies does Lillian have? |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-3 (6 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | carrots | and <num> | turnips | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 | Sandy grew 8 carrots and 7 turnips . Mary grew 6 carrots . How many carrots did they grow in all ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ai2 |
| -------- |
| 6 (1.000) |

### Top-4 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds | There are 86 blocks. 9 blocks more are added. How many are there total? |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-5 (5 samples using it): (271, 40, 68, 228, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 228 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | peanuts | . <LOC_1> has <num> | more | than <PER_1> | . How many | peanuts | does <LOC_1> have | ? <eos> | Addition | ilds | Jose has 85 peanuts. Kenya has 48 more than Jose. How many peanuts does Kenya have? |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |


## Subtraction (254)
### Top-1 (13 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds | Heather has 60 oranges. Russell takes 35 away. How many oranges will Heather have? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 13 (1.000) |

| ilds |
| -------- |
| 13 (1.000) |

### Top-2 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds | Roger has 92 blocks. 2 are eaten by a hippopotamus. How many blocks will Roger have? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-3 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds | Norma has 88 cards. She loses 70. How many cards will Norma have? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-4 (5 samples using it): (271, 40, 178, 66, 164, 214, 139)
| 271 | 40 | 178 | 66 | 164 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> weighs <num> | pounds | . <PER_2> weighs <num> | pounds | . How much heavier | is <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds | John weighs 81 pounds. Roy weighs 4 pounds. How much heavier is John than Roy? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-5 (4 samples using it): (271, 40, 99, 230, 229, 165, 107, 45, 214, 139)
| 271 | 40 | 99 | 230 | 229 | 165 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> <num> | oranges | . He | shares | <num> | with <PER_2> | . How many | oranges | will <PER_3> have | ? <eos> | Subtraction | ilds | Steve has 46 oranges. He shares 4 with Patrick. How many oranges will Steve have? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |


## CommonDiv (97)
### Top-1 (7 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds | Christopher strolled 5 miles at 4 miles per hour. How long did Christopher stroll? |

### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 7 (1.000) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-2 (5 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds | If Joan bicycled 25 miles at 5 miles per hour, how long was Joan travelling? |

### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-3 (5 samples using it): (271, 40, 232, 230, 229, 56, 89, 95, 3, 75, 253, 139)
| 271 | 40 | 232 | 230 | 229 | 56 | 89 | 95 | 3 | 75 | 253 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | erasers | . If he | shares | them among <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds | Eric has 9306 erasers. If he shares them among 99 friends, how many erasers does each friend get? |

### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-4 (4 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 39, 139)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 39 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> | jogging | ? <eos> | CommonDiv | ilds | If Teresa jogged 25 kilometers at 5 kilometers per hour, how long was Teresa jogging? |

### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |

### Top-5 (4 samples using it): (271, 40, 133, 162, 251, 72, 222, 254, 45, 214, 139)
| 271 | 40 | 133 | 162 | 251 | 72 | 222 | 254 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> sold <num> | boxes | of <MISC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does <PER_1> need | ? <eos> | CommonDiv | ilds | Sarah sold 24 boxes of Lemon Chalet Cremes. How many cases of 12 boxes, plus extra boxes does Sarah need? |

### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |


## Multiplication (93)
### Top-1 (5 samples using it): (90, 119, 196, 148, 42, 182, 53, 219, 197, 84)
| 90 | 119 | 196 | 148 | 42 | 182 | 53 | 219 | 197 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> wandered | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds | If Anne wandered for 3 hours at 2 miles per hour. How far did Anne go? |

### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-2 (4 samples using it): (271, 40, 17, 180, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | boxes | of | peanuts | . Each | box | holds <num> | peanuts | . How many | peanuts | does <PER_1> have | ? <eos> | Multiplication | ilds | Paula has 6 boxes of peanuts. Each box holds 4 peanuts. How many peanuts does Paula have? |

### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |

### Top-3 (3 samples using it): (271, 40, 186, 132, 272, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 272 | 95 | 3 | 75 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | crayons | in each | box | . How many | crayons | are in <num> | boxes | ? <eos> | Multiplication | ilds | There are 4 crayons in each box. How many crayons are in 3 boxes? |

### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |

### Top-4 (3 samples using it): (271, 40, 17, 180, 99, 230, 229, 196, 178, 66, 21, 22, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 196 | 178 | 66 | 21 | 22 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | boxes | of | eggs | . Each | box | holds <num> | eggs | and there are <num> | boxes | in a | <unk> | . How many | eggs | does <PER_1> have | ? <eos> | Multiplication | ilds | Maria has 3 boxes of eggs. Each box holds 7 eggs and there are 8 boxes in a case. How many eggs does Maria have? |

### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |

### Top-5 (3 samples using it): (200, 205, 243, 160, 40, 148, 42, 182, 53, 219, 197, 270, 59, 270, 75, 139)
| 200 | 205 | 243 | 160 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 270 | 59 | 270 | 75 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| It took <PER_1> <num> | hours | to stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds | It took Amanda 5 hours to stroll to Kimberly's house at 2 miles per hour. How far is it between Amanda's house and Kimberly's house? |

### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |


## TimeVariantUnknownFinal (35)
### Top-1 (2 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 13, 221, 203, 196, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 13 | 221 | 203 | 196 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> placed <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 | There are 48 erasers in the drawer and 30 erasers on the desk . Alyssa placed 39 erasers and 45 rulers on the desk . How many erasers are now there in total ?  |

### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-2 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| A | restaurant | served <num> | cakes | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | cakes | yesterday | . How many | cakes | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 | A restaurant served 5 cakes during lunch and 6 during dinner today . The restaurant served 3 cakes yesterday . How many cakes were served in total ?  |

### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-3 (1 samples using it): (271, 40, 177, 119, 196, 68, 228, 172, 107, 45, 214, 139)
| 271 | 40 | 177 | 119 | 196 | 68 | 228 | 172 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> <MISC_1> | cards | . <PER_2> gave | her <num> new <MISC_1> | cards | . <PER_1> bought <num> | <MISC_1> | cards | . How many <MISC_1> | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 | Sally had 27 Pokemon cards . Dan gave her 41 new Pokemon cards . Sally bought 20 Pokemon cards . How many Pokemon cards does Sally have now ?  |

### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-4 (1 samples using it): (271, 40, 186, 132, 99, 230, 229, 66, 147, 234, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 66 | 147 | 234 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> | dimes | in her | bank | . Her | dad | gave her <num> | dimes | and her | mother | gave her <num> | dimes | . How many | dimes | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 | Melanie had 7 dimes in her bank . Her dad gave her 8 dimes and her mother gave her 4 dimes . How many dimes does Melanie have now ?  |

### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-5 (1 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 178, 66, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> placed <num> | pencils | on the | desk | . How many | pencils | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 | There are 43 pencils in the drawer and 19 pencils on the desk . Dan placed 16 pencils on the desk . How many pencils are now there in total ?  |

### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |


## Sum (25)
### Top-1 (3 samples using it): (271, 40, 178, 66, 247, 119, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | , <PER_2> has <num> | books | , and <PER_3> | has <num> | books | . How many | books | do they have | together | ? <eos> | Sum | ai2 | Sandy has 10 books , Benny has 24 books , and Tim has 33 books . How many books do they have together ?  |

### Distribution of solution type, source using this template
| Sum |
| -------- |
| 3 (1.000) |

| ai2 |
| -------- |
| 3 (1.000) |

### Top-2 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 | Sally found 9 seashells , Tom found 7 seashells , and Jessica found 5 seashells on the beach . How many seashells did they find together ?  |

### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-3 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 267 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> blue | balloons | , <PER_2> has <num> | blue | balloons | , and <PER_3> | has <num> blue | balloons | . How many blue | balloons | do they have | in all | ? <eos> | Sum | ai2 | Alyssa has 37 blue balloons , Sandy has 28 blue balloons , and Sally has 39 blue balloons . How many blue balloons do they have in all ?  |

### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-4 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 203, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 203 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> picked <num> | limes | , <PER_2> picked <num> | limes | , and <PER_3> | picked <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were picked | in total | ? <eos> | Sum | ai2 | Fred picked 36 limes , Alyssa picked 32 limes , and Nancy picked 35 limes and 18 pears , at the farm . How many limes were picked in total ?  |

### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-5 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 12, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 12 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | pumpkins | , <PER_2> grew <num> | pumpkins | , and <PER_3> | grew <num> | pumpkins | . They worked | for <num> | days | on the | farm | . How many | pumpkins | did they grow | in all | ? <eos> | Sum | ai2 | Joan grew 24 pumpkins , Keith grew 42 pumpkins , and Alyssa grew 13 pumpkins . They worked for 34 days on the farm . How many pumpkins did they grow in all ?  |

### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |



# 3. dataset - top templates / duplicated sentences
## ilds (449)
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds | Heather has 60 oranges. Russell takes 35 away. How many oranges will Heather have? |

### Distribution of solution type, source using this template
| Subtraction | Addition |
| -------- | -------- |
| 13 (0.765) |4 (0.235) |

| ilds |
| -------- |
| 17 (1.000) |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds | Christopher strolled 5 miles at 4 miles per hour. How long did Christopher stroll? |

### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 7 (0.875) |1 (0.125) |

| ilds |
| -------- |
| 8 (1.000) |

### Top-3 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds | Lillian collects 88 candies. Lillian's father gives Lillian 5 more. How many candies does Lillian have? |

### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-4 (6 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds | If Joan bicycled 25 miles at 5 miles per hour, how long was Joan travelling? |

### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 5 (0.833) |1 (0.167) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-5 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds | Roger has 92 blocks. 2 are eaten by a hippopotamus. How many blocks will Roger have? |

### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |


## ai2 (316)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 | Keith has 20 books . Jason has 21 books . How many books do they have together ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-2 (6 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | carrots | and <num> | turnips | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 | Sandy grew 8 carrots and 7 turnips . Mary grew 6 carrots . How many carrots did they grow in all ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ai2 |
| -------- |
| 6 (1.000) |

### Top-3 (5 samples using it): (271, 40, 178, 66, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> found <num> | seashells | and <PER_2> found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Addition | ai2 | Sam found 18 seashells and Mary found 47 seashells on the beach . How many seashells did they find together ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ai2 |
| -------- |
| 5 (1.000) |

### Top-4 (4 samples using it): (271, 40, 186, 132, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> | quarters | in her | bank | . Her | dad | gave her <num> | quarters | . How many | quarters | does she have now | ? <eos> | Addition | ai2 | Sara had 21 quarters in her bank . Her dad gave her 49 quarters . How many quarters does she have now ?  |

### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 3 (0.750) |1 (0.250) |

| ai2 |
| -------- |
| 4 (1.000) |

### Top-5 (4 samples using it): (271, 40, 13, 221, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 13 | 221 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source | question |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> picked <num> | plums | and <PER_2> picked <num> | plums | . <PER_3> picked <num> | pears | . How many | plums | were picked | in all | ? <eos> | Addition | ai2 | Alyssa picked 17 plums and Jason picked 10 plums . Melanie picked 35 pears . How many plums were picked in all ?  |

### Distribution of solution type, source using this template
| Addition |
| -------- |
| 4 (1.000) |

| ai2 |
| -------- |
| 4 (1.000) |


