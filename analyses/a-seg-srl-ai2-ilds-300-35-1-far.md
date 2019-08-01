Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-35-1-far.txt')
# Analysis of segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-35-1-far.txt
k=100
n=10
# Overall - top templates
### Top-1 (12 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | cantelopes | . <PER_2> | grew | <num> | cantelopes | . How many | cantelopes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <ORG_1> | grew | <num> | potatoes | . <PER_1> | grew | <num> | potatoes | . How many | potatoes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | pumpkins | . <PER_2> | grew | <num> | pumpkins | . How many | pumpkins | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many more | books | does | <PER_1> | have | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-2 (12 samples using it): (20, 12, 4, 14, 16, 12, 6, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 16 | 12 | 6 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <LOC_1> | starts | with <num> | eggs | . <PER_1> | takes | <num> | away | . How many | eggs | does | <LOC_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | cards | . <PER_2> | takes | <num> | away | . How many | cards | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | crayons | . <PER_2> | takes | <num> | away | . How many | crayons | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | candies | . <PER_2> | takes | <num> | away | . How many | candies | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | pencils | . He | gives | <num> | to <PER_2> | . How many | pencils | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | gives | <num> | to <PER_2> | . How many | stickers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | blocks | . She | shares | <num> | with <PER_2> | . How many | blocks | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | erasers | . He | gives | <num> | to <PER_2> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | eggs | . He | gives | <num> | to <MISC_1> | . How many | eggs | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | marbles | . He | shares | <num> | with <PER_2> | . How many | marbles | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-3 (10 samples using it): (20, 12, 6, 14, 16, 12, 6, 5, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 5 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <PER_2> | . <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | takes | <num> | away | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> | away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> | away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | bananas | . She | shares | <num> | with <MISC_1> | . How many | bananas | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . He | shares | <num> | with <PER_2> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . He | gives | <num> | to <PER_2> | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | <PER_2> | <num> | oranges | . He | shares | <num> | with <PER_3> | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-4 (10 samples using it): (20, 12, 4, 14, 16, 12, 4, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 16 | 12 | 4 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | eggs | . He | buys | <num> more | . How many | eggs | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | apples | . He | buys | <num> more | . How many | apples | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | cards | . He | finds | another <num> | . How many | cards | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | eggs | . She | buys | <num> more | . How many | eggs | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | eggs | . She | finds | another <num> | . How many | eggs | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | erasers | . <PER_2> | gives | <PER_1> <num> more | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | <PER_2> | . <PER_3> | gives | <PER_1> <num> more | . How many | <MISC_1> | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | peanuts | . <PER_2> | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bananas | . <PER_2> | gives | <PER_1> <num> more | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-5 (9 samples using it): (20, 12, 6, 14, 32, 10, 24, 11, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 24 | 11 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (7 samples using it): (20, 12, 6, 14, 32, 10, 24, 34, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 24 | 34 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-7 (6 samples using it): (20, 12, 6, 14, 16, 12, 4, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | . He | finds | another <num> | . How many | oranges | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . She | buys | <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | tickets | . <PER_2> | gives | <PER_1> <num> more | . How many | tickets | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | pencils | . <PER_2> | gives | <PER_1> <num> more | . How many | pencils | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . <PER_2> | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-8 (6 samples using it): (20, 12, 6, 14, 23, 3, 12, 4, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 23 | 3 | 12 | 4 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | candies | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | cards | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | cards | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | peanuts | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-9 (5 samples using it): (20, 12, 4, 14, 16, 12, 6, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 16 | 12 | 6 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | loses | <num> | . How many | stickers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | peanuts | . He | loses | <num> | . How many | peanuts | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | blocks | . She | loses | <num> | . How many | blocks | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . She | loses | <num> | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-10 (5 samples using it): (20, 12, 6, 14, 25, 16, 12, 4, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 25 | 16 | 12 | 4 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . She | buys | <num> more | . How many bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-11 (5 samples using it): (20, 12, 6, 14, 22, 15, 23, 3, 12, 4, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 23 | 3 | 12 | 4 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | quarters | in his | bank | . His | dad | gave | him <num> | quarters | . How many | quarters | does | he | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | dimes | in his | bank | . His | dad | gave | him <num> | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | nickels | in her | bank | . Her | dad | gave | her <num> | nickels | . How many | nickels | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | quarters | in her | bank | . Her | dad | gave | her <num> | quarters | . How many | quarters | does | she | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | dimes | in his | bank | . His | sister | borrowed | <num> of his | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-12 (5 samples using it): (20, 12, 6, 14, 22, 15, 32, 0, 23, 3, 12, 9, 22, 15, 11, 26, 18, 19, 30, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 32 | 0 | 23 | 3 | 12 | 9 | 22 | 15 | 11 | 26 | 18 | 19 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | students | in the | class | and <num> | eggs | . If the | eggs | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | pencils | . If the | pencils | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | apples | . If the | apples | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |

### Top-13 (5 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 6, 14, 22, 15, 16, 12, 6, 14, 22, 15, 34, 1, 26, 9, 22, 15, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | candies | in a | box | . <PER_1> | has | <num> | candies | in a | bag | . <PER_2> | takes | <num> | candies | out of the | box | . How many | candies | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | has | <num> | oranges | in a | bag | . <PER_2> | takes | <num> | oranges | out of the | box | . How many | oranges | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | apples | in a | box | . <PER_1> | has | <num> | apples | in a | bag | . <PER_2> | takes | <num> | apples | out of the | box | . How many | apples | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-14 (4 samples using it): (20, 12, 6, 10, 22, 15, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | crayons | in each | box | . How many | crayons | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-15 (4 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 6, 14, 34, 26, 8, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 34 | 26 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | eggs | in a | box | . <PER_1> | takes | <num> | eggs | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | pencils | in a | box | . <PER_1> | takes | <num> | pencils | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-16 (4 samples using it): (20, 12, 6, 14, 16, 12, 9, 22, 15, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 9 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <num> | are | eaten | by a | hippopotamus | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | crayons | . <num> | are | eaten | by a | hippopotamus | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-17 (4 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 5, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 5 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . <PER_2> | baked | <num> | times | as many | . How many | muffins | did | <PER_2> | bake | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does | <PER_2> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . <PER_2> | has | <num> more | marbles | than <PER_1> | . How many | marbles | does | <PER_2> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does | <PER_2> | have | ? <eos> | Subtraction | ilds |

### Top-18 (4 samples using it): (20, 12, 6, 14, 32, 14, 16, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 14 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | and <num> | watermelons | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | turnips | and <num> | pumpkins | . <MISC_1> | grew | <num> | turnips | . How many | turnips | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | turnips | . <ORG_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | pumpkins | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-19 (4 samples using it): (20, 12, 6, 28, 9, 22, 15, 16, 12, 6, 14, 11, 1, 26, 9, 22, 15, 27)
| 20 | 12 | 6 | 28 | 9 | 22 | 15 | 16 | 12 | 6 | 14 | 11 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | blocks | stored | in | boxes | . If there | are | <num> | boxes | , how many | blocks | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-20 (4 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 11, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 11 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | , <PER_2> | has | <num> | books | , and <PER_3> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Sum | ai2 |
| <PER_1> | grew | <num> | onions | , <PER_2> | grew | <num> | onions | , and <PER_3> | grew | <num> | onions | . How many | onions | did | they | grow | in all | ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in total | ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in all | ? <eos> | Sum | ai2 |

### Top-21 (4 samples using it): (20, 12, 6, 14, 5, 13, 25, 23, 3, 12, 9, 22, 15, 11, 26, 18, 30, 27)
| 20 | 12 | 6 | 14 | 5 | 13 | 25 | 23 | 3 | 12 | 9 | 22 | 15 | 11 | 26 | 18 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | candies | in <PER_1> 's | candy | collection | . If the | candies | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | cards | in <PER_1> 's | <unk> | collection | . If the | cards | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |

### Top-22 (4 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 16, 12, 6, 14, 22, 15, 34, 1, 26, 17, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 17 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | erasers | and <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | erasers | in the | drawer | . How many | erasers | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | and <num> | rulers | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |

### Top-23 (4 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 34, 1, 26, 2, 6, 14, 25, 34, 1, 26, 18, 19, 8, 18, 19, 12, 9, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 34 | 1 | 26 | 2 | 6 | 14 | 25 | 34 | 1 | 26 | 18 | 19 | 8 | 18 | 19 | 12 | 9 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | bushes | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | bushes | today | . How many short | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-24 (3 samples using it): (20, 12, 6, 14, 23, 3, 12, 9, 34, 26, 17, 27)
| 20 | 12 | 6 | 14 | 23 | 3 | 12 | 9 | 34 | 26 | 17 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | cards | . <num> | cards more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | marbles | . <num> | marbles more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | cards | . <num> | cards more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |

### Top-25 (3 samples using it): (20, 12, 4, 14, 32, 24, 34, 26, 31, 8, 27)
| 20 | 12 | 4 | 14 | 32 | 24 | 34 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |

### Top-26 (3 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | pennies | . <PER_2> | has | <num> | pennies | . How many more | pennies | does | <PER_2> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much | <unk> | is | <PER_1> | than <PER_2> | ? <eos> | Subtraction | ilds |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much | <unk> | is | <PER_1> | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-27 (3 samples using it): (20, 12, 6, 14, 34, 1, 26, 31, 8, 29, 2, 29, 2, 6, 14, 27)
| 20 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 29 | 2 | 29 | 2 | 6 | 14 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | dollars | . How many more | dollars | does | she | have | to | <unk> | to | have | <num> | dollars | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | fish | . How many more | fish | does | she | need | to | buy | to | have | <num> | fish | ? <eos> | Subtraction | ilds |

### Top-28 (3 samples using it): (20, 12, 6, 14, 33, 0, 23, 3, 12, 6, 14, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 33 | 0 | 23 | 3 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | crayons | . Each | box | holds | <num> | crayons | . How many | crayons | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | peanuts | . Each | box | holds | <num> | peanuts | . How many | peanuts | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-29 (3 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |

### Top-30 (3 samples using it): (20, 12, 6, 14, 5, 34, 1, 33, 0, 11, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 5 | 34 | 1 | 33 | 0 | 11 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |

### Top-31 (3 samples using it): (20, 12, 6, 14, 16, 12, 4, 25, 11, 1, 26, 18, 19, 30, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 25 | 11 | 1 | 26 | 18 | 19 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | erasers | . If she | shares | them among <num> | friends | , how many | erasers | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | marbles | . If she | shares | them among <num> | friends | , how many | marbles | does | each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-32 (3 samples using it): (20, 12, 6, 14, 16, 12, 4, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | stickers | . She | gets | <num> more | from <PER_2> | . How many | stickers | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | gets | <num> more | from <PER_2> | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | gets | <num> more | from <MISC_1> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-33 (3 samples using it): (20, 12, 4, 14, 16, 12, 4, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 16 | 12 | 4 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | cards | . She | gets | <num> more | from <MISC_1> | . How many | cards | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | oranges | . She | gets | <num> more | from <MISC_1> | . How many | oranges | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bananas | . She | gets | <num> more | from <PER_2> | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-34 (3 samples using it): (20, 12, 6, 14, 5, 11, 33, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 5 | 11 | 33 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup from the | cookie mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup from the | cookie mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup from the | cookie mom | ? <eos> | CommonDiv | ilds |

### Top-35 (3 samples using it): (20, 12, 2, 6, 10, 22, 15, 16, 12, 6, 14, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 2 | 6 | 10 | 22 | 15 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . He | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |

### Top-36 (3 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 16, 12, 6, 14, 34, 1, 26, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-37 (3 samples using it): (20, 12, 6, 14, 25, 11, 12, 4, 14, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 25 | 11 | 12 | 4 | 14 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many orange | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | violet | balloons | , he | gave | <PER_2> <num> of the | balloons | . How many violet | balloons | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | violet | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many violet | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-38 (3 samples using it): (20, 12, 6, 14, 25, 16, 12, 4, 14, 25, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 25 | 16 | 12 | 4 | 14 | 25 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> <PER_3> | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> <PER_3> | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-39 (3 samples using it): (20, 12, 6, 14, 16, 12, 4, 14, 16, 12, 4, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 14 | 16 | 12 | 4 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does | <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does | <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | has | with <num> | cards | . <PER_2> | finds | another <num> | . How many | cards | does | <PER_2> | end | with | ? <eos> | Addition | ilds |

### Top-40 (3 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 6, 14, 5, 11, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 5 | 11 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If there | are | <num> | eggs | in a | box | and <PER_1> | puts | <num> more | eggs | inside | , how many | eggs | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | erasers | in a | box | and <PER_1> | puts | <num> more | erasers | inside | , how many | erasers | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | crayons | in a | box | and <PER_1> | puts | <num> more | crayons | inside | , how many | crayons | are | in the | box | ? <eos> | Addition | ilds |

### Top-41 (3 samples using it): (20, 12, 6, 10, 22, 15, 16, 12, 6, 10, 22, 15, 34, 1, 26, 17, 21, 27)
| 20 | 12 | 6 | 10 | 22 | 15 | 16 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 26 | 17 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in all | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-42 (3 samples using it): (20, 12, 29, 2, 6, 14, 33, 0, 22, 15, 32, 16, 12, 6, 14, 34, 1, 26, 8, 30, 27)
| 20 | 12 | 29 | 2 | 6 | 14 | 33 | 0 | 22 | 15 | 32 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 8 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | erasers | into | groups | of <num> | . <PER_1> | has | <num> | erasers | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | peanuts | into | groups | of <num> | . <PER_1> | has | <num> | peanuts | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-43 (3 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 23, 3, 12, 6, 14, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 23 | 3 | 12 | 6 | 14 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | quarters | in her | bank | . Her | dad | borrowed | <num> | quarters | from <PER_1> | . How many | quarters | does | she | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | quarters | and <num> | nickels | in his | bank | . His | dad | borrowed | <num> | nickels | from <PER_1> | . How many | nickels | does | he | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in her | bank | . Her | dad | borrowed | <num> | nickels | from <PER_1> | . How many | nickels | does | she | have | now | ? <eos> | Subtraction | ai2 |

### Top-44 (3 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 16, 12, 4, 14, 5, 11, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 16 | 12 | 4 | 14 | 5 | 11 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> | has | <num> | pencils | . <PER_1> | has | <num> | pencils | . If <PER_1> | gives | all of her | pencils | to <PER_2> | , how many | pencils | will | <PER_2> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | peanuts | . <PER_2> | has | <num> | peanuts | . If <PER_2> | gives | all of her | peanuts | to <PER_1> | , how many | peanuts | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . If <PER_2> | gives | all of her | crayons | to <PER_1> | , how many | crayons | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-45 (3 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 16, 12, 4, 14, 5, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 16 | 12 | 4 | 14 | 5 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |

### Top-46 (3 samples using it): (20, 12, 6, 14, 33, 0, 23, 3, 12, 6, 14, 16, 12, 6, 14, 22, 15, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 33 | 0 | 23 | 3 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> | has | <num> | boxes | of | tickets | . Each | box | holds | <num> | tickets | and there | are | <num> | boxes | in a | <unk> | . How many | tickets | does | <ORG_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | blocks | . Each | box | holds | <num> | blocks | and there | are | <num> | boxes | in a | <unk> | . How many | blocks | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | eggs | . Each | box | holds | <num> | eggs | and there | are | <num> | boxes | in a | <unk> | . How many | eggs | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-47 (3 samples using it): (20, 12, 6, 14, 25, 32, 13, 25, 16, 12, 4, 14, 25, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 25 | 32 | 13 | 25 | 16 | 12 | 4 | 14 | 25 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-48 (3 samples using it): (20, 12, 6, 14, 16, 12, 4, 16, 12, 6, 14, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | marbles | . He | buys | <num> more | . Later , <PER_1> | buys | <num> | apples | at the | store | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | tickets | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | eggs | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | erasers | at the | store | . How many | eggs | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-49 (3 samples using it): (20, 12, 4, 14, 29, 2, 5, 25, 32, 10, 22, 15, 34, 26, 17, 30, 17, 30, 27)
| 20 | 12 | 4 | 14 | 29 | 2 | 5 | 25 | 32 | 10 | 22 | 15 | 34 | 26 | 17 | 30 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | run | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-50 (3 samples using it): (20, 3, 12, 4, 16, 12, 6, 5, 34, 1, 26, 31, 8, 11, 1, 26, 31, 8, 30, 27)
| 20 | 3 | 12 | 4 | 16 | 12 | 6 | 5 | 34 | 1 | 26 | 31 | 8 | 11 | 1 | 26 | 31 | 8 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> | <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> | <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> | <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |

### Top-51 (3 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 22, 15, 16, 12, 4, 11, 12, 4, 13, 25, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 4 | 11 | 12 | 4 | 13 | 25 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |

### Top-52 (3 samples using it): (20, 12, 6, 28, 10, 22, 15, 34, 1, 26, 2, 6, 14, 13, 25, 34, 1, 26, 18, 19, 8, 18, 19, 12, 9, 27)
| 20 | 12 | 6 | 28 | 10 | 22 | 15 | 34 | 1 | 26 | 2 | 6 | 14 | 13 | 25 | 34 | 1 | 26 | 18 | 19 | 8 | 18 | 19 | 12 | 9 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | . How many dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | . How many orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | <num> | walnut | trees | today | . How many walnut | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-53 (3 samples using it): (20, 12, 5, 25, 16, 12, 6, 14, 5, 25, 5, 25, 16, 12, 4, 14, 29, 2, 5, 34, 26, 31, 8, 27)
| 20 | 12 | 5 | 25 | 16 | 12 | 6 | 14 | 5 | 25 | 5 | 25 | 16 | 12 | 4 | 14 | 29 | 2 | 5 | 34 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get | there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get | there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | jogged | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get | there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |

### Top-54 (3 samples using it): (20, 12, 6, 10, 22, 15, 22, 15, 23, 3, 12, 22, 15, 32, 23, 3, 12, 9, 22, 15, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 10 | 22 | 15 | 22 | 15 | 23 | 3 | 12 | 22 | 15 | 32 | 23 | 3 | 12 | 9 | 22 | 15 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | candies | in a | pile | on the | desk | . Each | candy | comes | in a | package | of <num> | . <num> | candies | are | added | to the | pile | . How many | candies | are | there in the | pile | ? <eos> | Addition | ilds |

### Top-55 (3 samples using it): (20, 12, 6, 14, 29, 2, 7, 9, 22, 15, 16, 12, 29, 2, 29, 2, 6, 14, 29, 2, 5, 16, 12, 6, 14, 11, 1, 26, 9, 22, 15, 27)
| 20 | 12 | 6 | 14 | 29 | 2 | 7 | 9 | 22 | 15 | 16 | 12 | 29 | 2 | 29 | 2 | 6 | 14 | 29 | 2 | 5 | 16 | 12 | 6 | 14 | 11 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-56 (2 samples using it): (20, 3, 12, 4, 34, 26, 18, 19, 8, 27)
| 20 | 3 | 12 | 4 | 34 | 26 | 18 | 19 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do | <num> | bananas | cost | ? <eos> | Multiplication | ilds |
| Each | <unk> | costs | $ <num> | . How much | do | <num> | tickets | cost | ? <eos> | Multiplication | ilds |

### Top-57 (2 samples using it): (20, 3, 12, 6, 14, 34, 1, 26, 18, 19, 8, 27)
| 20 | 3 | 12 | 6 | 14 | 34 | 1 | 26 | 18 | 19 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-58 (2 samples using it): (20, 12, 6, 14, 16, 12, 6, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . She | loses | <num> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-59 (2 samples using it): (20, 12, 6, 14, 32, 14, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 32 | 14 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | birds | and <num> | <unk> | . How many more | birds | are | there than | <unk> | ? <eos> | Subtraction | ilds |
| There | are | <num> | flowers | and <num> | bees | . How many <unk> | bees | are | there than | flowers | ? <eos> | Subtraction | ilds |

### Top-60 (2 samples using it): (20, 12, 6, 14, 22, 15, 34, 1, 26, 31, 8, 17, 30, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | drove | <num> | miles | every | hour | . How many | miles | would | he | drive | in <num> | hours | ? <eos> | Multiplication | ilds |
| <PER_1> | scored | <num> | points | in each | game | . How many | points | did | she | score | in <num> | games | ? <eos> | Multiplication | ilds |

### Top-61 (2 samples using it): (20, 12, 6, 14, 29, 2, 6, 14, 34, 1, 26, 31, 8, 29, 8, 27)
| 20 | 12 | 6 | 14 | 29 | 2 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 29 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much | <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | ran | <num> | miles | and | walked | <num> | miles | . How much | <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-62 (2 samples using it): (20, 12, 6, 14, 16, 12, 6, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | cookies | . <PER_2> | has | <num> | . How many more | cookies | does | <PER_2> | have | than <PER_1> | ? <eos> | Subtraction | ilds |

### Top-63 (2 samples using it): (20, 12, 6, 14, 16, 12, 4, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have | altogether | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have | altogether | ? <eos> | Addition | ilds |

### Top-64 (2 samples using it): (20, 3, 12, 6, 14, 16, 12, 6, 14, 11, 1, 26, 8, 21, 27)
| 20 | 3 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 11 | 1 | 26 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | pencils | . If there | are | <num> | children | , how many | pencils | are | there | in total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | oranges | . If there | are | <num> | children | , how many | oranges | are | there | in total | ? <eos> | Multiplication | ilds |

### Top-65 (2 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | marbles | in his | collection | . He | lost | <num> | marbles | . How many | marbles | does | he | have | now | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | strawberries | in his | <unk> | . He | picked | <num> more | strawberries | . How many | strawberries | did | he | have | then | ? <eos> | Addition | ilds |

### Top-66 (2 samples using it): (20, 12, 4, 14, 25, 16, 12, 6, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 25 | 16 | 12 | 6 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | bottle | caps | . <PER_2> | takes | <num> | away | . How many bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . She | shares | <num> | with <PER_2> | . How many bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-67 (2 samples using it): (20, 12, 4, 14, 16, 12, 9, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 16 | 12 | 9 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | cards | . <num> | are | eaten | by a | hippopotamus | . How many | cards | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . <num> | are | eaten | by a | hippopotamus | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-68 (2 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 22, 15, 34, 1, 26, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 1 | 26 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in all | ? <eos> | Addition | ai2 |

### Top-69 (2 samples using it): (20, 12, 6, 14, 32, 10, 16, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | and <num> | turnips | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | cantelopes | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-70 (2 samples using it): (20, 3, 12, 6, 14, 25, 16, 12, 6, 14, 11, 3, 1, 26, 17, 30, 27)
| 20 | 3 | 12 | 6 | 14 | 25 | 16 | 12 | 6 | 14 | 11 | 3 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-71 (2 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 4, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 4 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | quarters | in her | bank | . She | spent | <num> of her | quarters | . How many | quarters | does | she | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | pennies | in his | bank | . He | spent | <num> of his | pennies | . How many | pennies | does | he | have | now | ? <eos> | Subtraction | ai2 |

### Top-72 (2 samples using it): (20, 12, 4, 14, 25, 16, 12, 4, 5, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 4 | 14 | 25 | 16 | 12 | 4 | 5 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more | from <PER_2> | . How many bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more | from <PER_2> | . How many bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-73 (2 samples using it): (20, 12, 6, 14, 34, 26, 31, 8, 29, 2, 5, 11, 26, 8, 18, 19, 30, 27)
| 20 | 12 | 6 | 14 | 34 | 26 | 31 | 8 | 29 | 2 | 5 | 11 | 26 | 8 | 18 | 19 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> <MISC_1> | games | . How many | does | she | need | to | give | away | so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> <MISC_1> | games | . How many | does | she | need | to | give | away | so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |

### Top-74 (2 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 16, 12, 6, 5, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 16 | 12 | 6 | 5 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . She | shares | <num> | with <PER_3> | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | has | <num> | apples | . He | shares | <num> | with <PER_3> | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-75 (2 samples using it): (20, 12, 6, 14, 9, 22, 15, 23, 3, 26, 2, 6, 14, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 9 | 22 | 15 | 23 | 3 | 26 | 2 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | guests | <unk> | to his | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will | he | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | guests | <unk> | to her <unk> | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will | she | need | ? <eos> | CommonDiv | ilds |

### Top-76 (2 samples using it): (20, 12, 6, 14, 22, 15, 11, 12, 4, 14, 34, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 11 | 12 | 4 | 14 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> <num> of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> <num> of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-77 (2 samples using it): (20, 12, 6, 14, 33, 0, 16, 12, 6, 10, 22, 15, 34, 1, 33, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 33 | 0 | 16 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 33 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-78 (2 samples using it): (20, 12, 6, 14, 32, 14, 16, 12, 6, 14, 25, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 14 | 16 | 12 | 6 | 14 | 25 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blue | and <num> green | balloons | . <PER_2> | has | <num> | blue | balloons | . How many blue | balloons | do | they | have | in all | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | blue | and <num> red | marbles | . <PER_2> | has | <num> | blue | marbles | . How many blue | marbles | do | they | have | in all | ? <eos> | Addition | ai2 |

### Top-79 (2 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 23, 3, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 23 | 3 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | dimes | in his | bank | . His | sister | borrowed | <num> | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | quarters | and <num> | dimes | in her | bank | . Her | sister | borrowed | <num> | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-80 (2 samples using it): (20, 3, 12, 9, 22, 15, 23, 3, 12, 29, 2, 4, 34, 1, 26, 9, 22, 15, 27)
| 20 | 3 | 12 | 9 | 22 | 15 | 23 | 3 | 12 | 29 | 2 | 4 | 34 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | ducks | are | <unk> | in a | lake | . <num> more | ducks | come | to | join | them | . How many | ducks | are | <unk> | in the | lake | ? <eos> | Addition | ilds |
| <num> | birds | were | sitting | on the | fence | . <num> more | birds | <unk> | to | join | them | . How many | birds | are | sitting | on the | fence | ? <eos> | Addition | ilds |

### Top-81 (2 samples using it): (20, 12, 6, 14, 16, 12, 6, 14, 32, 3, 12, 6, 14, 34, 1, 33, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 32 | 3 | 12 | 6 | 14 | 34 | 1 | 33 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <num> | are | about | school | and the | rest | are | about | sports | . How many | books | about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | books | . <num> | are | about | school | and the | rest | are | about | sports | . How many | books | about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-82 (2 samples using it): (20, 3, 12, 6, 14, 32, 13, 25, 16, 12, 4, 14, 34, 1, 26, 17, 30, 27)
| 20 | 3 | 12 | 6 | 14 | 32 | 13 | 25 | 16 | 12 | 4 | 14 | 34 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | dog | had | <num> | puppies | and <num> | had | spots | . She | gave | <num> to her | friends | . How many | puppies | does | she now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> 's | cat | had | <num> | kittens | and <num> | had | spots | . She | gave | <num> to her | friends | . How many | kittens | does | she now | have | ? <eos> | Subtraction | ai2 |

### Top-83 (2 samples using it): (20, 12, 6, 10, 22, 15, 16, 12, 4, 10, 22, 15, 34, 1, 26, 9, 22, 15, 27)
| 20 | 12 | 6 | 10 | 22 | 15 | 16 | 12 | 4 | 10 | 22 | 15 | 34 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes | <num> | pencils | from a | jar | . There | were | originally <num> | pencils | in the | jar | . How many | pencils | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | apples | from a | jar | . There | were | originally <num> | apples | in the | jar | . How many | apples | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-84 (2 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 4, 10, 22, 15, 34, 1, 26, 9, 22, 15, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 4 | 10 | 22 | 15 | 34 | 1 | 26 | 9 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes | <num> | bananas | from a | jar | . There | were | originally <num> | bananas | in the | jar | . How many | bananas | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | eggs | from a | jar | . There | were | originally <num> | eggs | in the | jar | . How many | eggs | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-85 (2 samples using it): (20, 12, 6, 14, 25, 32, 14, 16, 12, 4, 14, 25, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 25 | 32 | 14 | 16 | 12 | 4 | 14 | 25 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | violet | balloons | and <num> red | balloons | . He | lost | <num> of the | violet | balloons | . How many violet | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | orange | balloons | and <num> blue | balloons | . She | lost | <num> of the | orange | balloons | . How many orange | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-86 (2 samples using it): (20, 12, 6, 28, 16, 12, 6, 14, 16, 12, 4, 14, 5, 11, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 28 | 16 | 12 | 6 | 14 | 16 | 12 | 4 | 14 | 5 | 11 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . <PER_2> | has | <num> | <PER_3> | . If <PER_2> | gives | all of his | <MISC_1> | to <PER_1> | , how many | <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | <MISC_1> | . <PER_2> | has | <num> | <PER_3> | . If <PER_2> | gives | all of his | <MISC_1> | to <PER_1> | , how many | <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-87 (2 samples using it): (20, 12, 6, 28, 10, 22, 15, 16, 12, 6, 14, 25, 5, 11, 3, 1, 26, 17, 30, 27)
| 20 | 12 | 6 | 28 | 10 | 22 | 15 | 16 | 12 | 6 | 14 | 25 | 5 | 11 | 3 | 1 | 26 | 17 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If there | are | <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps | inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps | inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |

### Top-88 (2 samples using it): (20, 12, 6, 28, 10, 22, 15, 16, 12, 6, 10, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 28 | 10 | 22 | 15 | 16 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | football | games | this | year | . She | went | to <num> | games | last | year | . How many football | games | did | <PER_1> | go | to in all | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | football | games | this | year | . He | went | to <num> | games | last | year | . How many football | games | did | <PER_1> | go | to in all | ? <eos> | Addition | ai2 |

### Top-89 (2 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 16, 12, 6, 28, 22, 15, 34, 1, 26, 17, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 16 | 12 | 6 | 28 | 22 | 15 | 34 | 1 | 26 | 17 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | scissors | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | rulers | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | rulers | in the | drawer | . How many | rulers | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-90 (2 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 23, 3, 12, 4, 14, 32, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 23 | 3 | 12 | 4 | 14 | 32 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in his | bank | . His | dad | gave | him <num> | nickels | and <num> | quarters | . How many | nickels | does | he | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | quarters | and <num> | nickels | in his | bank | . His | dad | gave | him <num> | nickels | and <num> | pennies | . How many | nickels | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |

### Top-91 (2 samples using it): (20, 3, 12, 2, 6, 14, 25, 16, 12, 6, 14, 32, 10, 22, 15, 25, 34, 1, 26, 2, 29, 2, 18, 30, 27)
| 20 | 3 | 12 | 2 | 6 | 14 | 25 | 16 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 25 | 34 | 1 | 26 | 2 | 29 | 2 | 18 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |

### Top-92 (2 samples using it): (20, 3, 12, 6, 14, 33, 0, 29, 2, 6, 14, 5, 16, 12, 6, 14, 22, 15, 34, 26, 18, 0, 33, 0, 21, 27)
| 20 | 3 | 12 | 6 | 14 | 33 | 0 | 29 | 2 | 6 | 14 | 5 | 16 | 12 | 6 | 14 | 22 | 15 | 34 | 26 | 18 | 0 | 33 | 0 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | <unk> | long | . Then she | <unk> | <num> | <unk> | off the | end | . How long | is | the | piece | of | wood | now | ? <eos> | Subtraction | ai2 |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | centimeters | long | . Then he | <unk> | <num> | centimeters | off the | end | . How long | is | the | piece | of | wood | now | ? <eos> | Subtraction | ai2 |

### Top-93 (2 samples using it): (20, 12, 18, 19, 6, 10, 22, 15, 16, 12, 6, 14, 22, 15, 29, 2, 6, 14, 34, 1, 26, 31, 8, 22, 15, 27)
| 20 | 12 | 18 | 19 | 6 | 10 | 22 | 15 | 16 | 12 | 6 | 14 | 22 | 15 | 29 | 2 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 22 | 15 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |

### Top-94 (2 samples using it): (20, 12, 6, 14, 16, 12, 4, 5, 16, 12, 6, 10, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 16 | 12 | 4 | 5 | 16 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bananas | . He | gets | <num> more | from <MISC_1> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | bananas | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . She | gets | <num> more | from <PER_2> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | crayons | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-95 (2 samples using it): (20, 12, 6, 28, 10, 22, 15, 11, 12, 6, 16, 12, 6, 10, 22, 15, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 28 | 10 | 22 | 15 | 11 | 12 | 6 | 16 | 12 | 6 | 10 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | basketball | games | this | year | , but | missed | <num> | . He | went | to <num> | games | last | year | . How many basketball | games | did | <PER_1> | go | to in total | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | <unk> | games | this | year | , but | missed | <num> | . He | went | to <num> | games | last | year | . How many <unk> | games | did | <PER_1> | go | to in all | ? <eos> | Addition | ai2 |

### Top-96 (2 samples using it): (20, 3, 12, 6, 14, 23, 3, 12, 6, 14, 16, 12, 4, 14, 24, 34, 1, 26, 31, 8, 21, 27)
| 20 | 3 | 12 | 6 | 14 | 23 | 3 | 12 | 6 | 14 | 16 | 12 | 4 | 14 | 24 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a party | . How many | cookies | did | they | have | altogether | ? <eos> | Addition | ilds |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a party | . How many | cookies | did | they | have | altogether | ? <eos> | Addition | ilds |

### Top-97 (2 samples using it): (20, 19, 20, 12, 6, 14, 16, 12, 6, 14, 16, 12, 10, 22, 15, 16, 12, 6, 14, 34, 26, 31, 8, 18, 30, 27)
| 20 | 19 | 20 | 12 | 6 | 14 | 16 | 12 | 6 | 14 | 16 | 12 | 10 | 22 | 15 | 16 | 12 | 6 | 14 | 34 | 26 | 31 | 8 | 18 | 30 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Last | week | <PER_1> | had | <num> | dollars | and <PER_2> | had | <num> | dollars | . <PER_1> | <unk> | cars | over the | weekend | and now | has | <num> | dollars | . How much money | did | <PER_1> | make | <unk> | cars | ? <eos> | Subtraction | ai2 |
| Last | week | <PER_1> | had | <num> | dollars | and <PER_2> | had | <num> | dollars | . <PER_1> | <unk> | cars | over the | weekend | and now | has | <num> | dollars | . How much money | did | <PER_1> | make | <unk> | cars | ? <eos> | Subtraction | ai2 |

### Top-98 (2 samples using it): (20, 12, 6, 14, 32, 10, 22, 15, 16, 12, 4, 14, 16, 12, 6, 14, 34, 1, 26, 31, 8, 21, 27)
| 20 | 12 | 6 | 14 | 32 | 10 | 22 | 15 | 16 | 12 | 4 | 14 | 16 | 12 | 6 | 14 | 34 | 1 | 26 | 31 | 8 | 21 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <PER_2> some of her | seashells | . She | has | <num> | seashell | . How many | seashells | did | she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <PER_2> some of her | seashells | . She | has | <num> | seashell | . How many | seashells | did | she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |

### Top-99 (2 samples using it): (20, 12, 6, 14, 22, 15, 16, 12, 6, 14, 22, 15, 16, 12, 4, 10, 22, 15, 34, 1, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 6 | 14 | 22 | 15 | 16 | 12 | 4 | 10 | 22 | 15 | 34 | 1 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |

### Top-100 (2 samples using it): (20, 12, 6, 14, 22, 15, 25, 15, 16, 12, 18, 19, 29, 2, 14, 29, 2, 5, 16, 12, 4, 14, 11, 26, 31, 8, 27)
| 20 | 12 | 6 | 14 | 22 | 15 | 25 | 15 | 16 | 12 | 18 | 19 | 29 | 2 | 14 | 29 | 2 | 5 | 16 | 12 | 4 | 14 | 11 | 26 | 31 | 8 | 27 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | peaches | at his | <unk> | fruit | dish | . He | went | to the | orchard | and | picked | peaches | to | <unk> | up | . There | are | now <num> | peaches | . how many | did | he | pick | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | peaches | at her | <unk> | fruit | dish | . She | went | to the | orchard | and | picked | peaches | to | <unk> | up | . There | are | now <num> | peaches | . how many | did | she | pick | ? <eos> | Subtraction | ai2 |


