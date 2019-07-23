# Analysis on segmentation
metadata_path=/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=/Users/shanglinghsu/mwp/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt
k=5
n=100
# 1. top templates
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | apples | . <PER_2> takes <num> | away | . How many | apples | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . <PER_2> takes <num> | away | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | blocks | . He gives <num> | to <PER_2> | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . She gives <num> | to <PER_2> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | cards | . <PER_2> takes <num> | away | . How many | cards | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <LOC_1> starts with <num> | eggs | . <PER_1> takes <num> | away | . How many | eggs | does <LOC_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | eggs | . She buys <num> | more | . How many | eggs | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | eggs | . He buys <num> | more | . How many | eggs | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | candies | . <PER_2> takes <num> | away | . How many | candies | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . He buys <num> | more | . How many | apples | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | cards | . He finds | another <num> | . How many | cards | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | eggs | . He gives <num> | to <MISC_1> | . How many | eggs | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | stickers | . He gives <num> | to <PER_2> | . How many | stickers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | erasers | . He gives <num> | to <PER_2> | . How many | erasers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . She gives <num> | to <PER_2> | . How many | apples | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction | Addition |
| -------- | -------- |
| 13 (0.765) |4 (0.235) |

| ilds |
| -------- |
| 17 (1.000) |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> strolled <num> | kilometers | at <num> | kilometers | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> flew <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| <PER_1> sprinted <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> wandered <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> wandered <num> | kilometers | at <num> | kilometers | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 7 (0.875) |1 (0.125) |

| ilds |
| -------- |
| 8 (1.000) |

### Top-3 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | pumpkins | . <PER_2> grew <num> | pumpkins | . How many | pumpkins | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | cantelopes | . <PER_2> grew <num> | cantelopes | . How many | cantelopes | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in all | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-4 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> had <num> | pencils | . He gave <num> | pencils | to <PER_2> | . How many | pencils | does <PER_1> have left | ? <eos> | Subtraction | ilds |
| <PER_1> collects <num> | oranges | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | oranges | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | blocks | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | blocks | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | peanuts | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | peanuts | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | cards | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | cards | does <PER_1> have | ? <eos> | Addition | ilds |

#### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-5 (7 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| I walk <num> | mile | every <num> | minutes | . I walked <num> | miles | . How many | minutes | did it take | <unk> | ? <eos> | Multiplication | ilds |
| <PER_1> grew <num> | carrots | and <num> | turnips | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | cantelopes | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | and <num> | watermelons | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | cantelopes | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | pumpkins | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | pumpkins | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition | Multiplication |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ai2 | ilds |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |



# 2. solution type - top templates
## Addition (258 samples)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | pumpkins | . <PER_2> grew <num> | pumpkins | . How many | pumpkins | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | cantelopes | . <PER_2> grew <num> | cantelopes | . How many | cantelopes | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in all | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-2 (6 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | oranges | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | oranges | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | blocks | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | blocks | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | peanuts | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | peanuts | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | cards | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | cards | does <PER_1> have | ? <eos> | Addition | ilds |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-3 (6 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | carrots | and <num> | turnips | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | cantelopes | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | and <num> | watermelons | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | cantelopes | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | pumpkins | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | pumpkins | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ai2 |
| -------- |
| 6 (1.000) |

### Top-4 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds |
| There are <num> | marbles | . <num> | marbles | more | are added | . How many | are there total | ? <eos> | Addition | ilds |
| There are <num> | oranges | . <num> | oranges | more | are added | . How many | are there total | ? <eos> | Addition | ilds |
| There are <num> | cards | . <num> | cards | more | are added | . How many | are there total | ? <eos> | Addition | ilds |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-5 (5 samples using it): (271, 40, 68, 228, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 228 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | peanuts | . <LOC_1> has <num> | more | than <PER_1> | . How many | peanuts | does <LOC_1> have | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | candies | . She gets <num> | more | from <PER_2> | . How many | candies | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | cards | . She gets <num> | more | from <MISC_1> | . How many | cards | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | bananas | . She gets <num> | more | from <PER_2> | . How many | bananas | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | oranges | . She gets <num> | more | from <MISC_1> | . How many | oranges | does <PER_1> end with | ? <eos> | Addition | ilds |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |


## Subtraction (254 samples)
### Top-1 (13 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | apples | . <PER_2> takes <num> | away | . How many | apples | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . <PER_2> takes <num> | away | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | blocks | . He gives <num> | to <PER_2> | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . She gives <num> | to <PER_2> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | cards | . <PER_2> takes <num> | away | . How many | cards | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <LOC_1> starts with <num> | eggs | . <PER_1> takes <num> | away | . How many | eggs | does <LOC_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | candies | . <PER_2> takes <num> | away | . How many | candies | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | eggs | . He gives <num> | to <MISC_1> | . How many | eggs | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | stickers | . He gives <num> | to <PER_2> | . How many | stickers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | erasers | . He gives <num> | to <PER_2> | . How many | erasers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . She gives <num> | to <PER_2> | . How many | apples | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 13 (1.000) |

| ilds |
| -------- |
| 13 (1.000) |

### Top-2 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | crayons | . <num> | are eaten by a | hippopotamus | . How many | crayons | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | bananas | . <num> | are eaten by a | hippopotamus | . How many | bananas | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | cards | . <num> | are eaten by a | hippopotamus | . How many | cards | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | crayons | . <num> | are eaten by a | hippopotamus | . How many | crayons | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-3 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | marbles | . She loses <num> | . How many | marbles | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | erasers | . She loses <num> | . How many | erasers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | bananas | . She loses <num> | . How many | bananas | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | blocks | . She loses <num> | . How many | blocks | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-4 (5 samples using it): (271, 40, 178, 66, 164, 214, 139)
| 271 | 40 | 178 | 66 | 164 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> weighs <num> | pounds | . <PER_2> weighs <num> | pounds | . How much heavier | is <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-5 (4 samples using it): (271, 40, 99, 230, 229, 165, 107, 45, 214, 139)
| 271 | 40 | 99 | 230 | 229 | 165 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> <num> | oranges | . He | shares | <num> | with <PER_2> | . How many | oranges | will <PER_3> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | bananas | . She | shares | <num> | with <MISC_1> | . How many | bananas | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | marbles | . He | shares | <num> | with <PER_2> | . How many | marbles | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . She | shares | <num> | with <PER_2> | . How many | apples | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |


## CommonDiv (97 samples)
### Top-1 (7 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> strolled <num> | kilometers | at <num> | kilometers | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> flew <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| <PER_1> sprinted <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> wandered <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

#### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 7 (1.000) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-2 (5 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> strolled <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

#### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-3 (5 samples using it): (271, 40, 232, 230, 229, 56, 89, 95, 3, 75, 253, 139)
| 271 | 40 | 232 | 230 | 229 | 56 | 89 | 95 | 3 | 75 | 253 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | erasers | . If he | shares | them among <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> has <num> | marbles | . If she | shares | them among <num> | friends | , how many | marbles | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> has <num> | tickets | . If she | shares | them among <num> | friends | , how many | tickets | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> has <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> has <num> | erasers | . If she | shares | them among <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds |

#### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-4 (4 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 39, 139)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 39 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> | jogging | ? <eos> | CommonDiv | ilds |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

#### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |

### Top-5 (4 samples using it): (271, 40, 133, 162, 251, 72, 222, 254, 45, 214, 139)
| 271 | 40 | 133 | 162 | 251 | 72 | 222 | 254 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> sold <num> | boxes | of <MISC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does <PER_1> need | ? <eos> | CommonDiv | ilds |
| <PER_1> sold <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does <PER_1> need | ? <eos> | CommonDiv | ilds |

#### Distribution of solution type, source using this template
| CommonDiv |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |


## Multiplication (93 samples)
### Top-1 (5 samples using it): (90, 119, 196, 148, 42, 182, 53, 219, 197, 84)
| 90 | 119 | 196 | 148 | 42 | 182 | 53 | 219 | 197 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> wandered | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |
| If <PER_1> strolled | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |
| If <PER_1> ran | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |

#### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 5 (1.000) |

| ilds |
| -------- |
| 5 (1.000) |

### Top-2 (4 samples using it): (271, 40, 17, 180, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | boxes | of | peanuts | . Each | box | holds <num> | peanuts | . How many | peanuts | does <PER_1> have | ? <eos> | Multiplication | ilds |
| <PER_1> has <num> | boxes | of | crayons | . Each | box | holds <num> | crayons | . How many | crayons | does <PER_1> have | ? <eos> | Multiplication | ilds |
| <PER_1> has <num> | boxes | of | pencils | . Each | box | holds <num> | pencils | . How many | pencils | does <PER_1> have | ? <eos> | Multiplication | ilds |

#### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 4 (1.000) |

| ilds |
| -------- |
| 4 (1.000) |

### Top-3 (3 samples using it): (271, 40, 186, 132, 272, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | crayons | in each | box | . How many | crayons | are in <num> | boxes | ? <eos> | Multiplication | ilds |
| There are <num> | marbles | in each | box | . How many | marbles | are in <num> | boxes | ? <eos> | Multiplication | ilds |

#### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |

### Top-4 (3 samples using it): (271, 40, 17, 180, 99, 230, 229, 196, 178, 66, 21, 22, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 196 | 178 | 66 | 21 | 22 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | boxes | of | eggs | . Each | box | holds <num> | eggs | and there are <num> | boxes | in a | <unk> | . How many | eggs | does <PER_1> have | ? <eos> | Multiplication | ilds |
| <ORG_1> has <num> | boxes | of | tickets | . Each | box | holds <num> | tickets | and there are <num> | boxes | in a | <unk> | . How many | tickets | does <ORG_1> have | ? <eos> | Multiplication | ilds |

#### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |

### Top-5 (3 samples using it): (200, 205, 243, 160, 40, 148, 42, 182, 53, 219, 197, 270, 59, 270, 75, 139)
| 200 | 205 | 243 | 160 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 270 | 59 | 270 | 75 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| It took <PER_1> <num> | hours | to stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It took <PER_1> <num> | hours | to run | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

#### Distribution of solution type, source using this template
| Multiplication |
| -------- |
| 3 (1.000) |

| ilds |
| -------- |
| 3 (1.000) |


## TimeVariantUnknownFinal (35 samples)
### Top-1 (2 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 13, 221, 203, 196, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 13 | 221 | 203 | 196 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> placed <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |
| There are <num> | crayons | in the | drawer | and <num> | crayons | on the | desk | . <PER_1> placed <num> | crayons | and <num> | scissors | on the | desk | . How many | crayons | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

#### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-2 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| A | restaurant | served <num> | cakes | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | cakes | yesterday | . How many | cakes | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

#### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-3 (1 samples using it): (271, 40, 177, 119, 196, 68, 228, 172, 107, 45, 214, 139)
| 271 | 40 | 177 | 119 | 196 | 68 | 228 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> <MISC_1> | cards | . <PER_2> gave | her <num> new <MISC_1> | cards | . <PER_1> bought <num> | <MISC_1> | cards | . How many <MISC_1> | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

#### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-4 (1 samples using it): (271, 40, 186, 132, 99, 230, 229, 66, 147, 234, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 66 | 147 | 234 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> | dimes | in her | bank | . Her | dad | gave her <num> | dimes | and her | mother | gave her <num> | dimes | . How many | dimes | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

#### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |

### Top-5 (1 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 178, 66, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| There are <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> placed <num> | pencils | on the | desk | . How many | pencils | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

#### Distribution of solution type, source using this template
| TimeVariantUnknownFinal |
| -------- |
| 1 (1.000) |

| ai2 |
| -------- |
| 1 (1.000) |


## Sum (25 samples)
### Top-1 (3 samples using it): (271, 40, 178, 66, 247, 119, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | , <PER_2> has <num> | books | , and <PER_3> | has <num> | books | . How many | books | do they have | together | ? <eos> | Sum | ai2 |
| <PER_1> grew <num> | onions | , <PER_2> grew <num> | onions | , and <PER_3> | grew <num> | onions | . How many | onions | did they grow | in all | ? <eos> | Sum | ai2 |
| <PER_1> grew <num> | cantelopes | , <PER_2> grew <num> | cantelopes | , and <PER_3> | grew <num> | cantelopes | . How many | cantelopes | did they grow | in total | ? <eos> | Sum | ai2 |

#### Distribution of solution type, source using this template
| Sum |
| -------- |
| 3 (1.000) |

| ai2 |
| -------- |
| 3 (1.000) |

### Top-2 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 |
| <PER_1> picked <num> | pears | , <PER_2> picked <num> | pears | , and <PER_3> | picked <num> | pears | from the pear | tree | . How many | pears | were picked | in total | ? <eos> | Sum | ai2 |

#### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-3 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 267 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> blue | balloons | , <PER_2> has <num> | blue | balloons | , and <PER_3> | has <num> blue | balloons | . How many blue | balloons | do they have | in all | ? <eos> | Sum | ai2 |
| <PER_1> has <num> blue | balloons | , <PER_2> has <num> | blue | balloons | , and <PER_3> | has <num> blue | balloons | . How many blue | balloons | do they have | in total | ? <eos> | Sum | ai2 |

#### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-4 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 203, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 203 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> picked <num> | limes | , <PER_2> picked <num> | limes | , and <PER_3> | picked <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were picked | in total | ? <eos> | Sum | ai2 |
| <PER_1> picked <num> | apples | , <PER_2> picked <num> | apples | , and <PER_3> | picked <num> | apples | and <num> | pears | , at the | farm | . How many | apples | were picked | in total | ? <eos> | Sum | ai2 |

#### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |

### Top-5 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 12, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 12 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | pumpkins | , <PER_2> grew <num> | pumpkins | , and <PER_3> | grew <num> | pumpkins | . They worked | for <num> | days | on the | farm | . How many | pumpkins | did they grow | in all | ? <eos> | Sum | ai2 |
| <PER_1> grew <num> | onions | , <PER_2> grew <num> | onions | , and <PER_3> | grew <num> | onions | . They worked | for <num> | days | on the | farm | . How many | onions | did they grow | in total | ? <eos> | Sum | ai2 |

#### Distribution of solution type, source using this template
| Sum |
| -------- |
| 2 (1.000) |

| ai2 |
| -------- |
| 2 (1.000) |



# 3. dataset - top templates / duplicated sentences
## ilds (449 samples)
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | apples | . <PER_2> takes <num> | away | . How many | apples | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . <PER_2> takes <num> | away | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | blocks | . He gives <num> | to <PER_2> | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | cards | . She gives <num> | to <PER_2> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | cards | . <PER_2> takes <num> | away | . How many | cards | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <LOC_1> starts with <num> | eggs | . <PER_1> takes <num> | away | . How many | eggs | does <LOC_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | eggs | . She buys <num> | more | . How many | eggs | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | eggs | . He buys <num> | more | . How many | eggs | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | candies | . <PER_2> takes <num> | away | . How many | candies | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . He buys <num> | more | . How many | apples | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | cards | . He finds | another <num> | . How many | cards | does <PER_1> end with | ? <eos> | Addition | ilds |
| <PER_1> starts with <num> | eggs | . He gives <num> | to <MISC_1> | . How many | eggs | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | stickers | . He gives <num> | to <PER_2> | . How many | stickers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | erasers | . He gives <num> | to <PER_2> | . How many | erasers | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | apples | . She gives <num> | to <PER_2> | . How many | apples | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction | Addition |
| -------- | -------- |
| 13 (0.765) |4 (0.235) |

| ilds |
| -------- |
| 17 (1.000) |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> strolled <num> | kilometers | at <num> | kilometers | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> flew <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| <PER_1> sprinted <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> wandered <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> wandered <num> | kilometers | at <num> | kilometers | per | hour | . How long | did <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 7 (0.875) |1 (0.125) |

| ilds |
| -------- |
| 8 (1.000) |

### Top-3 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> had <num> | pencils | . He gave <num> | pencils | to <PER_2> | . How many | pencils | does <PER_1> have left | ? <eos> | Subtraction | ilds |
| <PER_1> collects <num> | oranges | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | oranges | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | blocks | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | blocks | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | peanuts | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | peanuts | does <PER_1> have | ? <eos> | Addition | ilds |
| <PER_1> collects <num> | cards | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | cards | does <PER_1> have | ? <eos> | Addition | ilds |

#### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 6 (0.857) |1 (0.143) |

| ilds |
| -------- |
| 7 (1.000) |

### Top-4 (6 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> strolled <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> walked <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> <unk> | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| CommonDiv | Subtraction |
| -------- | -------- |
| 5 (0.833) |1 (0.167) |

| ilds |
| -------- |
| 6 (1.000) |

### Top-5 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> has <num> | crayons | . <num> | are eaten by a | hippopotamus | . How many | crayons | will <PER_1> have | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | bananas | . <num> | are eaten by a | hippopotamus | . How many | bananas | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | cards | . <num> | are eaten by a | hippopotamus | . How many | cards | does <PER_1> end with | ? <eos> | Subtraction | ilds |
| <PER_1> starts with <num> | crayons | . <num> | are eaten by a | hippopotamus | . How many | crayons | does <PER_1> end with | ? <eos> | Subtraction | ilds |

#### Distribution of solution type, source using this template
| Subtraction |
| -------- |
| 6 (1.000) |

| ilds |
| -------- |
| 6 (1.000) |


## ai2 (316 samples)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | pumpkins | . <PER_2> grew <num> | pumpkins | . How many | pumpkins | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | cantelopes | . <PER_2> grew <num> | cantelopes | . How many | cantelopes | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in all | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 7 (1.000) |

| ai2 |
| -------- |
| 7 (1.000) |

### Top-2 (6 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> grew <num> | carrots | and <num> | turnips | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | cantelopes | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | carrots | and <num> | watermelons | . <PER_2> grew <num> | carrots | . How many | carrots | did they grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | cantelopes | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | turnips | and <num> | pumpkins | . <MISC_1> grew <num> | turnips | . How many | turnips | did they grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> grew <num> | watermelons | and <num> | pumpkins | . <MISC_1> grew <num> | watermelons | . How many | watermelons | did they grow | in total | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 6 (1.000) |

| ai2 |
| -------- |
| 6 (1.000) |

### Top-3 (5 samples using it): (271, 40, 178, 66, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> found <num> | seashells | and <PER_2> found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | <unk> | and <PER_2> picked <num> | <unk> | from the <unk> | tree | . How many | <unk> | were picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | pears | and <PER_2> picked <num> | pears | from the pear | tree | . How many | pears | were picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | pears | and <PER_2> picked <num> | pears | from the pear | tree | . How many | pears | were picked | in total | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 5 (1.000) |

| ai2 |
| -------- |
| 5 (1.000) |

### Top-4 (4 samples using it): (271, 40, 186, 132, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> had <num> | quarters | in her | bank | . Her | dad | gave her <num> | quarters | . How many | quarters | does she have now | ? <eos> | Addition | ai2 |
| <PER_1> had <num> | quarters | in his | bank | . His | dad | gave him <num> | quarters | . How many | quarters | does he have now | ? <eos> | Addition | ai2 |
| <PER_1> had <num> | nickels | in her | bank | . Her | dad | gave her <num> | nickels | . How many | nickels | does <PER_1> have now | ? <eos> | Addition | ai2 |
| <PER_1> had <num> | quarters | in her | bank | . Her | sister | borrowed <num> of her | quarters | . How many | quarters | does <PER_1> have now | ? <eos> | Subtraction | ai2 |

#### Distribution of solution type, source using this template
| Addition | Subtraction |
| -------- | -------- |
| 3 (0.750) |1 (0.250) |

| ai2 |
| -------- |
| 4 (1.000) |

### Top-5 (4 samples using it): (271, 40, 13, 221, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 13 | 221 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> picked <num> | plums | and <PER_2> picked <num> | plums | . <PER_3> picked <num> | pears | . How many | plums | were picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | limes | and <PER_2> picked <num> | limes | . <PER_3> picked <num> | plums | . How many | limes | were picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | oranges | and <PER_2> picked <num> | oranges | . <PER_3> picked <num> | pears | . How many | oranges | were picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> picked <num> | oranges | and <PER_2> picked <num> | oranges | . <PER_3> picked <num> | apples | . How many | oranges | were picked | in all | ? <eos> | Addition | ai2 |

#### Distribution of solution type, source using this template
| Addition |
| -------- |
| 4 (1.000) |

| ai2 |
| -------- |
| 4 (1.000) |


