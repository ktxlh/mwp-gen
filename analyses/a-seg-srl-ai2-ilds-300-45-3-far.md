Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-45-3-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-45-3-far.txt
k=10
n=1
# Overall - top templates
### Top-1 (32 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-2 (13 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (11 samples using it): (119, 83, 123, 25, 118, 114, 121, 97, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 97 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-4 (11 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |

### Top-5 (10 samples using it): (119, 83, 123, 25, 118, 114, 121, 132, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 132 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (7 samples using it): (119, 83, 123, 48, 12, 109, 101, 57, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . She | buys | <num> more | . Later , <PER_1> | buys | <num> | oranges | at the | store | . How many | <MISC_1> | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-7 (6 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-8 (6 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | balloons | but | lost | <num> of them | . How many | orange | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-9 (6 samples using it): (119, 83, 123, 25, 104, 61, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 104 | 61 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (32 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-2 (11 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |

### Top-3 (7 samples using it): (119, 83, 123, 48, 12, 109, 101, 57, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . She | buys | <num> more | . Later , <PER_1> | buys | <num> | oranges | at the | store | . How many | <MISC_1> | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-4 (6 samples using it): (119, 83, 123, 25, 104, 61, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 104 | 61 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-5 (6 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-6 (5 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-7 (4 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |

### Top-8 (4 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now | there | in total | ? <eos> | Addition | ai2 |

### Top-9 (4 samples using it): (119, 83, 123, 80, 28, 58, 62, 96, 104, 61, 77, 83, 123, 80, 110, 130, 3, 105, 112, 79, 124, 17, 65, 89, 49, 134)
| 119 | 83 | 123 | 80 | 28 | 58 | 62 | 96 | 104 | 61 | 77 | 83 | 123 | 80 | 110 | 130 | 3 | 105 | 112 | 79 | 124 | 17 | 65 | 89 | 49 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-10 (4 samples using it): (119, 83, 123, 117, 62, 96, 62, 96, 104, 106, 81, 62, 96, 55, 14, 70, 64, 81, 62, 96, 85, 3, 105, 124, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 62 | 96 | 104 | 106 | 81 | 62 | 96 | 55 | 14 | 70 | 64 | 81 | 62 | 96 | 85 | 3 | 105 | 124 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | apples | in a | pile | on the | desk | . Each | apple | comes | in a | package | of <num> | . <num> | apples | are | added | to the | pile | . How many | apples | are | there | in the | pile | ? <eos> | Addition | ilds |


## Subtraction (257 samples)
### Top-1 (32 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-2 (13 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (5 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 37, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 37 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-4 (4 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 80, 97, 105, 37, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 80 | 97 | 105 | 37 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-5 (4 samples using it): (119, 83, 123, 25, 14, 64, 81, 62, 96, 85, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 14 | 64 | 81 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | blocks | . <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-6 (4 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 37, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 37 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes | <num> | pencils | from a | jar | . There | were | originally <num> | pencils | in the | jar | . How many | pencils | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-7 (6 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | balloons | but | lost | <num> of them | . How many | orange | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-8 (3 samples using it): (119, 83, 123, 80, 57, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | eggs | . <PER_2> | has | <num> | eggs | . He | loses | <num> | . How many | eggs | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-9 (3 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 55, 6, 40, 93, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 55 | 6 | 40 | 93 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | marbles | , he | gave | <PER_2> <num> | of the | marbles | . How many | orange | marbles | does | he now | have | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 50, 6, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 50 | 6 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> of <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |


## CommonDiv (95 samples)
### Top-1 (10 samples using it): (119, 83, 123, 25, 118, 114, 121, 132, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 132 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-2 (11 samples using it): (119, 83, 123, 25, 118, 114, 121, 97, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 97 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-3 (5 samples using it): (119, 83, 123, 25, 2, 82, 64, 81, 62, 96, 12, 109, 2, 82, 92, 83, 123, 25, 2, 82, 76, 57, 83, 123, 80, 87, 3, 105, 37, 17, 65, 134)
| 119 | 83 | 123 | 25 | 2 | 82 | 64 | 81 | 62 | 96 | 12 | 109 | 2 | 82 | 92 | 83 | 123 | 25 | 2 | 82 | 76 | 57 | 83 | 123 | 80 | 87 | 3 | 105 | 37 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-4 (4 samples using it): (119, 83, 123, 39, 55, 40, 24, 100, 70, 87, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 39 | 55 | 40 | 24 | 100 | 70 | 87 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | sold | <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (119, 83, 123, 25, 81, 62, 96, 102, 83, 123, 80, 87, 3, 105, 37, 17, 65, 134)
| 119 | 83 | 123 | 25 | 81 | 62 | 96 | 102 | 83 | 123 | 80 | 87 | 3 | 105 | 37 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (119, 83, 123, 129, 62, 96, 73, 25, 14, 70, 64, 81, 62, 96, 132, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 129 | 62 | 96 | 73 | 25 | 14 | 70 | 64 | 81 | 62 | 96 | 132 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | students | in the | class | and <num> | eggs | . If the | eggs | are | divided | equally among the | students | , how many | does | each | student | get | ? <eos> | CommonDiv | ilds |

### Top-7 (3 samples using it): (119, 83, 123, 26, 55, 42, 24, 23, 3, 105, 124, 17, 65, 134)
| 119 | 83 | 123 | 26 | 55 | 42 | 24 | 23 | 3 | 105 | 124 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | sold | <num> | boxes | of <MISC_1> | , how many | cases | of <num> | boxes | does | <MISC_2> pickup | from the | cookie mom | ? <eos> | CommonDiv | ilds |

### Top-8 (3 samples using it): (74, 16, 83, 123, 117, 62, 96, 102, 83, 123, 39, 130, 3, 105, 112, 79, 44)
| 74 | 16 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | <unk> | <num> | friends | to a | party | . He | has | <num> | cookies | . How many | cookies | will | each friend | get | ? <eos> | CommonDiv | ilds |

### Top-9 (3 samples using it): (119, 83, 123, 80, 98, 95, 72, 104, 61, 77, 83, 123, 80, 132, 105, 112, 79, 44)
| 119 | 83 | 123 | 80 | 98 | 95 | 72 | 104 | 61 | 77 | 83 | 123 | 80 | 132 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is | each | group | ? <eos> | CommonDiv | ilds |

### Top-10 (3 samples using it): (74, 61, 109, 101, 12, 109, 101, 130, 3, 105, 112, 79, 87, 3, 105, 112, 79, 4, 89)
| 74 | 61 | 109 | 101 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 87 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | heads | come | in packages of <num> | . <PER_1> | ate | <num> <MISC_1> <MISC_2> | . How many whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |


## Multiplication (93 samples)
### Top-1 (4 samples using it): (119, 83, 123, 117, 62, 96, 85, 3, 105, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-2 (11 samples using it): (119, 83, 123, 25, 118, 114, 121, 97, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 97 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-3 (3 samples using it): (119, 83, 123, 25, 2, 82, 31, 96, 73, 25, 113, 5, 97, 105, 112, 79, 31, 65, 134)
| 119 | 83 | 123 | 25 | 2 | 82 | 31 | 96 | 73 | 25 | 113 | 5 | 97 | 105 | 112 | 79 | 31 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-4 (2 samples using it): (74, 61, 109, 101, 7, 60, 123, 80, 79, 44)
| 74 | 61 | 109 | 101 | 7 | 60 | 123 | 80 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do | <num> | bananas | cost | ? <eos> | Multiplication | ilds |

### Top-5 (2 samples using it): (74, 16, 83, 123, 39, 130, 3, 105, 112, 79, 4, 89)
| 74 | 16 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-6 (2 samples using it): (119, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | drove | <num> | miles | every | hour | . How many | miles | would | he | drive | in <num> | hours | ? <eos> | Multiplication | ilds |

### Top-7 (2 samples using it): (119, 83, 123, 25, 113, 5, 104, 16, 83, 123, 39, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 113 | 5 | 104 | 16 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | crayons | . Each | box | holds | <num> | crayons | . How many | crayons | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-8 (2 samples using it): (74, 16, 83, 123, 80, 57, 83, 123, 80, 87, 3, 105, 46, 134)
| 74 | 16 | 83 | 123 | 80 | 57 | 83 | 123 | 80 | 87 | 3 | 105 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | pencils | . If there | are | <num> | children | , how many | pencils | are | there in total | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (74, 16, 83, 123, 80, 71, 102, 83, 123, 80, 42, 93, 3, 105, 1, 65, 134)
| 74 | 16 | 83 | 123 | 80 | 71 | 102 | 83 | 123 | 80 | 42 | 93 | 3 | 105 | 1 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-10 (2 samples using it): (119, 83, 123, 26, 68, 39, 57, 83, 123, 129, 62, 96, 40, 24, 23, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 26 | 68 | 39 | 57 | 83 | 123 | 129 | 62 | 96 | 40 | 24 | 23 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | packages | of | gum | . There | are | <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (1 samples using it): (119, 83, 123, 117, 62, 96, 104, 61, 109, 101, 103, 8, 61, 109, 101, 103, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 117 | 62 | 96 | 104 | 61 | 109 | 101 | 103 | 8 | 61 | 109 | 101 | 103 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | dimes | in her | bank | . Her | dad | gave | her <num> | dimes | and her | mother | gave | her <num> | dimes | . How many | dimes | does | <PER_1> | have | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-2 (1 samples using it): (74, 16, 83, 123, 117, 62, 96, 73, 121, 104, 16, 83, 123, 71, 73, 80, 110, 130, 3, 105, 37, 46, 134)
| 74 | 16 | 83 | 123 | 117 | 62 | 96 | 73 | 121 | 104 | 16 | 83 | 123 | 71 | 73 | 80 | 110 | 130 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pies | during | lunch | and <num> | during dinner today | . The | restaurant | served | <num> | pies | and <num> | pizzas | yesterday | . How many | pies | were | served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-3 (1 samples using it): (119, 83, 123, 117, 62, 96, 28, 58, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 28 | 58 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> | placed | <num> | pencils | on the | desk | . How many | pencils | are | now | there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (1 samples using it): (119, 83, 123, 80, 28, 58, 62, 96, 104, 61, 109, 101, 103, 8, 61, 109, 101, 103, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 28 | 58 | 62 | 96 | 104 | 61 | 109 | 101 | 103 | 8 | 61 | 109 | 101 | 103 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | pennies | and <num> | nickels | in her | bank | . Her | dad | gave | her <num> | nickels | and her | mother | gave | her <num> | nickels | . How many | nickels | does | <PER_1> | have | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (119, 83, 123, 71, 12, 109, 101, 55, 50, 98, 55, 50, 98, 107, 51, 14, 87, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 71 | 12 | 109 | 101 | 55 | 50 | 98 | 55 | 50 | 98 | 107 | 51 | 14 | 87 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <unk> | <unk> | . <PER_1> | paid | $ <num> | for | <unk> | , $ <num> | for | apples | , and $ <num> | for | peaches | . In total | , how much | money | did | she | spend | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (1 samples using it): (119, 83, 123, 80, 25, 56, 98, 106, 88, 56, 98, 88, 101, 97, 105, 112, 79, 17, 65, 134)
| 119 | 83 | 123 | 80 | 25 | 56 | 98 | 106 | 88 | 56 | 98 | 88 | 101 | 97 | 105 | 112 | 79 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | purchased | a | football | game | for $ <num> | , a | <unk> | game | for $ <num> | , and a <MISC_1> | game | for $ <num> | . How much | did | <PER_1> | spend | on video | games | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (1 samples using it): (119, 83, 123, 129, 62, 96, 28, 58, 62, 96, 102, 83, 123, 25, 28, 58, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 129 | 62 | 96 | 28 | 58 | 62 | 96 | 102 | 83 | 123 | 25 | 28 | 58 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> | placed | <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are | now | there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (1 samples using it): (119, 83, 123, 117, 62, 96, 73, 129, 62, 96, 102, 83, 123, 80, 28, 58, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 73 | 129 | 62 | 96 | 102 | 83 | 123 | 80 | 28 | 58 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | in the | drawer | and <num> | crayons | on the | desk | . <PER_1> | placed | <num> | crayons | and <num> | scissors | on the | desk | . How many | crayons | are | now | there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (119, 83, 123, 80, 25, 98, 64, 81, 12, 109, 101, 50, 6, 57, 83, 123, 80, 39, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 25 | 98 | 64 | 81 | 12 | 109 | 101 | 50 | 6 | 57 | 83 | 123 | 80 | 39 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | gave | <PER_1> <num> new | baseball | cards | . <PER_1> | bought | <num> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (1 samples using it): (119, 83, 123, 80, 129, 62, 96, 102, 83, 123, 117, 62, 96, 98, 82, 92, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 129 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 98 | 82 | 92 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | football | games | this | month | . He | went | to <num> | games | last | month | , and | <unk> | to | go | to <num> | games | next | month | . How many | games | will | he | <unk> | in all | ? <eos> | TimeVariantUnknownFinal | ai2 |


## Sum (20 samples)
### Top-1 (3 samples using it): (119, 83, 123, 80, 57, 83, 123, 25, 8, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | onions | , <PER_2> | grew | <num> | onions | , and <PER_3> | grew | <num> | onions | . How many | onions | did | they | grow | in all | ? <eos> | Sum | ai2 |

### Top-2 (2 samples using it): (119, 83, 123, 39, 57, 83, 123, 25, 8, 83, 123, 48, 12, 109, 101, 58, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 39 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 48 | 12 | 109 | 101 | 58 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | onions | , <PER_2> | grew | <num> | onions | , and <PER_3> | grew | <num> | onions | . They | worked | for <num> | days | on the | farm | . How many | onions | did | they | grow | in total | ? <eos> | Sum | ai2 |

### Top-3 (1 samples using it): (119, 83, 123, 80, 57, 83, 123, 25, 8, 83, 123, 39, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | , <PER_2> | has | <num> | books | , and <PER_3> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Sum | ai2 |

### Top-4 (1 samples using it): (119, 83, 123, 80, 57, 83, 123, 25, 8, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | , <PER_2> | found | <num> | seashells | , and <PER_3> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Sum | ai2 |

### Top-5 (1 samples using it): (119, 83, 123, 39, 57, 83, 123, 25, 8, 83, 123, 117, 62, 96, 6, 40, 24, 60, 34, 46, 134)
| 119 | 83 | 123 | 39 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 117 | 62 | 96 | 6 | 40 | 24 | 60 | 34 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | plums | , <PER_2> | picked | <num> | plums | , and <PER_3> | picked | <num> | plums | from the | <unk> | tree | . How many | plums | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-6 (1 samples using it): (119, 83, 123, 80, 57, 83, 123, 25, 8, 83, 123, 117, 62, 96, 85, 3, 105, 37, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | pears | , <PER_2> | picked | <num> | pears | , and <PER_3> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-7 (1 samples using it): (119, 83, 123, 80, 57, 83, 123, 25, 8, 83, 123, 80, 28, 58, 62, 96, 85, 3, 105, 37, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 25 | 8 | 83 | 123 | 80 | 28 | 58 | 62 | 96 | 85 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | limes | , <PER_2> | picked | <num> | limes | , and <PER_3> | picked | <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-8 (1 samples using it): (74, 61, 77, 83, 123, 25, 113, 5, 118, 103, 68, 50, 98, 84, 113, 5, 40, 24, 23, 3, 105, 112, 79, 46, 134)
| 74 | 61 | 77 | 83 | 123 | 25 | 113 | 5 | 118 | 103 | 68 | 50 | 98 | 84 | 113 | 5 | 40 | 24 | 23 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | construction | company | <unk> | <num> | ton | of | <unk> | , <num> | ton | of | <unk> | , and <num> | ton | of | <unk> | . How many | tons | of | material | did | the | company <unk> | in all | ? <eos> | Sum | ai2 |

### Top-9 (1 samples using it): (119, 83, 123, 25, 121, 57, 83, 123, 25, 113, 5, 28, 58, 62, 96, 98, 84, 68, 6, 40, 24, 23, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 121 | 57 | 83 | 123 | 25 | 113 | 5 | 28 | 58 | 62 | 96 | 98 | 84 | 68 | 6 | 40 | 24 | 23 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | made | trail | mix | for a <unk> trip | . She | used | <num> | pound | of | peanuts | , <num> | pound | of chocolate | <unk> | , and <num> | pound | of | raisins | . How many | pounds | of trail | mix | did | <PER_1> | make | ? <eos> | Sum | ai2 |

### Top-10 (1 samples using it): (74, 61, 77, 83, 123, 117, 62, 96, 68, 26, 28, 58, 62, 96, 68, 80, 98, 117, 62, 96, 68, 80, 40, 24, 23, 24, 23, 3, 105, 37, 46, 134)
| 74 | 61 | 77 | 83 | 123 | 117 | 62 | 96 | 68 | 26 | 28 | 58 | 62 | 96 | 68 | 80 | 98 | 117 | 62 | 96 | 68 | 80 | 40 | 24 | 23 | 24 | 23 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <unk> | <num> | truck | - | load | of | sand | , <num> | truck | - | load | of | <unk> | , and <num> | truck | - | load | of | cement | . How many | truck | - | <unk> | of | material | were | needed | in all | ? <eos> | Sum | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (32 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | erasers | . She | loses | <num> | . How many | erasers | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-2 (13 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (11 samples using it): (119, 83, 123, 25, 118, 114, 121, 97, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 97 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-4 (11 samples using it): (119, 83, 123, 48, 12, 109, 101, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | candies | . <MISC_1> | has | <num> | . How many | candies | do | they | have | in all | ? <eos> | Addition | ilds |

### Top-5 (10 samples using it): (119, 83, 123, 25, 118, 114, 121, 132, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 118 | 114 | 121 | 132 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (7 samples using it): (119, 83, 123, 48, 12, 109, 101, 57, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 48 | 12 | 109 | 101 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <MISC_1> | . She | buys | <num> more | . Later , <PER_1> | buys | <num> | oranges | at the | store | . How many | <MISC_1> | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-7 (6 samples using it): (119, 83, 123, 25, 104, 61, 109, 101, 130, 3, 105, 112, 79, 44)
| 119 | 83 | 123 | 25 | 104 | 61 | 109 | 101 | 130 | 3 | 105 | 112 | 79 | 44 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects | <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-8 (6 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | orange | balloons | but | lost | <num> of them | . How many | orange | balloons | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-9 (5 samples using it): (119, 83, 123, 80, 48, 12, 109, 101, 40, 93, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 48 | 12 | 109 | 101 | 40 | 93 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 37, 17, 65, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 37 | 17 | 65 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |


## ai2 (316 samples)
### Top-1 (6 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-2 (4 samples using it): (119, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | books | . <PER_2> | has | <num> | books | . How many | books | do | they | have | together | ? <eos> | Addition | ai2 |

### Top-3 (4 samples using it): (119, 83, 123, 117, 62, 96, 102, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 117 | 62 | 96 | 102 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | crayons | in the | drawer | . <PER_1> | placed | <num> | crayons | in the | drawer | . How many | crayons | are | now | there | in total | ? <eos> | Addition | ai2 |

### Top-4 (4 samples using it): (119, 83, 123, 80, 28, 58, 62, 96, 104, 61, 77, 83, 123, 80, 110, 130, 3, 105, 112, 79, 124, 17, 65, 89, 49, 134)
| 119 | 83 | 123 | 80 | 28 | 58 | 62 | 96 | 104 | 61 | 77 | 83 | 123 | 80 | 110 | 130 | 3 | 105 | 112 | 79 | 124 | 17 | 65 | 89 | 49 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> tall | trees | currently in the | park | . Park | workers | will | plant | <num> short | trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-5 (3 samples using it): (119, 83, 123, 80, 57, 83, 123, 117, 62, 96, 85, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found | <num> | seashells | on the | beach | . How many | seashells | did | they | find | together | ? <eos> | Addition | ai2 |

### Top-6 (3 samples using it): (119, 83, 123, 71, 73, 39, 57, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 71 | 73 | 39 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | carrots | and <num> | watermelons | . <PER_2> | grew | <num> | carrots | . How many | carrots | did | they | grow | in all | ? <eos> | Addition | ai2 |

### Top-7 (3 samples using it): (119, 83, 123, 80, 57, 83, 123, 117, 62, 96, 85, 3, 105, 37, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 117 | 62 | 96 | 85 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | pears | and <PER_2> | picked | <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-8 (3 samples using it): (119, 83, 123, 39, 73, 71, 102, 83, 123, 39, 130, 3, 105, 112, 79, 46, 134)
| 119 | 83 | 123 | 39 | 73 | 71 | 102 | 83 | 123 | 39 | 130 | 3 | 105 | 112 | 79 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | watermelons | and <num> | turnips | . <ORG_1> | grew | <num> | watermelons | . How many | watermelons | did | they | grow | in total | ? <eos> | Addition | ai2 |

### Top-9 (3 samples using it): (119, 83, 123, 80, 57, 83, 123, 80, 57, 83, 123, 39, 130, 3, 105, 37, 46, 134)
| 119 | 83 | 123 | 80 | 57 | 83 | 123 | 80 | 57 | 83 | 123 | 39 | 130 | 3 | 105 | 37 | 46 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and <PER_2> | picked | <num> | oranges | . <PER_3> | picked | <num> | apples | . How many | oranges | were | picked | in all | ? <eos> | Addition | ai2 |

### Top-10 (3 samples using it): (119, 83, 123, 117, 62, 96, 104, 61, 109, 101, 103, 130, 3, 105, 112, 79, 4, 89)
| 119 | 83 | 123 | 117 | 62 | 96 | 104 | 61 | 109 | 101 | 103 | 130 | 3 | 105 | 112 | 79 | 4 | 89 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | nickels | in her | bank | . Her | dad | gave | her <num> | nickels | . How many | nickels | does | <PER_1> | have | now | ? <eos> | Addition | ai2 |


