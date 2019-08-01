Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-numdummy-ai2-ilds-300-45-3-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-numdummy-ai2-ilds-300-45-3-far.txt
k=10
n=10
# Overall - top templates
### Top-1 (46 samples using it): (117, 83, 40, 134, 43, 80, 112, 1, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 134 | 43 | 80 | 112 | 1 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <PER_2> | . <PER_3> | <unk> | <num> away | . How many | <MISC_1> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> away | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> with <MISC_1> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-2 (10 samples using it): (117, 83, 40, 134, 43, 80, 112, 1, 129, 128, 27, 30, 66, 23)
| 117 | 83 | 40 | 134 | 43 | 80 | 112 | 1 | 129 | 128 | 27 | 30 | 66 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | another <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | another <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more from <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> more from <PER_2> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> more from <MISC_1> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-3 (8 samples using it): (117, 83, 40, 81, 42, 19, 110, 93, 128, 27, 30, 113)
| 117 | 83 | 40 | 81 | 42 | 19 | 110 | 93 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (7 samples using it): (117, 83, 40, 84, 14, 83, 40, 84, 1, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 84 | 14 | 83 | 40 | 84 | 1 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many more | <unk> | <unk> | <PER_2> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <MISC_1> | , but she | <unk> | <num> | <MISC_1> | . How many | <MISC_1> | <unk> | she | <unk> | now ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many more | <unk> | <unk> | <PER_1> | <unk> than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-5 (7 samples using it): (117, 83, 40, 134, 107, 43, 80, 112, 1, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 134 | 107 | 43 | 80 | 112 | 1 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | but | <unk> | <num> of them | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | now ? <eos> | Subtraction | ai2 |
| <PER_1> | <unk> | <num> | <unk> | <unk> | . He | <unk> | <num> more than <PER_2> | . How many <unk> | <unk> | <unk> | <PER_2> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . She | <unk> | another <num> | . How many <unk> | <unk> | <unk> | <ORG_1> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . <PER_2> | <unk> | <num> away | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . She | <unk> | <num> with <PER_2> | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . He | <unk> | <num> more from <PER_2> | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . He | <unk> | <num> more from <PER_2> | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Addition | ilds |

### Top-6 (7 samples using it): (117, 83, 40, 84, 14, 83, 40, 134, 43, 80, 112, 1, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 84 | 14 | 83 | 40 | 134 | 43 | 80 | 112 | 1 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . He | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <MISC_1> | . <PER_2> | <unk> | <num> | <MISC_1> | . He | <unk> | <num> | . How many | <MISC_1> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . She | <unk> | <num> with <PER_3> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . He | <unk> | <num> with <PER_3> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | another <num> | . How many | <unk> | <unk> | <PER_2> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | another <num> | . How many | <unk> | <unk> | <PER_2> | <unk> | with ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | with <num> | <unk> | . <PER_2> | <unk> | another <num> | . How many | <unk> | <unk> | <PER_2> | <unk> | with ? <eos> | Addition | ilds |

### Top-7 (7 samples using it): (117, 83, 40, 134, 41, 84, 21, 19, 14, 83, 40, 134, 21, 19, 46, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 134 | 41 | 84 | 21 | 19 | 14 | 83 | 40 | 134 | 21 | 19 | 46 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in all | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total | ? <eos> | Addition | ai2 |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in all | ? <eos> | Addition | ai2 |

### Top-8 (6 samples using it): (117, 83, 40, 134, 43, 38, 80, 42, 19, 46, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 134 | 43 | 38 | 80 | 42 | 19 | 46 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |
| <PER_1> | <unk> | with <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | with ? <eos> | Subtraction | ilds |

### Top-9 (6 samples using it): (117, 83, 40, 134, 61, 6, 18, 112, 1, 129, 128, 27, 30, 113)
| 117 | 83 | 40 | 134 | 61 | 6 | 18 | 112 | 1 | 129 | 128 | 27 | 30 | 113 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-10 (6 samples using it): (117, 83, 40, 134, 41, 84, 14, 83, 40, 84, 1, 129, 128, 27, 30, 66, 23)
| 117 | 83 | 40 | 134 | 41 | 84 | 14 | 83 | 40 | 84 | 1 | 129 | 128 | 27 | 30 | 66 | 23 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <ORG_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <MISC_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |


