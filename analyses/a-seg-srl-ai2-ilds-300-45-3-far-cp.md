Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-45-3-far-cp.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-45-3-far-cp.txt
k=10
n=1
# Overall - top templates
### Top-1 (21 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-2 (14 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-3 (10 samples using it): (95, 27, 53, 110, 125, 99, 88, 59, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-5 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-6 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-7 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-8 (4 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 40, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in each | <unk> | . How many | <unk> | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-9 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 4, 84, 23, 107)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 4 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | ? <eos> | Subtraction | ilds |

### Top-10 (4 samples using it): (95, 27, 53, 110, 0, 75, 132, 96, 109, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 0 | 75 | 132 | 96 | 109 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (21 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-2 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-3 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-4 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-5 (3 samples using it): (95, 27, 53, 110, 90, 63, 85, 97, 127, 84, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 63 | 85 | 97 | 127 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . <num> | <unk> more | <unk> | <unk> | . How many | <unk> | there total | ? <eos> | Addition | ilds |

### Top-6 (3 samples using it): (95, 27, 53, 110, 90, 18, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 18 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-7 (14 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-8 (1 samples using it): (95, 63, 85, 97, 49, 9, 22, 43, 49, 9, 75, 132, 107)
| 95 | 63 | 85 | 97 | 49 | 9 | 22 | 43 | 49 | 9 | 75 | 132 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | <unk> | <unk> | <unk> | . <num> more | <unk> | <unk> | to <unk> | . How many | <unk> | <unk> | <unk> | ? <eos> | Addition | ilds |

### Top-9 (1 samples using it): (95, 27, 53, 110, 125, 99, 122, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 122 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> red | <unk> | and <num> | blue | <unk> | . How many | <unk> | <unk> | she | <unk> | altogether | ? <eos> | Addition | ilds |

### Top-10 (1 samples using it): (95, 27, 53, 110, 125, 99, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> red | <unk> | and <num> blue | <unk> | . How many | <unk> | <unk> | she | <unk> | altogether | ? <eos> | Addition | ilds |


## Subtraction (257 samples)
### Top-1 (14 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-2 (21 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-3 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 4, 84, 23, 107)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 4 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | ? <eos> | Subtraction | ilds |

### Top-4 (4 samples using it): (95, 27, 53, 110, 0, 75, 132, 96, 109, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 0 | 75 | 132 | 96 | 109 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-5 (3 samples using it): (95, 27, 53, 110, 4, 57, 39, 56, 23, 121, 132, 31, 97, 53, 110, 10)
| 95 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 121 | 132 | 31 | 97 | 53 | 110 | 10 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . How many more | <unk> | <unk> | <PER_1> | <unk> | to | <unk> | to | <unk> | <num> | <unk> | ? <eos> | Subtraction | ilds |

### Top-6 (2 samples using it): (95, 27, 53, 110, 31, 97, 53, 110, 82, 39, 56, 23, 121, 132, 107)
| 95 | 27 | 53 | 110 | 31 | 97 | 53 | 110 | 82 | 39 | 56 | 23 | 121 | 132 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and | <unk> | <num> | <unk> | . How much <unk> | <unk> | <PER_1> | <unk> | than | <unk> | ? <eos> | Subtraction | ai2 |

### Top-7 (2 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How much <unk> | <unk> | <PER_1> | than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-8 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-9 (10 samples using it): (95, 27, 53, 110, 125, 99, 88, 59, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-10 (1 samples using it): (95, 27, 53, 110, 125, 99, 4, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 4 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and <num> | <unk> | . How many more | <unk> | <unk> | there | than <unk> | ? <eos> | Subtraction | ilds |


## CommonDiv (95 samples)
### Top-1 (10 samples using it): (95, 27, 53, 110, 125, 99, 88, 59, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-2 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-3 (1 samples using it): (95, 27, 53, 110, 71, 82, 39, 56, 23, 121, 132, 107)
| 95 | 27 | 53 | 110 | 71 | 82 | 39 | 56 | 23 | 121 | 132 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | for $ <num> | . How much | <unk> | each | <unk> <unk> | to | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (1 samples using it): (95, 27, 98, 47, 72, 81, 32, 49, 9, 40, 96, 109, 15)
| 95 | 27 | 98 | 47 | 72 | 81 | 32 | 49 | 9 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> <PER_1> | <unk> | <num> | <unk> | <unk> | equally into <num> | <unk> | . How many | <unk> | <unk> | in each | <unk> | ? <eos> | CommonDiv | ilds |


## Multiplication (93 samples)
### Top-1 (4 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 40, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in each | <unk> | . How many | <unk> | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-2 (3 samples using it): (95, 27, 80, 20, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 80 | 20 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | for <num> | <unk> | at <num> | miles | per hour | . How far | <unk> | <PER_1> | <unk> | ? <eos> | Multiplication | ilds |

### Top-3 (2 samples using it): (95, 18, 117, 35, 127, 129, 11, 103, 23, 107)
| 95 | 18 | 117 | 35 | 127 | 129 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | <unk> | $ <num> | . How much | <unk> | <num> | <unk> | <unk> | ? <eos> | Multiplication | ilds |

### Top-4 (2 samples using it): (95, 18, 27, 53, 110, 4, 57, 39, 11, 103, 23, 107)
| 95 | 18 | 27 | 53 | 110 | 4 | 57 | 39 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <num> | <unk> | <unk> | ? <eos> | Multiplication | ilds |

### Top-5 (2 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 6, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | every | hour | . How many | miles | <unk> | he | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-6 (1 samples using it): (95, 18, 117, 53, 110, 82, 39, 11, 103, 23, 107)
| 95 | 18 | 117 | 53 | 110 | 82 | 39 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> | ? <eos> | Multiplication | ilds |

### Top-7 (1 samples using it): (95, 18, 117, 53, 110, 4, 57, 40, 96, 109, 15)
| 95 | 18 | 117 | 53 | 110 | 4 | 57 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-8 (1 samples using it): (95, 27, 8, 131, 90, 18, 117, 53, 110, 10)
| 95 | 27 | 8 | 131 | 90 | 18 | 117 | 53 | 110 | 10 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| How much | <unk> | <num> | <unk> of <unk> <unk> | <unk> <unk> each | <unk> | <unk> | <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-9 (1 samples using it): (95, 18, 117, 35, 59, 39, 56, 23, 6, 109, 15)
| 95 | 18 | 117 | 35 | 59 | 39 | 56 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If each | <unk> | <unk> | $ <num> | , how much | <unk> | <PER_1> | <unk> | for <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-10 (1 samples using it): (95, 27, 53, 110, 90, 18, 27, 53, 110, 4, 57, 84, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 18 | 27 | 53 | 110 | 4 | 57 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . Each | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | there | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)

## Sum (20 samples)

# Dataset - top templates
## ilds (449 samples)
### Top-1 (21 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-2 (14 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-3 (10 samples using it): (95, 27, 53, 110, 125, 99, 88, 59, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-5 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-6 (4 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 40, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in each | <unk> | . How many | <unk> | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-7 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 4, 84, 23, 107)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 4 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | ? <eos> | Subtraction | ilds |

### Top-8 (4 samples using it): (95, 27, 53, 110, 0, 75, 132, 96, 109, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 0 | 75 | 132 | 96 | 109 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-9 (3 samples using it): (95, 27, 53, 110, 90, 63, 85, 97, 127, 84, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 63 | 85 | 97 | 127 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . <num> | <unk> more | <unk> | <unk> | . How many | <unk> | there total | ? <eos> | Addition | ilds |

### Top-10 (3 samples using it): (95, 27, 80, 20, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 80 | 20 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | for <num> | <unk> | at <num> | miles | per hour | . How far | <unk> | <PER_1> | <unk> | ? <eos> | Multiplication | ilds |


## ai2 (316 samples)
### Top-1 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-2 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-3 (2 samples using it): (95, 27, 53, 110, 31, 97, 53, 110, 82, 39, 56, 23, 121, 132, 107)
| 95 | 27 | 53 | 110 | 31 | 97 | 53 | 110 | 82 | 39 | 56 | 23 | 121 | 132 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and | <unk> | <num> | <unk> | . How much <unk> | <unk> | <PER_1> | <unk> | than | <unk> | ? <eos> | Subtraction | ai2 |

### Top-4 (1 samples using it): (95, 27, 53, 110, 35, 75, 132, 4, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 35 | 75 | 132 | 4 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | but <num> | <unk> | <unk> | . How many <unk> | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (95, 27, 53, 110, 88, 0, 27, 53, 110, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 88 | 0 | 27 | 53 | 110 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | tall | . Then she | <unk> | <num> | <unk> | <unk> | . How tall | <unk> | <PER_1> | now | ? <eos> | Addition | ai2 |

### Top-6 (1 samples using it): (95, 27, 53, 110, 116, 18, 117, 53, 110, 4, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 116 | 18 | 117 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ai2 |

### Top-7 (2 samples using it): (95, 27, 53, 110, 28, 72, 81, 122, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 122 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and | <unk> | <PER_2> <num> of the | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | Subtraction | ai2 |

### Top-8 (1 samples using it): (95, 18, 117, 53, 110, 51, 109, 35, 32, 49, 9, 84, 23, 38, 55)
| 95 | 18 | 117 | 53 | 110 | 51 | 109 | 35 | 32 | 49 | 9 | 84 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <num> | <unk> | during | <unk> | and <num> during dinner | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? <eos> | Addition | ai2 |

### Top-9 (1 samples using it): (95, 27, 98, 47, 102, 31, 97, 81, 49, 9, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 98 | 47 | 102 | 31 | 97 | 81 | 49 | 9 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | but | <unk> | <num> of them | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | Subtraction | ai2 |

### Top-10 (1 samples using it): (95, 27, 53, 110, 31, 97, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 31 | 97 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> blue | <unk> | but | <unk> | <num> of them | . How many blue | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | Subtraction | ai2 |


