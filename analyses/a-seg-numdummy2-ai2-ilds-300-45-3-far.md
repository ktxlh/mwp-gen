Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-numdummy2-ai2-ilds-300-45-3-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-numdummy2-ai2-ilds-300-45-3-far.txt
k=10
n=10
# Overall - top templates
### Top-1 (22 samples using it): (79, 80, 51, 120, 91, 35, 21, 91, 0, 118, 34, 4, 23)
| 79 | 80 | 51 | 120 | 91 | 35 | 21 | 91 | 0 | 118 | 34 | 4 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> with <MISC_1> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> with <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> to <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | another <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |

### Top-2 (12 samples using it): (79, 80, 51, 69, 15, 81, 111, 123, 2, 124, 125, 68)
| 79 | 80 | 51 | 69 | 15 | 81 | 111 | 123 | 2 | 124 | 125 | 68 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-3 (9 samples using it): (79, 80, 51, 120, 91, 35, 21, 91, 0, 118, 34, 4, 23, 68)
| 79 | 80 | 51 | 120 | 91 | 35 | 21 | 91 | 0 | 118 | 34 | 4 | 23 | 68 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | another <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | another <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more from <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> more from <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more from <MISC_1> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-4 (8 samples using it): (79, 80, 51, 120, 91, 35, 21, 91, 0, 127, 124, 125, 68)
| 79 | 80 | 51 | 120 | 91 | 35 | 21 | 91 | 0 | 127 | 124 | 125 | 68 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . He | <unk> | <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . He | <unk> | <num> to <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . He | <unk> | <num> to <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . He | <unk> | <num> to <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> with <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |

### Top-5 (7 samples using it): (79, 69, 15, 81, 111, 123, 80, 51, 120, 91, 0, 69, 15, 81, 58, 23)
| 79 | 69 | 15 | 81 | 111 | 123 | 80 | 51 | 120 | 91 | 0 | 69 | 15 | 81 | 58 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <ORG_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-6 (7 samples using it): (79, 69, 15, 81, 21, 45, 87, 81, 21, 69, 15, 81, 21, 97, 91, 0, 118, 87, 23)
| 79 | 69 | 15 | 81 | 21 | 45 | 87 | 81 | 21 | 69 | 15 | 81 | 21 | 97 | 91 | 0 | 118 | 87 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in all | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there in all | ? <eos> | Addition | ai2 |

### Top-7 (6 samples using it): (79, 80, 51, 120, 91, 0, 81, 21, 91, 0, 118, 34, 4, 23)
| 79 | 80 | 51 | 120 | 91 | 0 | 81 | 21 | 91 | 0 | 118 | 34 | 4 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (79, 80, 51, 120, 91, 0, 91, 0, 118, 34, 4, 23)
| 79 | 80 | 51 | 120 | 91 | 0 | 91 | 0 | 118 | 34 | 4 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |

### Top-9 (5 samples using it): (79, 80, 51, 120, 91, 80, 51, 120, 91, 0, 56, 124, 125, 68)
| 79 | 80 | 51 | 120 | 91 | 80 | 51 | 120 | 91 | 0 | 56 | 124 | 125 | 68 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many more | <unk> | <unk> | <PER_2> | <unk> | ? <eos> | Subtraction | ilds |

### Top-10 (5 samples using it): (79, 80, 51, 120, 91, 80, 51, 120, 91, 0, 69, 15, 81, 58, 23)
| 79 | 80 | 51 | 120 | 91 | 80 | 51 | 120 | 91 | 0 | 69 | 15 | 81 | 58 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <ORG_1> | <unk> | <num> | <unk> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |


