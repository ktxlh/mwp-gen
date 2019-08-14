Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-45-3-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-45-3-far.txt
k=10
n=10
# Overall - top templates
### Top-1 (32 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | loses | <num> | . How many | stickers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | peanuts | . He | loses | <num> | . How many | peanuts | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | blocks | . She | loses | <num> | . How many | blocks | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . She | loses | <num> | . How many | bananas | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | <MISC_1> | , but she | lost | <num> <MISC_1> | . How many | <MISC_1> | does | she | have | now | ? <eos> | Subtraction | ilds |
| <LOC_1> | starts | with <num> | eggs | . <PER_1> | takes | <num> away | . How many | eggs | does | <LOC_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | <MISC_1> | . She | buys | <num> more | . How many | <MISC_1> | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-2 (13 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . She | loses | <num> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | takes | <num> away | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <MISC_1> | . She | gives | <num> to <MISC_2> | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | bananas | . She | shares | <num> with <MISC_1> | . How many | bananas | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . He | shares | <num> with <PER_2> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (11 samples using it): (119, 83, 123, 25, 118, 114, 121, 97, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 97 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> | miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> | miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |

### Top-4 (11 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | cookies | . <PER_2> | has | <num> | . How many more | cookies | does | <PER_2> | have | than <PER_1> | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . He | finds | another <num> | . How many | oranges | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . She | buys | <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | tickets | . <PER_2> | gives | <PER_1> <num> more | . How many | tickets | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | pencils | . <PER_2> | gives | <PER_1> <num> more | . How many | pencils | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . <PER_2> | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | stickers | . She | gets | <num> more from <PER_2> | . How many | stickers | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | gets | <num> more from <PER_2> | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-5 (10 samples using it): (119, 83, 123, 25, 118, 114, 121, 132, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 132 | 105 | 112 | 79 | 44 | solution type | source |
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

### Top-6 (7 samples using it): (119, 83, 123, 48, 12, 109, 101, 57, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . She | buys | <num> more | . Later , <PER_1> | buys | <num> | oranges | at the | store | . How many | <MISC_1> | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | buys | <num> more | . Later , <PER_1> | buys | <num> | apples | at the | store | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | tickets | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | eggs | . <PER_2> | gives | <PER_1> <num> more | . Later , <PER_1> | buys | <num> | erasers | at the | store | . How many | eggs | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | gets | <num> more from <PER_2> | . Later , <PER_1> | buys | <num> | crayons | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bananas | . He | gets | <num> more from <MISC_1> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | bananas | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . She | gets | <num> more from <PER_2> | . Later , <PER_1> | buys | <num> | cards | at the | store | . How many | crayons | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-7 (6 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | cantelopes | . <PER_2> | grew | <num> | cantelopes | . How many | cantelopes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <ORG_1> | grew | <num> | potatoes | . <PER_1> | grew | <num> | potatoes | . How many | potatoes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | pumpkins | . <PER_2> | grew | <num> | pumpkins | . How many | pumpkins | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many more | books | does | <PER_1> | have | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-8 (6 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | balloons | but | lost | <num> of them | . How many | orange | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |
| <PER_1> | starts | with <num> | bottle | caps | . She | finds | another <num> | . How many | bottle | caps | does | <ORG_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . <PER_2> | takes | <num> away | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . She | shares | <num> with <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more from <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bottle | caps | . He | gets | <num> more from <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-9 (6 samples using it): (119, 83, 123, 25, 104, 61, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 104 | 61 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | candies | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | cards | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | cards | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | peanuts | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . She | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |


