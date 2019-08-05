Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-45-3-war.txt')
# Analysis of segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-45-3-war.txt
k=100
n=10
# Overall - top templates
### Top-1 (32 samples using it): (119, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | loses | <num> | . How many | stickers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | peanuts | . He | loses | <num> | . How many | peanuts | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | blocks | . She | loses | <num> | . How many | blocks | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . She | loses | <num> | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <LOC_1> | starts | with <num> | eggs | . <PER_1> | takes | <num> away | . How many | eggs | does | <LOC_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | <MISC_1> | . She | buys | <num> more | . How many | <MISC_1> | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | crayons | . <PER_2> | takes | <num> away | . How many | crayons | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-2 (14 samples using it): (119, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . She | loses | <num> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <PER_2> | . <PER_3> | takes | <num> away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | takes | <num> away | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <MISC_1> | . She | gives | <num> to <MISC_2> | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | bananas | . She | shares | <num> with <MISC_1> | . How many | bananas | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (10 samples using it): (119, 38, 31, 26, 118, 108, 8, 7, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 118 | 108 | 8 | 7 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | walked | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| If <PER_1> | <unk> | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (10 samples using it): (119, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | oranges | . He | finds | another <num> | . How many | oranges | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . She | buys | <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | tickets | . <PER_2> | gives | <PER_1> <num> more | . How many | tickets | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | pencils | . <PER_2> | gives | <PER_1> <num> more | . How many | pencils | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . <PER_2> | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | stickers | . She | gets | <num> more from <PER_2> | . How many | stickers | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | gets | <num> more from <PER_2> | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | gets | <num> more from <MISC_1> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-5 (7 samples using it): (119, 38, 31, 26, 28, 48, 53, 130, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 53 | 130 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (7 samples using it): (119, 38, 31, 26, 99, 60, 57, 9, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 9 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . She | buys | <num> more | . Later , <PER_1> | buys | <num> | oranges | at the | store | . How many | <MISC_1> | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | buys | <num> more | . Later , <PER_1> | buys | <num> | apples | at the | store | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | tickets | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | eggs | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | erasers | at the | store | . How many | eggs | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | gets | <num> more from <PER_2> | . Later , <PER_1> | buys | <num> | crayons | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bananas | . He | gets | <num> more from <MISC_1> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | bananas | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . She | gets | <num> more from <PER_2> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | crayons | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-7 (6 samples using it): (119, 38, 31, 26, 54, 84, 60, 57, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 84 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | candies | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | cards | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | cards | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | peanuts | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-8 (6 samples using it): (119, 38, 31, 26, 28, 48, 9, 15, 76, 48, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | and <num> | watermelons | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | turnips | and <num> | pumpkins | . <MISC_1> | grew | <num> | turnips | . How many | turnips | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | and <num> | turnips | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | turnips | . <ORG_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | cantelopes | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | pumpkins | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-9 (6 samples using it): (119, 38, 31, 26, 28, 48, 11, 24, 9, 15, 76, 48, 101, 114, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | and <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in all | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | and <num> | rulers | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | scissors | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | rulers | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | rulers | in the | drawer | . How many | rulers | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-10 (5 samples using it): (119, 38, 31, 26, 9, 15, 76, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many more | books | does | <PER_1> | have | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-11 (5 samples using it): (119, 38, 31, 26, 9, 15, 76, 48, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | cantelopes | . <PER_2> | grew | <num> | cantelopes | . How many | cantelopes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <ORG_1> | grew | <num> | potatoes | . <PER_1> | grew | <num> | potatoes | . How many | potatoes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | pumpkins | . <PER_2> | grew | <num> | pumpkins | . How many | pumpkins | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-12 (5 samples using it): (119, 38, 31, 26, 50, 99, 60, 57, 85, 117, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 50 | 99 | 60 | 57 | 85 | 117 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . She | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-13 (5 samples using it): (119, 38, 31, 26, 50, 99, 60, 57, 85, 117, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 50 | 99 | 60 | 57 | 85 | 117 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | bottle | caps | . She | finds | another <num> | . How many | bottle | caps | does | <ORG_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . <PER_2> | takes | <num> away | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . She | shares | <num> with <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more from <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more from <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-14 (5 samples using it): (119, 38, 31, 26, 11, 24, 28, 48, 54, 84, 126, 80, 101, 114, 7, 70, 123, 109, 82, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 28 | 48 | 54 | 84 | 126 | 80 | 101 | 114 | 7 | 70 | 123 | 109 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | students | in the | class | and <num> | eggs | . If the | eggs | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | pencils | . If the | pencils | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | apples | . If the | apples | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |

### Top-15 (5 samples using it): (119, 38, 31, 26, 89, 24, 54, 38, 31, 26, 89, 24, 9, 15, 76, 48, 101, 114, 85, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 54 | 38 | 31 | 26 | 89 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | candies | in a | box | . <PER_1> | has | <num> | candies | in a | bag | . <PER_2> | takes | <num> | candies | out of the | box | . How many | candies | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | has | <num> | oranges | in a | bag | . <PER_2> | takes | <num> | oranges | out of the | box | . How many | oranges | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | apples | in a | box | . <PER_1> | has | <num> | apples | in a | bag | . <PER_2> | takes | <num> | apples | out of the | box | . How many | apples | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-16 (5 samples using it): (119, 38, 31, 26, 22, 84, 126, 80, 11, 24, 54, 105, 67, 80, 22, 15, 76, 48, 67, 80, 75, 9, 15, 76, 48, 52, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 22 | 84 | 126 | 80 | 11 | 24 | 54 | 105 | 67 | 80 | 22 | 15 | 76 | 48 | 67 | 80 | 75 | 9 | 15 | 76 | 48 | 52 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-17 (4 samples using it): (119, 38, 31, 26, 89, 24, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | crayons | in each | box | . How many | crayons | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-18 (4 samples using it): (119, 38, 31, 26, 73, 53, 130, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 73 | 53 | 130 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> miles | per hour | . How long | did | <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |

