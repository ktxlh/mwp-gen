Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-5-30-far.txt')
# Analysis of segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-5-30-far.txt
k=100
n=10
# Overall - top templates
### Top-1 (12 samples using it): (13, 77, 142, 81, 125, 108, 34, 122, 118, 102, 134)
| 13 | 77 | 142 | 81 | 125 | 108 | 34 | 122 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered <num> | kilometers | at <num> | kilometers | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | strolled <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-2 (7 samples using it): (13, 77, 142, 81, 70, 139, 112, 126, 144, 45, 92, 118, 102, 134)
| 13 | 77 | 142 | 81 | 70 | 139 | 112 | 126 | 144 | 45 | 92 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | crayons | . <PER_2> | takes | <num> away | . How many | crayons | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | eggs | . He | buys | <num> more | . How many | eggs | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | cards | . He | finds | another <num> | . How many | cards | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | eggs | . She | buys | <num> more | . How many | eggs | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | eggs | . She | finds | another <num> | . How many | eggs | does | <PER_1> | end | with ? <eos> | Addition | ilds |

### Top-3 (6 samples using it): (13, 77, 142, 127, 23, 142, 127, 23, 124, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 23 | 124 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | candies | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | cards | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | cards | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | collects | <num> | peanuts | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-4 (5 samples using it): (13, 77, 142, 73, 35, 34, 122, 79, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> | erasers | . She | loses <num> | . How many | erasers | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | blocks | . She | loses <num> | . How many | blocks | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | bananas | . She | loses <num> | . How many | bananas | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| There | were | <num> | <unk> and <num> | ducks | in the | <unk> | . How many | birds | were | in the | <unk> | ? <eos> | Addition | ilds |
| There | are <num> | <unk> | in a | tree | with <num> | <unk> | . How many more | <unk> | are | there than | <unk> | ? <eos> | Subtraction | ilds |

### Top-5 (5 samples using it): (13, 22, 96, 35, 34, 122, 31, 93, 79, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 93 | 79 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . He | gives | <num> | to <PER_2> | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | pencils | . He | gives | <num> | to <PER_2> | . How many | pencils | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | gives | <num> | to <PER_2> | . How many | stickers | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | erasers | . He | gives | <num> | to <PER_2> | . How many | erasers | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | apples | . She | shares | <num> | with <PER_2> | . How many | apples | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-6 (5 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 24, 77, 142, 81, 12, 73, 114)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | cantelopes | . <PER_2> | grew | <num> | cantelopes | . How many | cantelopes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <ORG_1> | grew | <num> | potatoes | . <PER_1> | grew | <num> | potatoes | . How many | potatoes | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | pumpkins | . <PER_2> | grew | <num> | pumpkins | . How many | pumpkins | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-7 (5 samples using it): (13, 77, 142, 127, 23, 142, 127, 73, 35, 34, 122, 92, 118, 102, 134)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 35 | 34 | 122 | 92 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <num> | are | eaten | by a | hippopotamus | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | crayons | . <num> | are | eaten | by a | hippopotamus | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | bananas | . <num> | are | eaten | by a | hippopotamus | . How many | bananas | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-8 (5 samples using it): (13, 77, 142, 73, 35, 34, 122, 41, 143, 44, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 41 | 143 | 44 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> | eggs | . He | gives | <num> | to <MISC_1> | . How many | eggs | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | apples | . She | gives | <num> | to <PER_2> | . How many | apples | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | cards | . She | gets | <num> more | from <MISC_1> | . How many | cards | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | oranges | . She | gets | <num> more | from <MISC_1> | . How many | oranges | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with | <num> | bananas | . She | gets | <num> more | from <PER_2> | . How many | bananas | does | <PER_1> | end | with ? <eos> | Addition | ilds |

### Top-9 (5 samples using it): (13, 77, 142, 70, 139, 112, 91, 24, 77, 142, 127, 23, 52, 69, 124)
| 13 | 77 | 142 | 70 | 139 | 112 | 91 | 24 | 77 | 142 | 127 | 23 | 52 | 69 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has <num> | bottle | caps | . She | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (13, 77, 142, 73, 35, 34, 122, 31, 70, 24, 77, 142, 81, 12, 73, 114)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | carrots | and <num> | watermelons | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew <num> | turnips | and <num> | pumpkins | . <MISC_1> | grew | <num> | turnips | . How many | turnips | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew <num> | carrots | and <num> | turnips | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |
| <PER_1> | grew <num> | turnips | and <num> | cantelopes | . <MISC_1> | grew | <num> | turnips | . How many | turnips | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew <num> | watermelons | and <num> | turnips | . <ORG_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-11 (5 samples using it): (13, 77, 142, 81, 12, 73, 35, 34, 122, 31, 70, 139, 35, 34, 77, 142, 73, 9, 34)
| 13 | 77 | 142 | 81 | 12 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 77 | 142 | 73 | 9 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | pencils | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | pencils | and <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in all | ? <eos> | Addition | ai2 |
| There | are <num> | erasers | and <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | erasers | in the | drawer | . How many | erasers | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | scissors | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | rulers | and <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | rulers | in the | drawer | . How many | rulers | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-12 (5 samples using it): (13, 77, 142, 127, 136, 80, 26, 70, 24, 77, 142, 127, 73, 35, 34, 122, 31, 70, 10, 134)
| 13 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 24 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 10 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | students | in the | class | and <num> | eggs | . If the | eggs | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | pencils | . If the | pencils | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |
| There | are | <num> | students | in the | class | and <num> | apples | . If the | apples | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |

### Top-13 (4 samples using it): (13, 77, 142, 73, 35, 34, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 73 | 35 | 34 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are <num> | crayons | in each | box | . How many | crayons | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-14 (4 samples using it): (13, 22, 96, 35, 34, 122, 79, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 79 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . She | loses <num> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | stickers | . He | loses <num> | . How many | stickers | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with <num> | peanuts | . He | loses <num> | . How many | peanuts | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-15 (4 samples using it): (13, 77, 142, 81, 125, 108, 34, 122, 93, 79)
| 13 | 77 | 142 | 81 | 125 | 108 | 34 | 122 | 93 | 79 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-16 (4 samples using it): (13, 22, 96, 35, 34, 122, 96, 35, 34, 77, 142, 101, 102, 134)
| 13 | 22 | 96 | 35 | 34 | 122 | 96 | 35 | 34 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have together | ? <eos> | Addition | ai2 |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have together | ? <eos> | Addition | ai2 |

### Top-17 (4 samples using it): (13, 77, 142, 73, 35, 34, 122, 31, 70, 24, 77, 142, 24)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 24 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are <num> | eggs | in a | box | . <PER_1> | takes | <num> | eggs | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are <num> | pencils | in a | box | . <PER_1> | takes | <num> | pencils | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-18 (4 samples using it): (13, 77, 142, 127, 134, 77, 142, 81, 12, 73, 57, 116, 22, 96, 35, 34)
| 13 | 77 | 142 | 127 | 134 | 77 | 142 | 81 | 12 | 73 | 57 | 116 | 22 | 96 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | dollars | . How many more | dollars | does | she | have | to | <unk> | to | have | <num> | dollars | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | fish | . How many more | fish | does | she | need | to | buy | to | have | <num> | fish | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | apples | . How many more | apples | does | <PER_1> | need | to | pick | to | have | <num> | apples altogether | ? <eos> | Subtraction | ilds |

### Top-19 (4 samples using it): (13, 77, 142, 73, 35, 34, 122, 96, 35, 34, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 96 | 35 | 34 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | candies | . If there | are | <num> | children | , how many | candies | are | there in | total | ? <eos> | Multiplication | ilds |
| If there | are <num> | eggs | in a | box | and <PER_1> | puts | <num> more | eggs inside | , how many | eggs | are | in the | box | ? <eos> | Addition | ilds |
| If there | are <num> | erasers | in a | box | and <PER_1> | puts | <num> more | erasers inside | , how many | erasers | are | in the | box | ? <eos> | Addition | ilds |
| If there | are <num> | crayons | in a | box | and <PER_1> | puts | <num> more | crayons inside | , how many | crayons | are | in the | box | ? <eos> | Addition | ilds |

### Top-20 (4 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | blocks | stored | in | boxes | . If there | are | <num> | boxes | , how many | blocks | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-21 (4 samples using it): (13, 77, 142, 81, 12, 73, 35, 34, 122, 31, 70, 58, 129, 65, 92, 118, 102, 134)
| 13 | 77 | 142 | 81 | 12 | 73 | 35 | 34 | 122 | 31 | 70 | 58 | 129 | 65 | 92 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | pears | and <num> | apples | from the | orchard | . She | gave | <num> | pears | to <PER_2> | . How many | pears | does | <PER_1> | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found <num> | seashells | and <num> | <unk> | on the | beach | . She | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found <num> | seashells | and <num> | <unk> | on the | beach | . He | gave | <num> of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |

### Top-22 (4 samples using it): (13, 77, 142, 73, 35, 34, 122, 31, 70, 43, 35, 34, 77, 142, 73, 9, 34)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 43 | 35 | 34 | 77 | 142 | 73 | 9 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | scissors | in the | drawer | . <PER_1> | placed | <num> | scissors | in the | drawer | . How many | scissors | are | now there | in all | ? <eos> | Addition | ai2 |
| There | are <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in all | ? <eos> | Addition | ai2 |

### Top-23 (4 samples using it): (13, 77, 142, 127, 23, 142, 127, 134, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 134 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | candies | in <PER_1> 's | candy | collection | . If the | candies | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | cards | in <PER_1> 's | <unk> | collection | . If the | cards | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |

### Top-24 (4 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 35, 34, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes | <num> | pencils | from a | jar | . There | were | originally <num> | pencils | in the | jar | . How many | pencils | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | apples | from a | jar | . There | were | originally <num> | apples | in the | jar | . How many | apples | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | bananas | from a | jar | . There | were | originally <num> | bananas | in the | jar | . How many | bananas | are | left | in the | jar | ? <eos> | Subtraction | ilds |
| <PER_1> | removes | <num> | eggs | from a | jar | . There | were | originally <num> | eggs | in the | jar | . How many | eggs | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-25 (4 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 10, 134, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 10 | 134 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | violet | balloons | and <num> red | balloons | . He | lost | <num> of the | violet | balloons | . How many | violet | balloons | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has <num> | orange | balloons | and <num> blue | balloons | . She | lost | <num> of the | orange | balloons | . How many | orange | balloons | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| If there | are <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |
| If there | are <num> | bottle | caps | in a | box | and <PER_1> | puts | <num> more | bottle | caps inside | , how many | bottle | caps | are | in the | box | ? <eos> | Addition | ilds |

### Top-26 (4 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 112, 126, 55, 34, 122, 79, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 112 | 126 | 55 | 34 | 122 | 79 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> | has | <num> | boxes | of | tickets | . Each box | holds | <num> | tickets | and there | are | <num> | boxes | in a | <unk> | . How many | tickets | does <ORG_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | blocks | . Each box | holds | <num> | blocks | and there | are | <num> | boxes | in a | <unk> | . How many | blocks | does <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | boxes | of | eggs | . Each box | holds | <num> | eggs | and there | are | <num> | boxes | in a | <unk> | . How many | eggs | does <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | had | <num> | meatballs | on her | <unk> | . <PER_2> | <unk> some | of her | meatballs | . Now she | has | <num> | meatballs | on her | <unk> | . How many | meatballs | did <PER_2> | <unk> | ? <eos> | Subtraction | ilds |

### Top-27 (4 samples using it): (13, 77, 142, 73, 35, 34, 122, 31, 70, 138, 12, 73, 35, 34, 122, 81, 12, 73, 35, 34, 122, 31, 70, 139)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 138 | 12 | 73 | 35 | 34 | 122 | 81 | 12 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | to | <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | to | <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | jogged | to | <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | to | <LOC_1> <LOC_2> | house | . It | is | <num> | miles | from <PER_1> 's | house | to <LOC_1> <LOC_2> | house | . It | took | <PER_1> <num> | hours | to | get there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |

### Top-28 (4 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 79, 77, 142, 127, 23, 142, 127, 134, 77, 142, 127, 23, 142, 127, 73, 120, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 127 | 23 | 142 | 127 | 134 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 120 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many | short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many | short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many | short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | bushes | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | bushes | today | . How many | short | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-29 (4 samples using it): (13, 77, 142, 127, 43, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 112, 126, 55, 34, 122, 31, 70, 24, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 43 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 112 | 126 | 55 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and brings <num> | cookies | to | share with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and brings <num> | cookies | to | share with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and brings <num> | cookies | to | share with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and brings <num> | cookies | to | share with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-30 (3 samples using it): (13, 77, 142, 70, 139, 112, 91, 129, 65, 127, 73, 35, 34)
| 13 | 77 | 142 | 70 | 139 | 112 | 91 | 129 | 65 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | takes | <num> away | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-31 (3 samples using it): (13, 77, 96, 35, 34, 77, 142, 127, 134, 77, 143, 44)
| 13 | 77 | 96 | 35 | 34 | 77 | 142 | 127 | 134 | 77 | 143 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | cards | . <num> | cards more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | marbles | . <num> | marbles more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |
| There | are | <num> | cards | . <num> | cards more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |

### Top-32 (3 samples using it): (13, 77, 128, 75, 98, 121, 34, 122, 118, 102, 134)
| 13 | 77 | 128 | 75 | 98 | 121 | 34 | 122 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |
| If <PER_1> | wandered | for <num> | hours | at <num> miles | per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |

### Top-33 (3 samples using it): (13, 77, 142, 70, 139, 112, 126, 144, 85, 122, 31, 70, 4, 49)
| 13 | 77 | 142 | 70 | 139 | 112 | 126 | 144 | 85 | 122 | 31 | 70 | 4 | 49 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | . He | finds | another <num> | . How many | oranges | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . She | buys | <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-34 (3 samples using it): (13, 22, 96, 35, 34, 122, 93, 79, 77, 142, 81, 12, 73, 114)
| 13 | 22 | 96 | 35 | 34 | 122 | 93 | 79 | 77 | 142 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | tickets | . <PER_2> | gives | <PER_1> <num> more | . How many | tickets | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | pencils | . <PER_2> | gives | <PER_1> <num> more | . How many | pencils | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | candies | . <PER_2> | gives | <PER_1> <num> more | . How many | candies | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-35 (3 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 148, 79, 77, 142, 127, 134)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 148 | 79 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does <PER_2> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . <PER_2> | has | <num> more | marbles | than <PER_1> | . How many | marbles | does <PER_2> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | whistles | . He | has | <num> more | whistles | that <PER_2> | . How many | whistles | does <PER_2> | have | ? <eos> | Subtraction | ilds |

### Top-36 (3 samples using it): (13, 77, 142, 66, 10, 134, 77, 142, 66, 10, 134, 77, 142, 101, 102, 134)
| 13 | 77 | 142 | 66 | 10 | 134 | 77 | 142 | 66 | 10 | 134 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | boxes | of | crayons | . Each | box | holds | <num> | crayons | . How many | crayons | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has <num> | boxes | of | peanuts | . Each | box | holds | <num> | peanuts | . How many | peanuts | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-37 (3 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 43, 35, 34, 77, 142, 101, 102, 134)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 43 | 35 | 34 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find together | ? <eos> | Addition | ai2 |

### Top-38 (3 samples using it): (13, 77, 142, 127, 73, 114, 122, 31, 70, 24, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 114 | 122 | 31 | 70 | 24 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |

### Top-39 (3 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 101, 102, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | marbles | in his | collection | . He | lost | <num> | marbles | . How many | marbles | does | he | have now | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | quarters | in her | bank | . She | spent | <num> of her | quarters | . How many | quarters | does | she | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | pennies | in his | bank | . He | spent | <num> of his | pennies | . How many | pennies | does | he | have now | ? <eos> | Subtraction | ai2 |

### Top-40 (3 samples using it): (13, 22, 96, 35, 34, 122, 41, 143, 44, 100, 17, 28, 47, 69, 124)
| 13 | 22 | 96 | 35 | 34 | 122 | 41 | 143 | 44 | 100 | 17 | 28 | 47 | 69 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | stickers | . She | gets | <num> more | from <PER_2> | . How many | stickers | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | . He | gets | <num> more | from <PER_2> | . How many | marbles | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | apples | . She | gets | <num> more | from <MISC_1> | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-41 (3 samples using it): (13, 77, 142, 94, 42, 103, 66, 10, 89, 100, 77, 142, 127, 134)
| 13 | 77 | 142 | 94 | 42 | 103 | 66 | 10 | 89 | 100 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | erasers | . If she | shares | them among | <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | marbles | . If she | shares | them among | <num> | friends | , how many | marbles | does each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | tickets | . If she | shares | them among | <num> | friends | , how many | tickets | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-42 (3 samples using it): (13, 77, 142, 101, 75, 35, 34, 122, 31, 70, 24, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 101 | 75 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> | bottle | caps | . <PER_2> | takes | <num> | away | . How many | bottle | caps | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-43 (3 samples using it): (13, 77, 142, 73, 49, 13, 77, 142, 78, 138, 39)
| 13 | 77 | 142 | 73 | 49 | 13 | 77 | 142 | 78 | 138 | 39 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | sold <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup | from the cookie mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup | from the cookie mom | ? <eos> | CommonDiv | ilds |
| If <PER_1> | sold <num> | boxes | of <MISC_1> | , how many cases | of <num> | boxes | does | <MISC_2> pickup | from the cookie mom | ? <eos> | CommonDiv | ilds |

### Top-44 (3 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 112, 12, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 112 | 12 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | <unk> <num> | friends | to a | party | . He | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | is | <unk> <num> | friends | to a | party | . She | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |

### Top-45 (3 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | strawberries | in his | <unk> | . He | picked | <num> more | strawberries | . How many | strawberries | did | he | have then | ? <eos> | Addition | ilds |
| <PER_1> | sold | <num> | boxes | of <MISC_1> <MISC_2> | <MISC_3> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave <PER_2> | <num> of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-46 (3 samples using it): (13, 77, 142, 127, 23, 92, 118, 102, 134, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 23 | 92 | 118 | 102 | 134 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | orange | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many | orange | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has <num> | violet | balloons | , he | gave | <PER_2> <num> of the | balloons | . How many | violet | balloons | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | has <num> | violet | marbles | , he | gave | <PER_2> <num> of the | marbles | . How many | violet | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-47 (3 samples using it): (13, 77, 142, 127, 134, 77, 142, 127, 23, 142, 127, 134, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 134 | 77 | 142 | 127 | 23 | 142 | 127 | 134 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | baseball | cards | . <PER_2> | bought | <num> | of | <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has <num> | baseball | cards | . <PER_2> | bought | <num> | of | <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | has <num> | baseball | cards | . <PER_2> | bought | <num> | of | <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |

### Top-48 (3 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 139, 112, 126, 89, 100, 77, 142, 101, 14)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 139 | 112 | 126 | 89 | 100 | 77 | 142 | 101 | 14 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | blocks | . <PER_2> | has | with <num> | blocks | . <PER_2> | finds | another <num> | . How many | blocks | does <PER_2> | end | with | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | cards | . <PER_2> | has | with <num> | cards | . <PER_2> | finds | another <num> | . How many | cards | does <PER_2> | end | with | ? <eos> | Addition | ilds |

### Top-49 (3 samples using it): (13, 77, 142, 127, 136, 80, 26, 70, 139, 112, 91, 34, 122, 31, 70, 144, 85, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 139 | 112 | 91 | 34 | 122 | 31 | 70 | 144 | 85 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | erasers | into | groups | of <num> | . <PER_1> | has | <num> | erasers | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | peanuts | into | groups | of <num> | . <PER_1> | has | <num> | peanuts | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-50 (3 samples using it): (13, 77, 142, 127, 23, 142, 127, 23, 142, 127, 23, 142, 127, 134, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 23 | 142 | 127 | 23 | 142 | 127 | 134 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> | of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> | of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought | <num> | of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |

### Top-51 (3 samples using it): (13, 77, 142, 81, 12, 73, 17, 28, 47, 108, 22, 96, 35, 34, 122, 68, 138, 12, 73, 35, 34)
| 13 | 77 | 142 | 81 | 12 | 73 | 17 | 28 | 47 | 108 | 22 | 96 | 35 | 34 | 122 | 68 | 138 | 12 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | took | <PER_1> | <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between | <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> | <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between | <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> | <num> | hours | to | run | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between | <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-52 (3 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 127, 23, 43, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 23 | 43 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | heads | come | in | packages of | <num> | . <PER_1> | ate | <num> <MISC_1> | <MISC_2> | . How many whole | boxes | did he | eat | and how many | <MISC_1> <MISC_2> | does he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in | packages of | <num> | . <PER_1> | ate | <num> <MISC_1> | <MISC_2> | . How many whole | boxes | did he | eat | and how many | <MISC_1> <MISC_2> | does he | have | left | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in | packages of | <num> | . <PER_1> | ate | <num> <MISC_1> | <MISC_2> | . How many whole | boxes | did he | eat | and how many | <MISC_1> <MISC_2> | does he | have | left | ? <eos> | CommonDiv | ilds |

### Top-53 (3 samples using it): (13, 77, 142, 127, 136, 80, 26, 70, 139, 112, 126, 55, 34, 122, 31, 70, 139, 35, 34, 122, 31, 70, 139)
| 13 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 139 | 112 | 126 | 55 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 31 | 70 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each time she | goes | to the | store | . How many | peanuts | did <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each time she | goes | to the | store | . How many | peanuts | did <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| A | farmer | <unk> the | day | with <num> | buckets | of | seeds | . <unk> <unk> the | morning | <unk> | seeds | , she now | has | <num> | buckets | . How many | buckets | of seeds | did | the | farmer <unk> | ? <eos> | Subtraction | ai2 |

### Top-54 (3 samples using it): (13, 77, 142, 70, 139, 112, 91, 129, 9, 34, 122, 31, 70, 138, 140, 129, 65, 127, 23, 52, 69, 124)
| 13 | 77 | 142 | 70 | 139 | 112 | 91 | 129 | 9 | 34 | 122 | 31 | 70 | 138 | 140 | 129 | 65 | 127 | 23 | 52 | 69 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . She | gets | <num> more | from <PER_2> | . Later | , <PER_1> | buys | <num> | crayons | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | bananas | . He | gets | <num> more | from <MISC_1> | . Later | , <PER_1> | buys | <num> | cards | at the | store | . How many | bananas | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | crayons | . She | gets | <num> more | from <PER_2> | . Later | , <PER_1> | buys | <num> | cards | at the | store | . How many | crayons | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-55 (3 samples using it): (13, 77, 142, 127, 23, 142, 127, 73, 35, 34, 122, 79, 77, 142, 127, 134, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 127 | 134 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . When they | cleaned | them , they | discovered that <num> | were | cracked | . How many | seashells | did they | find together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . When they | cleaned | them , they | discovered that <num> | were | cracked | . How many | seashells | did they | find together | ? <eos> | Addition | ai2 |
| <PER_1> | found | <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . When they | cleaned | them , they | discovered that <num> | were | cracked | . How many | seashells | did they | find together | ? <eos> | Addition | ai2 |

### Top-56 (3 samples using it): (13, 77, 142, 127, 73, 120, 79, 77, 142, 127, 73, 120, 142, 127, 134, 77, 142, 127, 23, 142, 127, 73, 120, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 120 | 79 | 77 | 142 | 127 | 73 | 120 | 142 | 127 | 134 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 120 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | . How many | orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | <num> | walnut | trees | today | . How many | walnut | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-57 (3 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 35, 34, 122, 81, 12, 73, 120, 79, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 81 | 12 | 73 | 120 | 79 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | candies | in a | box | . <PER_1> | has | <num> | candies | in a | bag | . <PER_2> | takes | <num> | candies | out of the | box | . How many | candies | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-58 (3 samples using it): (13, 77, 142, 127, 73, 57, 123, 75, 129, 65, 127, 23, 2, 46, 102, 134, 77, 142, 127, 73, 120, 79, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 57 | 123 | 75 | 129 | 65 | 127 | 23 | 2 | 46 | 102 | 134 | 77 | 142 | 127 | 73 | 120 | 79 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of | <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there | in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | bananas | in a | pile | on the | desk | . Each | banana | comes | in a | package | of | <num> | . <num> | bananas | are | added | to the | pile | . How many | bananas | are | there | in the | pile | ? <eos> | Addition | ilds |
| There | are | <num> | candies | in a | pile | on the | desk | . Each | candy | comes | in a | package | of | <num> | . <num> | candies | are | added | to the | pile | . How many | candies | are | there | in the | pile | ? <eos> | Addition | ilds |

### Top-59 (2 samples using it): (13, 77, 142, 121, 34, 122, 31, 70, 137, 79)
| 13 | 77 | 142 | 121 | 34 | 122 | 31 | 70 | 137 | 79 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do | <num> | bananas | cost | ? <eos> | Multiplication | ilds |
| Each | <unk> | costs | $ <num> | . How much | do | <num> | tickets | cost | ? <eos> | Multiplication | ilds |

### Top-60 (2 samples using it): (13, 77, 142, 66, 10, 89, 100, 77, 142, 127, 134)
| 13 | 77 | 142 | 66 | 10 | 89 | 100 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has | <num> | legs | . How many | legs | do <num> | bees | have | ? <eos> | Multiplication | ilds |
| A | <unk> | has | <num> | legs | . How many | legs | do <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-61 (2 samples using it): (13, 77, 93, 113, 34, 122, 96, 35, 34)
| 13 | 77 | 93 | 113 | 34 | 122 | 96 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> miles at | <num> miles per hour | . How long | did | <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| If <PER_1> | walked | <num> kilometers at | <num> kilometers per hour | , how long | was | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-62 (2 samples using it): (13, 77, 142, 13, 77, 79, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 13 | 77 | 79 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | birds | and <num> | <unk> | . How many more | birds | are | there than | <unk> | ? <eos> | Subtraction | ilds |
| There | are <num> | flowers | and <num> | bees | . How many <unk> | bees | are | there than | flowers | ? <eos> | Subtraction | ilds |

### Top-63 (2 samples using it): (13, 77, 142, 70, 139, 112, 126, 144, 85, 122, 118, 102, 134)
| 13 | 77 | 142 | 70 | 139 | 112 | 126 | 144 | 85 | 122 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | oranges | . <PER_2> | takes | <num> away | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-64 (2 samples using it): (13, 77, 142, 127, 136, 80, 26, 70, 139, 112, 108, 22, 96, 35, 34)
| 13 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 139 | 112 | 108 | 22 | 96 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | ran | <num> | miles | and | walked | <num> | miles | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-65 (2 samples using it): (13, 77, 142, 70, 139, 112, 126, 69, 124, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 70 | 139 | 112 | 126 | 69 | 124 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bananas | . She | shares | <num> | with <MISC_1> | . How many | bananas | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | marbles | . He | shares | <num> | with <PER_2> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-66 (2 samples using it): (13, 77, 96, 35, 34, 122, 96, 35, 34, 122, 93, 79)
| 13 | 77 | 96 | 35 | 34 | 122 | 96 | 35 | 34 | 122 | 93 | 79 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much <unk> | is | <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |
| <PER_1> | weighs | <num> | pounds | . <PER_2> | weighs | <num> | pounds | . How much <unk> | is | <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-67 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> red | markers | and <num> blue | markers | . How many | markers | does | she | have altogether | ? <eos> | Addition | ilds |
| <unk> <PER_1> | bought <num> | <unk> | <unk> | equally into <num> | boxes | . How many | <unk> | were | in each | box | ? <eos> | CommonDiv | ilds |

### Top-68 (2 samples using it): (13, 22, 96, 35, 34, 122, 41, 124, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 41 | 124 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | apples | . He | buys | <num> more | . How many | apples | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | candies | . <PER_2> | takes | <num> away | . How many | candies | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-69 (2 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 24, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have altogether | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | markers | . <PER_2> | gave | her <num> more | markers | . How many | markers | does | <PER_1> | have altogether | ? <eos> | Addition | ilds |

### Top-70 (2 samples using it): (13, 77, 142, 121, 34, 122, 31, 9, 34, 122, 118, 102, 134)
| 13 | 77 | 142 | 121 | 34 | 122 | 31 | 9 | 34 | 122 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> blocks | . She | shares | <num> | with <PER_2> | . How many blocks | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> <MISC_1> | . She | shares | <num> | with <PER_2> | . How many <MISC_1> | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-71 (2 samples using it): (13, 22, 96, 35, 34, 122, 93, 79, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 93 | 79 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | peanuts | . <PER_2> | gives | <PER_1> <num> more | . How many | peanuts | does | <PER_1> | end | with ? <eos> | Addition | ilds |
| <PER_1> | starts | with <num> | bananas | . <PER_2> | gives | <PER_1> <num> more | . How many | bananas | does | <PER_1> | end | with ? <eos> | Addition | ilds |

### Top-72 (2 samples using it): (13, 77, 142, 1, 35, 34, 122, 96, 35, 34, 77, 142, 73, 114)
| 13 | 77 | 142 | 1 | 35 | 34 | 122 | 96 | 35 | 34 | 77 | 142 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | pencils | . If there | are | <num> | children | , how many | pencils | are | there in total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | oranges | . If there | are | <num> | children | , how many | oranges | are | there in total | ? <eos> | Multiplication | ilds |

### Top-73 (2 samples using it): (13, 77, 142, 127, 23, 142, 127, 73, 120, 79, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 120 | 79 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bottle | caps | . <num> | are | eaten | by a | hippopotamus | . How many | bottle | caps | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | starts with <num> | bottle | caps | . <num> | are | eaten | by a | hippopotamus | . How many | bottle | caps | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |

### Top-74 (2 samples using it): (13, 77, 96, 35, 34, 122, 31, 70, 43, 35, 34, 77, 142, 127, 73, 114)
| 13 | 77 | 96 | 35 | 34 | 122 | 31 | 70 | 43 | 35 | 34 | 77 | 142 | 127 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked | <num> | <unk> | and <PER_2> | picked | <num> | <unk> | from the <unk> | tree | . How many | <unk> | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-75 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 81, 12, 73, 114)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | watermelons | and <num> | cantelopes | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |
| <PER_1> | grew | <num> | watermelons | and <num> | pumpkins | . <MISC_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-76 (2 samples using it): (13, 77, 142, 81, 125, 70, 139, 112, 126, 69, 124, 77, 142, 127, 73, 35, 34)
| 13 | 77 | 142 | 81 | 125 | 70 | 139 | 112 | 126 | 69 | 124 | 77 | 142 | 127 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with | <num> | bottle | caps | . She | shares | <num> | with <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with ? <eos> | Subtraction | ilds |
| <PER_1> | starts | with | <num> | bottle | caps | . He | gets | <num> more | from <PER_2> | . How many | bottle | caps | does | <PER_1> | end | with ? <eos> | Addition | ilds |

### Top-77 (2 samples using it): (13, 77, 142, 73, 22, 96, 35, 34, 122, 96, 35, 34, 77, 142, 127, 73, 114)
| 13 | 77 | 142 | 73 | 22 | 96 | 35 | 34 | 122 | 96 | 35 | 34 | 77 | 142 | 127 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |
| <PER_1> | picked <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-78 (2 samples using it): (13, 77, 142, 127, 134, 77, 142, 127, 23, 142, 127, 23, 142, 127, 134)
| 13 | 77 | 142 | 127 | 134 | 77 | 142 | 127 | 23 | 142 | 127 | 23 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> <MISC_1> | games | . How many | does she | need to | give | away so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> <MISC_1> | games | . How many | does she | need to | give | away so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |

### Top-79 (2 samples using it): (13, 22, 96, 35, 34, 122, 31, 70, 139, 112, 126, 69, 124, 77, 142, 73, 35, 34)
| 13 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 139 | 112 | 126 | 69 | 124 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . She | shares | <num> | with <PER_3> | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | has | <num> | apples | . He | shares | <num> | with <PER_3> | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-80 (2 samples using it): (13, 77, 142, 127, 73, 120, 79, 77, 142, 127, 73, 120, 79, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 120 | 79 | 77 | 142 | 127 | 73 | 120 | 79 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | guests | <unk> | to his | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will he | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | has <num> | guests | <unk> | to her <unk> | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will she | need | ? <eos> | CommonDiv | ilds |

### Top-81 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 81, 66, 10, 134, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 81 | 66 | 10 | 134 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> <num> | of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | on the | beach | . he | gave | <PER_2> <num> | of the | seashells | . How many | seashells | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-82 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 35, 34, 122, 31, 70, 67, 73, 35, 34)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 31 | 70 | 67 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-83 (2 samples using it): (13, 77, 142, 73, 35, 34, 122, 31, 70, 10, 134, 77, 142, 127, 81, 12, 73, 114)
| 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 10 | 134 | 77 | 142 | 127 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | blue | and <num> green | balloons | . <PER_2> | has | <num> | blue | balloons | . How many | blue | balloons | do | they | have | in all | ? <eos> | Addition | ai2 |
| <PER_1> | has <num> | blue | and <num> red | marbles | . <PER_2> | has | <num> | blue | marbles | . How many | blue | marbles | do | they | have | in all | ? <eos> | Addition | ai2 |

### Top-84 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 79, 77, 142, 101, 102, 134, 77, 142, 101, 102, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 101 | 102 | 134 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | dimes | in his | bank | . His | sister | borrowed | <num> | dimes | . How many | dimes | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | quarters | and <num> | dimes | in her | bank | . Her | sister | borrowed | <num> | dimes | . How many | dimes | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |

### Top-85 (2 samples using it): (13, 77, 142, 127, 23, 142, 127, 73, 120, 142, 127, 134, 77, 142, 127, 23, 2, 34)
| 13 | 77 | 142 | 127 | 23 | 142 | 127 | 73 | 120 | 142 | 127 | 134 | 77 | 142 | 127 | 23 | 2 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <num> | are about | school | and the | rest | are about | sports | . How many | books about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | books | . <num> | are about | school | and the | rest | are about | sports | . How many | books about | sports | does | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-86 (2 samples using it): (13, 77, 142, 81, 125, 108, 22, 70, 139, 112, 91, 68, 140, 129, 65, 92, 118, 102, 134)
| 13 | 77 | 142 | 81 | 125 | 108 | 22 | 70 | 139 | 112 | 91 | 68 | 140 | 129 | 65 | 92 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | dog | had | <num> | puppies | and <num> | had | spots | . She | gave | <num> | to her | friends | . How many | puppies | does | she now | have | ? <eos> | Subtraction | ai2 |
| <PER_1> 's | cat | had | <num> | kittens | and <num> | had | spots | . She | gave | <num> | to her | friends | . How many | kittens | does | she now | have | ? <eos> | Subtraction | ai2 |

### Top-87 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 24, 77, 142, 127, 134, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 134 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | class | is | <unk> | a pizza | party | . You | buy | <num> | pizzas | . Each | pizza | has <num> | slices | . How many | slices | is that | altogether | ? <eos> | Multiplication | ilds |
| A | restaurant | made <num> | hamburgers | and <num> hot | dogs | to | serve | during | lunch | . <unk> <num> | hamburgers | were <unk> | served | . How many | hamburgers | were | over | ? <eos> | Subtraction | ai2 |

### Top-88 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 79, 77, 142, 127, 23, 124, 77, 142, 101, 102, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 127 | 23 | 124 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | quarters | in her | bank | . Her | dad | borrowed <num> | quarters | from <PER_1> | . How many | quarters | does | she | have now | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in her | bank | . Her | dad | borrowed <num> | nickels | from <PER_1> | . How many | nickels | does | she | have now | ? <eos> | Subtraction | ai2 |

### Top-89 (2 samples using it): (13, 77, 143, 34, 122, 31, 109, 102, 138, 113, 34, 122, 118, 102, 134)
| 13 | 77 | 143 | 34 | 122 | 31 | 109 | 102 | 138 | 113 | 34 | 122 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> <MISC_1> | . <PER_2> | has | <num> <PER_3> | . If <PER_2> | gives | all of his <MISC_1> | to <PER_1> | , how many <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> <MISC_1> | . <PER_2> | has | <num> <PER_3> | . If <PER_2> | gives | all of his <MISC_1> | to <PER_1> | , how many <MISC_1> | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-90 (2 samples using it): (13, 77, 142, 4, 22, 96, 35, 34, 122, 118, 102, 138, 134, 77, 142, 73, 35, 34)
| 13 | 77 | 142 | 4 | 22 | 96 | 35 | 34 | 122 | 118 | 102 | 138 | 134 | 77 | 142 | 73 | 35 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | peanuts | . <PER_2> | has | <num> | peanuts | . If <PER_2> | gives | all of her | peanuts | to <PER_1> | , how many | peanuts | will | <PER_1> | have | ? <eos> | Addition | ilds |
| <PER_1> | has <num> | crayons | . <PER_2> | has | <num> | crayons | . If <PER_2> | gives | all of her | crayons | to <PER_1> | , how many | crayons | will | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-91 (2 samples using it): (13, 77, 13, 77, 142, 73, 35, 34, 122, 31, 70, 96, 35, 34, 77, 142, 127, 73, 35, 34, 109)
| 13 | 77 | 13 | 77 | 142 | 73 | 35 | 34 | 122 | 31 | 70 | 96 | 35 | 34 | 77 | 142 | 127 | 73 | 35 | 34 | 109 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | football | games | this | year | . She | went | to <num> | games | last | year | . How many | football | games | did | <PER_1> | go | to in all | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | football | games | this | year | . He | went | to <num> | games | last | year | . How many | football | games | did | <PER_1> | go | to in all | ? <eos> | Addition | ai2 |

### Top-92 (2 samples using it): (13, 77, 142, 81, 12, 73, 35, 34, 122, 96, 35, 34, 122, 79, 77, 142, 73, 9, 34)
| 13 | 77 | 142 | 81 | 12 | 73 | 35 | 34 | 122 | 96 | 35 | 34 | 122 | 79 | 77 | 142 | 73 | 9 | 34 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | crayons | and <num> | pencils | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now there | in total | ? <eos> | Addition | ai2 |
| There | are <num> | pencils | and <num> | rulers | in the | drawer | . <PER_1> | placed | <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |

### Top-93 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 79, 77, 142, 127, 136, 80, 26, 70, 24, 77, 142, 127, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 79 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 24 | 77 | 142 | 127 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in his | bank | . His | dad | gave | him | <num> | nickels | and <num> | quarters | . How many | nickels | does he | have now | ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | pennies | and <num> | dimes | in his | bank | . His | dad | gave | him | <num> | dimes | and <num> | nickels | . How many | dimes | does he | have now | ? <eos> | Addition | ai2 |

### Top-94 (2 samples using it): (13, 22, 96, 35, 34, 122, 96, 35, 34, 122, 96, 35, 34, 77, 142, 81, 12, 73, 114)
| 13 | 22 | 96 | 35 | 34 | 122 | 96 | 35 | 34 | 122 | 96 | 35 | 34 | 77 | 142 | 81 | 12 | 73 | 114 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in total | ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many blue | balloons | do | they | have | in all | ? <eos> | Sum | ai2 |

### Top-95 (2 samples using it): (13, 77, 142, 127, 73, 120, 39, 12, 73, 35, 34, 122, 31, 70, 24, 77, 142, 127, 23, 124)
| 13 | 77 | 142 | 127 | 73 | 120 | 39 | 12 | 73 | 35 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 23 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | on the | beach | . she | gave | <PER_2> some of her | seashells | . She | has | <num> | seashell | . How many | seashells | did she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> some of his | seashells | . He | has | <num> | seashell | . How many | seashells | did he | give | to <PER_2> | ? <eos> | Subtraction | ai2 |

### Top-96 (2 samples using it): (13, 77, 142, 127, 23, 7, 3, 9, 34, 122, 31, 70, 138, 140, 129, 65, 127, 23, 52, 69, 124)
| 13 | 77 | 142 | 127 | 23 | 7 | 3 | 9 | 34 | 122 | 31 | 70 | 138 | 140 | 129 | 65 | 127 | 23 | 52 | 69 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gives | <PER_1> <num> more | . Later | , <PER_1> | buys | <num> | tickets | at the | store | . How many | apples | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | eggs | . <PER_2> | gives | <PER_1> <num> more | . Later | , <PER_1> | buys | <num> | erasers | at the | store | . How many | eggs | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-97 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 35, 34, 122, 79, 77, 142, 127, 136, 80, 26, 70, 139)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 79 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | school | is | <unk> | a <unk> | trip | . There | are | <num> | students | and <num> | seats | on each school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |
| The | school | is | <unk> | a <unk> | trip | . There | are | <num> | students | and <num> | seats | on each school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |

### Top-98 (2 samples using it): (13, 77, 142, 81, 125, 114, 50, 22, 96, 35, 34, 122, 31, 70, 148, 79, 77, 142, 101, 102, 134)
| 13 | 77 | 142 | 81 | 125 | 114 | 50 | 22 | 96 | 35 | 34 | 122 | 31 | 70 | 148 | 79 | 77 | 142 | 101 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a party | . How many | cookies | did | they | have altogether | ? <eos> | Addition | ilds |
| <PER_1> <PER_2> | mom | baked | <num> | cookies | . <PER_3> \xe2\x80\x99s | dad | baked | <num> | cookies | . They both | <unk> | them to | school | for a party | . How many | cookies | did | they | have altogether | ? <eos> | Addition | ilds |

### Top-99 (2 samples using it): (13, 77, 142, 127, 136, 80, 26, 70, 139, 112, 126, 55, 34, 122, 31, 70, 24, 77, 142, 127, 23, 124)
| 13 | 77 | 142 | 127 | 136 | 80 | 26 | 70 | 139 | 112 | 126 | 55 | 34 | 122 | 31 | 70 | 24 | 77 | 142 | 127 | 23 | 124 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave <PER_2> some | of her | seashells | . She | has | <num> | seashell | . How many | seashells | did she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | and <num> | <unk> | on the | beach | . She | gave <PER_2> some | of her | seashells | . She | has | <num> | seashell | . How many | seashells | did she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |

### Top-100 (2 samples using it): (13, 77, 142, 127, 73, 35, 34, 122, 31, 70, 139, 35, 34, 122, 31, 70, 139, 35, 34, 122, 92, 118, 102, 134)
| 13 | 77 | 142 | 127 | 73 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 31 | 70 | 139 | 35 | 34 | 122 | 92 | 118 | 102 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |
| There | were | <num> | roses | in the | vase | . <PER_1> | cut | some | roses | from her flower | garden | . There | are | now <num> | roses | in the | vase | . How many | roses | did | she | cut | ? <eos> | Subtraction | ai2 |