### Top-19 (4 samples using it): (119, 38, 31, 26, 11, 24, 9, 15, 76, 48, 85, 124, 35, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 9 | 15 | 76 | 48 | 85 | 124 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | eggs | in a | box | . <PER_1> | takes | <num> | eggs | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | pencils | in a | box | . <PER_1> | takes | <num> | pencils | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-20 (4 samples using it): (119, 38, 31, 26, 54, 126, 80, 101, 114, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 126 | 80 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <num> | are | eaten | by a | hippopotamus | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | crayons | . <num> | are | eaten | by a | hippopotamus | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-21 (4 samples using it): (119, 38, 31, 26, 30, 85, 18, 28, 48, 97, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 30 | 85 | 18 | 28 | 48 | 97 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <MISC_1> <MISC_2> <MISC_3> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |

### Top-22 (4 samples using it): (119, 38, 31, 26, 99, 60, 57, 51, 97, 66, 70, 123, 109, 82, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 97 | 66 | 70 | 123 | 109 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | erasers | . If she | shares | them among <num> | friends | , how many | erasers | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | marbles | . If she | shares | them among <num> | friends | , how many | marbles | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | tickets | . If she | shares | them among <num> | friends | , how many | tickets | does | each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-23 (4 samples using it): (119, 38, 31, 26, 54, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | eggs | . <PER_2> | has | <num> | eggs | . He | loses | <num> | . How many | eggs | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <MISC_1> | . <PER_2> | has | <num> | <MISC_1> | . He | loses | <num> | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . She | shares | <num> with <PER_3> | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | has | <num> | apples | . He | shares | <num> with <PER_3> | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-24 (4 samples using it): (119, 38, 31, 26, 80, 59, 24, 9, 15, 76, 48, 52, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 80 | 59 | 24 | 9 | 15 | 76 | 48 | 52 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | blocks | stored | in | boxes | . If there | are | <num> | boxes | , how many | blocks | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-25 (4 samples using it): (119, 38, 31, 26, 11, 24, 9, 15, 76, 48, 101, 114, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are | <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in all | ? <eos> | Addition | ai2 |
| There | are | <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-26 (4 samples using it): (119, 38, 31, 26, 11, 24, 9, 15, 76, 48, 101, 114, 85, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes | <num> | pencils | from a | jar | . There | were | originally <num> | pencils | in the | jar | . How many | pencils | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | apples | from a | jar | . There | were | originally <num> | apples | in the | jar | . How many | apples | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | bananas | from a | jar | . There | were | originally <num> | bananas | in the | jar | . How many | bananas | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | eggs | from a | jar | . There | were | originally <num> | eggs | in the | jar | . How many | eggs | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-27 (4 samples using it): (119, 38, 31, 26, 67, 80, 30, 51, 28, 48, 46, 18, 130, 70, 123, 82, 14, 100, 62)
| 119 | 38 | 31 | 26 | 67 | 80 | 30 | 51 | 28 | 48 | 46 | 18 | 130 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | run | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | ride | to <LOC_1> <LOC_2> | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> <PER_2> | house | and <PER_3> 's | house | ? <eos> | Multiplication | ilds |

### Top-28 (4 samples using it): (119, 38, 31, 26, 28, 48, 101, 114, 54, 20, 86, 15, 76, 48, 51, 40, 66, 70, 123, 109, 82, 56, 43, 124, 35, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 101 | 114 | 54 | 20 | 86 | 15 | 76 | 48 | 51 | 40 | 66 | 70 | 123 | 109 | 82 | 56 | 43 | 124 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | bushes | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | bushes | today | . How many short | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-29 (3 samples using it): (119, 38, 31, 26, 54, 20, 86, 126, 80, 85, 124, 35, 62)
| 119 | 38 | 31 | 26 | 54 | 20 | 86 | 126 | 80 | 85 | 124 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | cards | . <num> | cards | more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | marbles | . <num> | marbles | more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | cards | . <num> | cards | more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |

### Top-30 (3 samples using it): (119, 38, 31, 26, 40, 66, 70, 123, 82, 112, 35, 112, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 40 | 66 | 70 | 123 | 82 | 112 | 35 | 112 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | dollars | . How many more | dollars | does | she | have | to | <unk> | to | have | <num> | dollars | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | fish | . How many more | fish | does | she | need | to | buy | to | have | <num> | fish | ? <eos> | Subtraction | ilds |

### Top-31 (3 samples using it): (119, 38, 31, 26, 99, 60, 57, 51, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have | altogether | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have | altogether | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> pet | fish | . She | bought | <num> more | fish | . How many pet | fish | does | <PER_1> | have | now | ? <eos> | Addition | ilds |

### Top-32 (3 samples using it): (119, 38, 31, 26, 46, 18, 54, 4, 15, 76, 48, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 46 | 18 | 54 | 4 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | crayons | . Each | box | holds | <num> | crayons | . How many | crayons | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | peanuts | . Each | box | holds | <num> | peanuts | . How many | peanuts | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-33 (3 samples using it): (119, 38, 31, 26, 42, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 42 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |

### Top-34 (3 samples using it): (119, 38, 31, 26, 54, 126, 80, 101, 114, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 54 | 126 | 80 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | <MISC_1> | . <num> | are | eaten | by a | hippopotamus | . How many | <MISC_1> | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | cards | . <num> | are | eaten | by a | hippopotamus | . How many | cards | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . <num> | are | eaten | by a | hippopotamus | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-35 (3 samples using it): (119, 38, 31, 26, 42, 15, 76, 48, 101, 114, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 42 | 15 | 76 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | <unk> | and <PER_2> | picked | <num> | <unk> | from the <unk> | tree | . How many | <unk> | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-36 (3 samples using it): (119, 38, 31, 26, 30, 7, 1, 66, 70, 123, 82, 14, 100, 62)
| 119 | 38 | 31 | 26 | 30 | 7 | 1 | 66 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> | pickup | from the cookie | mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> | pickup | from the cookie | mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> | pickup | from the cookie | mom | ? <eos> | CommonDiv | ilds |

### Top-37 (3 samples using it): (119, 4, 15, 76, 48, 11, 24, 9, 15, 76, 48, 40, 66, 70, 123, 82, 62)
| 119 | 4 | 15 | 76 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . He | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |

### Top-38 (3 samples using it): (119, 38, 31, 26, 42, 38, 31, 26, 9, 15, 76, 48, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 9 | 15 | 76 | 48 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in all | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-39 (3 samples using it): (119, 38, 31, 26, 50, 87, 60, 57, 51, 85, 117, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 50 | 87 | 60 | 57 | 51 | 85 | 117 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many | orange | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | violet | balloons | , he | gave | <PER_2> <num> of the | balloons | . How many | violet | balloons | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | violet | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many | violet | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-40 (3 samples using it): (119, 38, 31, 26, 50, 99, 60, 57, 51, 114, 85, 117, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 50 | 99 | 60 | 57 | 51 | 114 | 85 | 117 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-41 (3 samples using it): (119, 38, 31, 26, 54, 38, 31, 26, 99, 60, 57, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 54 | 38 | 31 | 26 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does | <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does | <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | has | with <num> | cards | . <PER_2> | finds | another <num> | . How many | cards | does | <PER_2> | end | with | ? <eos> | Addition | ilds |

### Top-42 (3 samples using it): (119, 38, 31, 26, 89, 24, 9, 15, 76, 48, 30, 97, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 9 | 15 | 76 | 48 | 30 | 97 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If there | are | <num> | eggs | in a | box | and <PER_1> | puts | <num> more | eggs | inside | , how many | eggs | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | erasers | in a | box | and <PER_1> | puts | <num> more | erasers | inside | , how many | erasers | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | crayons | in a | box | and <PER_1> | puts | <num> more | crayons | inside | , how many | crayons | are | in the | box | ? <eos> | Addition | ilds |

### Top-43 (3 samples using it): (119, 38, 31, 26, 42, 38, 31, 26, 42, 15, 76, 48, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 42 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | onions | , <PER_2> | grew | <num> | onions | , and <PER_3> | grew | <num> | onions | . How many | onions | did | they | grow | in all | ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in total | ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in all | ? <eos> | Sum | ai2 |

### Top-44 (3 samples using it): (119, 38, 31, 26, 75, 72, 69, 54, 84, 126, 80, 101, 114, 7, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 75 | 72 | 69 | 54 | 84 | 126 | 80 | 101 | 114 | 7 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | cards | in <PER_1> 's | <unk> | collection | . If the | cards | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |

### Top-45 (3 samples using it): (119, 105, 22, 15, 76, 48, 46, 18, 46, 18, 73, 9, 15, 76, 48, 40, 66, 70, 123, 82, 62)
| 119 | 105 | 22 | 15 | 76 | 48 | 46 | 18 | 46 | 18 | 73 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | erasers | into | groups | of <num> | . <PER_1> | has | <num> | erasers | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | peanuts | into | groups | of <num> | . <PER_1> | has | <num> | peanuts | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-46 (3 samples using it): (119, 38, 31, 26, 54, 38, 31, 26, 99, 60, 57, 51, 30, 97, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 30 | 97 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> | has | <num> | pencils | . <PER_1> | has | <num> | pencils | . If <PER_1> | gives | all of her | pencils | to <PER_2> | , how many | pencils | will | <PER_2> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | peanuts | . <PER_2> | has | <num> | peanuts | . If <PER_2> | gives | all of her | peanuts | to <PER_1> | , how many | peanuts | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . If <PER_2> | gives | all of her | crayons | to <PER_1> | , how many | crayons | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-47 (3 samples using it): (119, 38, 31, 26, 28, 48, 11, 24, 99, 60, 57, 51, 30, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 11 | 24 | 99 | 60 | 57 | 51 | 30 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |

### Top-48 (3 samples using it): (119, 38, 31, 26, 50, 42, 126, 80, 99, 60, 57, 51, 114, 85, 117, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 50 | 42 | 126 | 80 | 99 | 60 | 57 | 51 | 114 | 85 | 117 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-49 (3 samples using it): (119, 38, 31, 26, 28, 48, 89, 24, 54, 4, 15, 76, 48, 28, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 89 | 24 | 54 | 4 | 15 | 76 | 48 | 28 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in his | bank | . His | dad | gave | him <num> | nickels | and <num> | quarters | . How many | nickels | does | he | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | quarters | and <num> | nickels | in his | bank | . His | dad | gave | him <num> | nickels | and <num> | pennies | . How many | nickels | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | pennies | and <num> | dimes | in his | bank | . His | dad | gave | him <num> | dimes | and <num> | nickels | . How many | dimes | does | he | have | now | ? <eos> | Addition | ai2 |

### Top-50 (3 samples using it): (119, 84, 105, 59, 99, 60, 57, 40, 66, 70, 123, 82, 97, 66, 70, 123, 109, 100, 62)
| 119 | 84 | 105 | 59 | 99 | 60 | 57 | 40 | 66 | 70 | 123 | 82 | 97 | 66 | 70 | 123 | 109 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |

### Top-51 (3 samples using it): (119, 38, 31, 26, 42, 38, 31, 26, 11, 24, 54, 105, 75, 87, 20, 86, 126, 80, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 11 | 24 | 54 | 105 | 75 | 87 | 20 | 86 | 126 | 80 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |

### Top-52 (3 samples using it): (119, 38, 31, 26, 50, 11, 24, 54, 20, 86, 15, 76, 48, 50, 51, 85, 117, 66, 70, 123, 109, 82, 56, 43, 124, 35, 62)
| 119 | 38 | 31 | 26 | 50 | 11 | 24 | 54 | 20 | 86 | 15 | 76 | 48 | 50 | 51 | 85 | 117 | 66 | 70 | 123 | 109 | 82 | 56 | 43 | 124 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | . How many | orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | <num> | walnut | trees | today | . How many | walnut | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-53 (3 samples using it): (119, 38, 75, 24, 9, 15, 76, 48, 30, 51, 30, 51, 9, 15, 76, 48, 67, 80, 130, 70, 123, 82, 62)
| 119 | 38 | 75 | 24 | 9 | 15 | 76 | 48 | 30 | 51 | 30 | 51 | 9 | 15 | 76 | 48 | 67 | 80 | 130 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | to <LOC_1> <LOC_2> | house | . It | is | <num> | miles | from <PER_1> 's | house | to <LOC_1> <LOC_2> | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |

### Top-54 (3 samples using it): (119, 38, 31, 26, 89, 24, 11, 24, 54, 84, 105, 11, 24, 73, 54, 84, 126, 80, 101, 114, 85, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 11 | 24 | 54 | 84 | 105 | 11 | 24 | 73 | 54 | 84 | 126 | 80 | 101 | 114 | 85 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there | in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there | in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | candies | in a | pile | on the | desk | . Each | candy | comes | in a | package | of <num> | . <num> | candies | are | added | to the | pile | . How many | candies | are | there | in the | pile | ? <eos> | Addition | ilds |

### Top-55 (2 samples using it): (119, 84, 60, 57, 130, 70, 123, 109, 82, 62)
| 119 | 84 | 60 | 57 | 130 | 70 | 123 | 109 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do | <num> | bananas | cost | ? <eos> | Multiplication | ilds |
| Each | <unk> | costs | $ <num> | . How much | do | <num> | tickets | cost | ? <eos> | Multiplication | ilds |

### Top-56 (2 samples using it): (119, 4, 15, 76, 48, 40, 66, 70, 123, 109, 82, 62)
| 119 | 4 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 109 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-57 (2 samples using it): (119, 38, 31, 26, 28, 48, 85, 71, 124, 35, 14, 100, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 85 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | birds | and <num> | <unk> | . How many more | birds | are | there | than | <unk> | ? <eos> | Subtraction | ilds |
| There | are | <num> | flowers | and <num> | bees | . How many <unk> | bees | are | there | than | flowers | ? <eos> | Subtraction | ilds |

### Top-58 (2 samples using it): (119, 38, 31, 26, 42, 15, 76, 48, 130, 70, 123, 82, 14, 100, 62)
| 119 | 38 | 31 | 26 | 42 | 15 | 76 | 48 | 130 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | ran | <num> | miles | and | walked | <num> | miles | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-59 (2 samples using it): (119, 38, 31, 26, 9, 15, 76, 48, 130, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 9 | 15 | 76 | 48 | 130 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much <unk> | is | <PER_1> | than <PER_2> | ? <eos> | Subtraction | ilds |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much <unk> | is | <PER_1> | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-60 (2 samples using it): (119, 38, 31, 26, 99, 60, 57, 51, 132, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 132 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does | <PER_2> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does | <PER_2> | have | ? <eos> | Subtraction | ilds |

### Top-61 (2 samples using it): (119, 38, 31, 26, 54, 4, 15, 76, 48, 85, 93, 1, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 4 | 15 | 76 | 48 | 85 | 93 | 1 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <num> | pizzas | . Each | pizza | has | <num> | slices | . How many | slices | of | pizza | are | there | altogether | ? <eos> | Multiplication | ilds |
| Mrs. <PER_1> | bought | <num> | pizzas | . Each | pizza | had | <num> | slices | . How many total | slices | of | pizza | did | she | have | ? <eos> | Multiplication | ilds |

### Top-62 (2 samples using it): (119, 4, 15, 76, 48, 9, 15, 76, 48, 52, 71, 124, 35, 134, 62)
| 119 | 4 | 15 | 76 | 48 | 9 | 15 | 76 | 48 | 52 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | pencils | . If there | are | <num> | children | , how many | pencils | are | there | in total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | oranges | . If there | are | <num> | children | , how many | oranges | are | there | in total | ? <eos> | Multiplication | ilds |

### Top-63 (2 samples using it): (119, 38, 31, 26, 54, 38, 31, 26, 89, 24, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 54 | 38 | 31 | 26 | 89 | 24 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | <unk> | . There | are | <num> | apples | in each | <unk> | . How many | apples | are | there | in all | ? <eos> | Multiplication | ilds |
| <LOC_1> | has | <num> elementary | schools | . There | are | <num> | students | in each | school | . How many elementary | students | are | there altogether | in <LOC_1> | ? <eos> | Multiplication | ilds |

### Top-64 (2 samples using it): (119, 38, 31, 26, 89, 24, 9, 15, 76, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | marbles | in his | collection | . He | lost | <num> | marbles | . How many | marbles | does | he | have | now | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | strawberries | in his | <unk> | . He | picked | <num> more | strawberries | . How many | strawberries | did | he | have | then | ? <eos> | Addition | ilds |

### Top-65 (2 samples using it): (119, 38, 31, 26, 54, 20, 86, 84, 126, 80, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 20 | 86 | 84 | 126 | 80 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | shirts | . <num> | are | blue the | rest | are | green | . How many green | shirts | does | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | balloons | . <num> | balloons | are red and the | rest | are | green | . How many green | balloons | does | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-66 (2 samples using it): (119, 4, 15, 76, 48, 51, 9, 15, 76, 48, 52, 117, 66, 70, 123, 82, 62)
| 119 | 4 | 15 | 76 | 48 | 51 | 9 | 15 | 76 | 48 | 52 | 117 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-67 (2 samples using it): (119, 38, 31, 26, 89, 24, 54, 4, 15, 76, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 89 | 24 | 54 | 4 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | quarters | in his | bank | . His | dad | gave | him <num> | quarters | . How many | quarters | does | he | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | dimes | in his | bank | . His | dad | gave | him <num> | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |

### Top-68 (2 samples using it): (119, 38, 31, 26, 11, 24, 54, 4, 15, 76, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 54 | 4 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | nickels | in her | bank | . Her | dad | gave | her <num> | nickels | . How many | nickels | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | quarters | in her | bank | . Her | dad | gave | her <num> | quarters | . How many | quarters | does | she | have | now | ? <eos> | Addition | ai2 |

### Top-69 (2 samples using it): (119, 38, 31, 26, 46, 18, 28, 48, 46, 18, 85, 93, 1, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 46 | 18 | 28 | 48 | 46 | 18 | 85 | 93 | 1 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | bought | <num> | pounds | of | peanuts | and <num> | pounds | of | raisins | . How many | pounds | of | <unk> | did | she | buy | in all | ? <eos> | Addition | ai2 |
| <PER_1> 's <unk> <unk> | bought | <num> | pound | of green | <unk> | and <num> | pound | of red | <unk> | . How many | pounds | of | <unk> | did | <PER_1> 's | <unk> <unk> buy | in all | ? <eos> | Addition | ai2 |

### Top-70 (2 samples using it): (119, 38, 31, 26, 50, 130, 70, 123, 82, 67, 80, 75, 86, 4, 15, 76, 48, 100, 62)
| 119 | 38 | 31 | 26 | 50 | 130 | 70 | 123 | 82 | 67 | 80 | 75 | 86 | 4 | 15 | 76 | 48 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | games | . How many | does | she | need | to | give | away | so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <MISC_1> | games | . How many | does | she | need | to | give | away | so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |

### Top-71 (2 samples using it): (119, 38, 31, 26, 80, 11, 24, 54, 20, 86, 15, 76, 48, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 80 | 11 | 24 | 54 | 20 | 86 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | guests | <unk> | to his | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will | he | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | guests | <unk> | to her <unk> | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will | she | need | ? <eos> | CommonDiv | ilds |

### Top-72 (2 samples using it): (119, 38, 31, 26, 11, 24, 87, 60, 57, 51, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 87 | 60 | 57 | 51 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> <num> of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> <num> of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-73 (2 samples using it): (119, 38, 31, 26, 46, 18, 9, 15, 76, 48, 101, 114, 85, 93, 1, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 46 | 18 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 93 | 1 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-74 (2 samples using it): (119, 84, 126, 80, 11, 24, 54, 84, 105, 67, 80, 30, 85, 71, 124, 35, 14, 100, 62)
| 119 | 84 | 126 | 80 | 11 | 24 | 54 | 84 | 105 | 67 | 80 | 30 | 85 | 71 | 124 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | ducks | are | <unk> | in a | lake | . <num> more | ducks | come | to | join | them | . How many | ducks | are | <unk> | in the | lake | ? <eos> | Addition | ilds |
| <num> | birds | were | sitting | on the | fence | . <num> more | birds | <unk> | to | join | them | . How many | birds | are | sitting | on the | fence | ? <eos> | Addition | ilds |

### Top-75 (2 samples using it): (119, 38, 31, 26, 54, 105, 11, 24, 42, 4, 15, 76, 48, 85, 93, 1, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 105 | 11 | 24 | 42 | 4 | 15 | 76 | 48 | 85 | 93 | 1 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <num> | are | about | school | and the | rest | are | about | sports | . How many | books | about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | books | . <num> | are | about | school | and the | rest | are | about | sports | . How many | books | about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-76 (2 samples using it): (119, 84, 38, 31, 26, 118, 81, 26, 99, 60, 57, 51, 40, 66, 70, 123, 82, 62)
| 119 | 84 | 38 | 31 | 26 | 118 | 81 | 26 | 99 | 60 | 57 | 51 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | dog | had | <num> | puppies | and <num> | had | spots | . She | gave | <num> to her | friends | . How many | puppies | does | she now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> 's | cat | had | <num> | kittens | and <num> | had | spots | . She | gave | <num> to her | friends | . How many | kittens | does | she now | have | ? <eos> | Subtraction | ai2 |

### Top-77 (2 samples using it): (119, 38, 31, 26, 28, 48, 101, 114, 54, 4, 15, 76, 48, 30, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 101 | 114 | 54 | 4 | 15 | 76 | 48 | 30 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | quarters | in her | bank | . Her | dad | borrowed | <num> | quarters | from <PER_1> | . How many | quarters | does | she | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in her | bank | . Her | dad | borrowed | <num> | nickels | from <PER_1> | . How many | nickels | does | she | have | now | ? <eos> | Subtraction | ai2 |

### Top-78 (2 samples using it): (119, 38, 31, 26, 54, 38, 31, 26, 99, 60, 57, 48, 30, 97, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 54 | 38 | 31 | 26 | 99 | 60 | 57 | 48 | 30 | 97 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . <PER_2> | has | <num> | <PER_3> | . If <PER_2> | gives | all of his | <MISC_1> | to <PER_1> | , how many | <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | <MISC_1> | . <PER_2> | has | <num> | <PER_3> | . If <PER_2> | gives | all of his | <MISC_1> | to <PER_1> | , how many | <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-79 (2 samples using it): (119, 38, 31, 26, 50, 11, 24, 9, 15, 76, 48, 51, 30, 52, 117, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 50 | 11 | 24 | 9 | 15 | 76 | 48 | 51 | 30 | 52 | 117 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If there | are | <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps | inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |
| If there | are | <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps | inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |

### Top-80 (2 samples using it): (119, 38, 31, 26, 50, 11, 24, 9, 15, 76, 48, 46, 18, 85, 117, 66, 70, 123, 82, 112, 134, 62)
| 119 | 38 | 31 | 26 | 50 | 11 | 24 | 9 | 15 | 76 | 48 | 46 | 18 | 85 | 117 | 66 | 70 | 123 | 82 | 112 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | football | games | this | year | . She | went | to <num> | games | last | year | . How many | football | games | did | <PER_1> | go | to | in all | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | football | games | this | year | . He | went | to <num> | games | last | year | . How many | football | games | did | <PER_1> | go | to | in all | ? <eos> | Addition | ai2 |

### Top-81 (2 samples using it): (119, 38, 31, 26, 46, 18, 54, 4, 15, 76, 48, 42, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 46 | 18 | 54 | 4 | 15 | 76 | 48 | 42 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | blocks | . Each | box | holds | <num> | blocks | and there | are | <num> | boxes | in a | <unk> | . How many | blocks | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | eggs | . Each | box | holds | <num> | eggs | and there | are | <num> | boxes | in a | <unk> | . How many | eggs | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-82 (2 samples using it): (119, 20, 86, 15, 76, 48, 51, 54, 38, 31, 26, 28, 48, 101, 114, 51, 85, 71, 124, 35, 112, 35, 14, 100, 62)
| 119 | 20 | 86 | 15 | 76 | 48 | 51 | 54 | 38 | 31 | 26 | 28 | 48 | 101 | 114 | 51 | 85 | 71 | 124 | 35 | 112 | 35 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |

### Top-83 (2 samples using it): (119, 4, 15, 76, 48, 46, 18, 22, 15, 76, 48, 30, 9, 15, 76, 48, 101, 114, 85, 15, 76, 48, 46, 18, 112, 62)
| 119 | 4 | 15 | 76 | 48 | 46 | 18 | 22 | 15 | 76 | 48 | 30 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 15 | 76 | 48 | 46 | 18 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | <unk> | long | . Then she | <unk> | <num> | <unk> | off the | end | . How long | is | the | piece | of | wood | now | ? <eos> | Subtraction | ai2 |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | centimeters | long | . Then he | <unk> | <num> | centimeters | off the | end | . How long | is | the | piece | of | wood | now | ? <eos> | Subtraction | ai2 |

### Top-84 (2 samples using it): (119, 38, 31, 26, 76, 48, 46, 18, 9, 15, 76, 48, 75, 84, 126, 80, 101, 114, 40, 66, 70, 123, 82, 14, 100, 62)
| 119 | 38 | 31 | 26 | 76 | 48 | 46 | 18 | 9 | 15 | 76 | 48 | 75 | 84 | 126 | 80 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |

### Top-85 (2 samples using it): (119, 38, 31, 26, 50, 46, 18, 87, 60, 57, 9, 15, 76, 48, 46, 18, 85, 117, 66, 70, 123, 82, 112, 134, 62)
| 119 | 38 | 31 | 26 | 50 | 46 | 18 | 87 | 60 | 57 | 9 | 15 | 76 | 48 | 46 | 18 | 85 | 117 | 66 | 70 | 123 | 82 | 112 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | basketball | games | this | year | , but | missed | <num> | . He | went | to <num> | games | last | year | . How many | basketball | games | did | <PER_1> | go | to | in total | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | <unk> | games | this | year | , but | missed | <num> | . He | went | to <num> | games | last | year | . How many | <unk> | games | did | <PER_1> | go | to | in all | ? <eos> | Addition | ai2 |

### Top-86 (2 samples using it): (119, 84, 38, 31, 26, 54, 84, 38, 31, 26, 99, 60, 57, 51, 101, 114, 40, 66, 70, 123, 82, 112, 62)
| 119 | 84 | 38 | 31 | 26 | 54 | 84 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a | party | . How many | cookies | did | they | have | altogether | ? <eos> | Addition | ilds |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a | party | . How many | cookies | did | they | have | altogether | ? <eos> | Addition | ilds |

### Top-87 (2 samples using it): (119, 20, 86, 38, 31, 26, 42, 38, 31, 26, 54, 105, 50, 11, 24, 42, 15, 76, 48, 130, 70, 123, 82, 14, 100, 62)
| 119 | 20 | 86 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 54 | 105 | 50 | 11 | 24 | 42 | 15 | 76 | 48 | 130 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Last | week | <PER_1> | had | <num> | dollars | and <PER_2> | had | <num> | dollars | . <PER_1> | <unk> | cars | over the | weekend | and now | has | <num> | dollars | . How much money | did | <PER_1> | make | <unk> | cars | ? <eos> | Subtraction | ai2 |
| Last | week | <PER_1> | had | <num> | dollars | and <PER_2> | had | <num> | dollars | . <PER_1> | <unk> | cars | over the | weekend | and now | has | <num> | dollars | . How much money | did | <PER_1> | make | <unk> | cars | ? <eos> | Subtraction | ai2 |

### Top-88 (2 samples using it): (119, 38, 31, 26, 28, 48, 11, 24, 99, 60, 57, 51, 9, 15, 76, 48, 40, 66, 70, 123, 82, 112, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 11 | 24 | 99 | 60 | 57 | 51 | 9 | 15 | 76 | 48 | 40 | 66 | 70 | 123 | 82 | 112 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <PER_2> some of her | seashells | . She | has | <num> | seashell | . How many | seashells | did | she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <PER_2> some of her | seashells | . She | has | <num> | seashell | . How many | seashells | did | she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |

### Top-89 (2 samples using it): (119, 38, 31, 26, 11, 24, 9, 15, 76, 48, 11, 24, 9, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 9 | 15 | 76 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |

### Top-90 (2 samples using it): (119, 38, 31, 26, 101, 114, 51, 69, 54, 105, 11, 24, 67, 80, 50, 67, 80, 59, 9, 15, 76, 48, 130, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 101 | 114 | 51 | 69 | 54 | 105 | 11 | 24 | 67 | 80 | 50 | 67 | 80 | 59 | 9 | 15 | 76 | 48 | 130 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | peaches | at his | <unk> | fruit | dish | . He | went | to the | orchard | and | picked | peaches | to | <unk> | up | . There | are | now <num> | peaches | . how many | did | he | pick | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | peaches | at her | <unk> | fruit | dish | . She | went | to the | orchard | and | picked | peaches | to | <unk> | up | . There | are | now <num> | peaches | . how many | did | she | pick | ? <eos> | Subtraction | ai2 |

### Top-91 (2 samples using it): (119, 38, 31, 26, 42, 38, 31, 26, 42, 38, 31, 26, 99, 60, 57, 51, 101, 114, 40, 66, 70, 123, 82, 134, 62)
| 119 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 42 | 38 | 31 | 26 | 99 | 60 | 57 | 51 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | onions | , <PER_2> | grew | <num> | onions | , and <PER_3> | grew | <num> | onions | . They | worked | for <num> | days | on the | farm | . How many | onions | did | they | grow | in total | ? <eos> | Sum | ai2 |
| <PER_1> | grew | <num> | pumpkins | , <PER_2> | grew | <num> | pumpkins | , and <PER_3> | grew | <num> | pumpkins | . They | worked | for <num> | days | on the | farm | . How many | pumpkins | did | they | grow | in all | ? <eos> | Sum | ai2 |

### Top-92 (2 samples using it): (119, 38, 31, 26, 11, 24, 28, 48, 11, 24, 9, 15, 76, 48, 28, 48, 101, 114, 85, 71, 124, 35, 134, 62)
| 119 | 38 | 31 | 26 | 11 | 24 | 28 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 28 | 48 | 101 | 114 | 85 | 71 | 124 | 35 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> | placed | <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are | now there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |
| There | are | <num> | crayons | in the | drawer | and <num> | crayons | on the | desk | . <PER_1> | placed | <num> | crayons | and <num> | scissors | on the | desk | . How many | crayons | are | now there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-93 (2 samples using it): (119, 84, 126, 80, 11, 24, 54, 105, 11, 24, 9, 15, 76, 48, 101, 114, 85, 25, 14, 100, 62)
| 119 | 84 | 126 | 80 | 11 | 24 | 54 | 105 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 85 | 25 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | birds | were | sitting | in a | tree | . Some more | fly | up to the | tree | . Then there | were | <num> | birds | in the | tree | . How many more | fly | up to the | tree | ? <eos> | Subtraction | ilds |
| <num> | birds | were | sitting | in a | tree | . Some more | fly | up to the | tree | . Then there | were | <num> | birds | in the | tree | . How many more | <unk> | up to the | tree | ? <eos> | Subtraction | ilds |

### Top-94 (2 samples using it): (119, 4, 15, 76, 48, 50, 11, 24, 69, 54, 20, 86, 38, 31, 26, 50, 99, 60, 57, 85, 117, 66, 70, 123, 82, 134, 62)
| 119 | 4 | 15 | 76 | 48 | 50 | 11 | 24 | 69 | 54 | 20 | 86 | 38 | 31 | 26 | 50 | 99 | 60 | 57 | 85 | 117 | 66 | 70 | 123 | 82 | 134 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> \xe2\x80\x99s | <unk> | gives | out | gold | stars | for <unk> | <unk> | work | . | <unk> | , <PER_1> | earned | <num> | gold | stars | . Today , he | earned | <num> more | . How many | gold | stars | did | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> \xe2\x80\x99s | <unk> | gives | out | gold | stars | for <unk> | <unk> | work | . | <unk> | , <PER_1> | earned | <num> | gold | stars | . Today , she | earned | <num> more | . How many | gold | stars | did | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-95 (2 samples using it): (119, 126, 80, 11, 24, 54, 4, 15, 76, 48, 46, 18, 28, 48, 46, 18, 9, 15, 76, 48, 46, 18, 85, 93, 1, 66, 70, 123, 82, 112, 35, 62)
| 119 | 126 | 80 | 11 | 24 | 54 | 4 | 15 | 76 | 48 | 46 | 18 | 28 | 48 | 46 | 18 | 9 | 15 | 76 | 48 | 46 | 18 | 85 | 93 | 1 | 66 | 70 | 123 | 82 | 112 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | baking | a | cake | . The | recipe | <unk> | for <num> | cups | of | flour | and <num> | cups | of | sugar | . She already | put | in <num> | cups | of | flour | . How many | cups | of | flour | does | she | need | to | add | ? <eos> | Subtraction | ai2 |
| <PER_1> | is | baking | a | cake | . The | recipe | <unk> | for <num> | cups | of | flour | and <num> | cups | of | sugar | . She already | put | in <num> | cups | of | flour | . How many | cups | of | flour | does | she | need | to | add | ? <eos> | Subtraction | ai2 |

### Top-96 (2 samples using it): (119, 38, 31, 26, 28, 48, 11, 24, 9, 15, 76, 48, 11, 24, 9, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 62)
| 119 | 38 | 31 | 26 | 28 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> red | orchids | and <num> white | orchids | in the | vase | . <PER_1> | cut | some red | orchids | from her flower | garden | . There | are | now <num> red | orchids | in the | vase | . How many red | orchids | did | she | cut | ? <eos> | Subtraction | ai2 |
| There | were | <num> red | orchids | and <num> white | orchids | in the | vase | . <PER_1> | cut | some red | orchids | from her flower | garden | . There | are | now <num> red | orchids | in the | vase | . How many red | orchids | did | she | cut | ? <eos> | Subtraction | ai2 |

### Top-97 (2 samples using it): (119, 38, 31, 26, 50, 11, 24, 54, 20, 86, 15, 76, 48, 51, 54, 84, 126, 80, 75, 86, 15, 76, 48, 50, 11, 24, 85, 117, 66, 70, 123, 109, 82, 100, 62)
| 119 | 38 | 31 | 26 | 50 | 11 | 24 | 54 | 20 | 86 | 15 | 76 | 48 | 51 | 54 | 84 | 126 | 80 | 75 | 86 | 15 | 76 | 48 | 50 | 11 | 24 | 85 | 117 | 66 | 70 | 123 | 109 | 82 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | walnut | trees | today | . When the | workers | are | finished | there | will | be | <num> | walnut | trees | in the | park | . How many | walnut | trees | did | the | workers | plant | today | ? <eos> | Subtraction | ai2 |
| There | are | <num> | maple | trees | currently in the | park | . Park | workers | will | plant | maple | trees | today | . When the | workers | are | finished | there | will | be | <num> | maple | trees | in the | park | . How many | maple | trees | did | the | workers | plant | today | ? <eos> | Subtraction | ai2 |

### Top-98 (2 samples using it): (119, 84, 126, 80, 11, 24, 54, 84, 20, 86, 84, 105, 11, 24, 9, 15, 76, 48, 101, 114, 40, 66, 70, 123, 82, 56, 109, 100, 62)
| 119 | 84 | 126 | 80 | 11 | 24 | 54 | 84 | 20 | 86 | 84 | 105 | 11 | 24 | 9 | 15 | 76 | 48 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 56 | 109 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | children | were | <unk> | on the | bus | . At the | bus | stop | , some more | children | got | on the | bus | . Then there | were | <num> | children | altogether on the | bus | . How many | children | got | on the | bus | at the | bus | stop | ? <eos> | Subtraction | ilds |
| <num> | children | were | <unk> | on the | bus | . At the | bus | stop | , some more | children | got | on the | bus | . Then there | were | <num> | children | altogether on the | bus | . How many | children | got | on the | bus | at the | bus | stop | ? <eos> | Subtraction | ilds |

### Top-99 (2 samples using it): (119, 38, 31, 26, 46, 18, 11, 24, 28, 48, 101, 114, 54, 105, 50, 11, 24, 51, 9, 15, 76, 48, 46, 18, 101, 114, 40, 66, 70, 123, 82, 14, 100, 62)
| 119 | 38 | 31 | 26 | 46 | 18 | 11 | 24 | 28 | 48 | 101 | 114 | 54 | 105 | 50 | 11 | 24 | 51 | 9 | 15 | 76 | 48 | 46 | 18 | 101 | 114 | 40 | 66 | 70 | 123 | 82 | 14 | 100 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> | bales | of | hay | in the | barn | and <num> | bales | in the | <unk> | . <PER_1> | <unk> | bales | in the | barn | today | . There | are | now <num> | bales | of | hay | in the | barn | . How many | bales | did | he | store | in the | barn | ? <eos> | Subtraction | ai2 |
| There | were | <num> | bales | of | hay | in the | barn | and <num> | bales | in the | <unk> | . <PER_1> | <unk> | bales | in the | barn | today | . There | are | now <num> | bales | of | hay | in the | barn | . How many | bales | did | he | store | in the | barn | ? <eos> | Subtraction | ai2 |

### Top-100 (2 samples using it): (119, 38, 31, 26, 50, 11, 24, 54, 20, 86, 15, 76, 48, 50, 51, 28, 48, 50, 51, 9, 15, 76, 48, 67, 80, 101, 114, 85, 117, 66, 70, 123, 109, 82, 56, 43, 124, 35, 62)
| 119 | 38 | 31 | 26 | 50 | 11 | 24 | 54 | 20 | 86 | 15 | 76 | 48 | 50 | 51 | 28 | 48 | 50 | 51 | 9 | 15 | 76 | 48 | 67 | 80 | 101 | 114 | 85 | 117 | 66 | 70 | 123 | 109 | 82 | 56 | 43 | 124 | 35 | 62 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |
| There | are | <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | and <num> | orchid | bushes | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |


