Namespace(a_gen=False, a_seg=True, data='/Users/shanglinghsu/mwp/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/', gen_fi='', pure='', tagged_fi='/Users/shanglinghsu/mwp/ntg2/segs/seg-srl-ai2-ilds-300-45-3-far-cp.txt')
# Analysis on segmentation
metadata_path=/Users/shanglinghsu/mwp/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated//metadata_train.tsv
seg_path=/Users/shanglinghsu/mwp/ntg2/segs/seg-srl-ai2-ilds-300-45-3-far-cp.txt
k=10
n=1
# Overall - top templates
### Top-1 (32 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
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

### Top-4 (10 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-5 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-7 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-8 (6 samples using it): (95, 27, 53, 110, 90, 18, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 18 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-9 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 0, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 0 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> more | . Later , <PER_1> | <unk> | <num> | <unk> | at the | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 51, 109, 94, 57, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . There | <unk> | <num> | <unk> | on each | <unk> | . How many | <unk> | <unk> | there | in all | ? <eos> | Multiplication | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (32 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-2 (10 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-3 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-4 (6 samples using it): (95, 27, 53, 110, 90, 18, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 18 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-5 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 0, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 0 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> more | . Later , <PER_1> | <unk> | <num> | <unk> | at the | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-6 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-7 (5 samples using it): (95, 27, 98, 47, 102, 28, 72, 81, 49, 9, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 98 | 47 | 102 | 28 | 72 | 81 | 49 | 9 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | . He | <unk> | <num> more | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (95, 27, 53, 110, 125, 99, 51, 109, 73, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now | there | in total | ? <eos> | Addition | ai2 |

### Top-9 (4 samples using it): (95, 27, 53, 110, 125, 99, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |

### Top-10 (4 samples using it): (95, 27, 98, 47, 125, 99, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 98 | 47 | 125 | 99 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <ORG_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |


## Subtraction (257 samples)
### Top-1 (32 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | with | ? <eos> | Subtraction | ilds |

### Top-2 (14 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . She | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-3 (5 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 51, 109, 73, 27, 53, 110, 83, 96, 109, 49, 9, 75, 132, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 83 | 96 | 109 | 49 | 9 | 75 | 132 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | in a | <unk> | . <PER_2> | <unk> | <num> | <unk> | out | of the | <unk> | . How many | <unk> | <unk> | <unk> | in the | <unk> | ? <eos> | Subtraction | ilds |

### Top-4 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 4, 84, 23, 107)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 4 | 84 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | ? <eos> | Subtraction | ilds |

### Top-5 (4 samples using it): (95, 27, 53, 110, 0, 75, 132, 96, 109, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 0 | 75 | 132 | 96 | 109 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <num> | <unk> | <unk> | by a | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-6 (4 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . He | <unk> | <num> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |

### Top-7 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 117, 80, 20, 51, 109, 49, 9, 75, 132, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 117 | 80 | 20 | 51 | 109 | 49 | 9 | 75 | 132 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | from a | <unk> | . There | <unk> | originally <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | <unk> | in the | <unk> | ? <eos> | Subtraction | ilds |

### Top-8 (3 samples using it): (95, 27, 53, 110, 4, 57, 39, 56, 23, 121, 132, 31, 97, 53, 110, 10)
| 95 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 121 | 132 | 31 | 97 | 53 | 110 | 10 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . How many more | <unk> | <unk> | <PER_1> | <unk> | to | <unk> | to | <unk> | <num> | <unk> | ? <eos> | Subtraction | ilds |

### Top-9 (3 samples using it): (95, 27, 98, 47, 102, 28, 72, 81, 34, 32, 49, 9, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 98 | 47 | 102 | 28 | 72 | 81 | 34 | 32 | 49 | 9 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | . <PER_2> | <unk> | <num> of <PER_1> <PER_3> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (95, 27, 98, 47, 125, 99, 51, 109, 28, 72, 81, 34, 111, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 98 | 47 | 125 | 99 | 51 | 109 | 28 | 72 | 81 | 34 | 111 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | on the | <unk> | . She | <unk> | <num> of the | <unk> | to <PER_2> | . How many | <unk> | <unk> | <PER_1> now | <unk> | ? <eos> | Subtraction | ai2 |


## CommonDiv (95 samples)
### Top-1 (10 samples using it): (95, 27, 53, 110, 125, 99, 88, 59, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | at <num> | <unk> | per hour | , how long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-2 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-3 (4 samples using it): (95, 27, 53, 110, 88, 49, 9, 80, 20, 104, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 88 | 49 | 9 | 80 | 20 | 104 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | of <LOC_1> | . How many | cases | of <num> | <unk> | , plus extra | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-4 (4 samples using it): (95, 27, 53, 110, 28, 72, 81, 34, 104, 57, 39, 11, 103, 23, 107)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 34 | 104 | 57 | 39 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . If he | <unk> | them among <num> | <unk> | , how many | <unk> | <unk> | each | friend | <unk> | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (95, 27, 98, 47, 42, 96, 109, 73, 27, 53, 110, 104, 57, 84, 23, 6, 109, 15)
| 95 | 27 | 98 | 47 | 42 | 96 | 109 | 73 | 27 | 53 | 110 | 104 | 57 | 84 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | in | <unk> | . If there | <unk> | <num> | <unk> | , how many | <unk> | <unk> | <unk> | in each | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (95, 27, 98, 47, 111, 34, 122, 90, 63, 85, 97, 35, 32, 59, 39, 56, 23, 107)
| 95 | 27 | 98 | 47 | 111 | 34 | 122 | 90 | 63 | 85 | 97 | 35 | 32 | 59 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in <PER_1> 's | <unk> | <unk> | . If the | <unk> | <unk> | <unk> | into <num> | <unk> | , how big | <unk> | each | <unk> | ? <eos> | CommonDiv | ilds |

### Top-7 (4 samples using it): (95, 27, 66, 109, 73, 27, 98, 47, 111, 34, 111, 34, 73, 117, 80, 12, 31, 97, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 66 | 109 | 73 | 27 | 98 | 47 | 111 | 34 | 111 | 34 | 73 | 117 | 80 | 12 | 31 | 97 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to <PER_2> 's | <unk> | . It | <unk> | <num> | miles | from <PER_1> 's | <unk> | to <PER_2> 's | <unk> | . It | <unk> | <PER_1> <num> | <unk> | to | <unk> | there | . How fast | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-8 (3 samples using it): (95, 27, 53, 110, 88, 59, 114, 57, 39, 56, 23, 6, 109, 15)
| 95 | 27 | 53 | 110 | 88 | 59 | 114 | 57 | 39 | 56 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | <num> | <unk> | of <MISC_1> | , how many cases | of <num> | <unk> | <unk> | <MISC_2> | pickup | from the <unk> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-9 (3 samples using it): (95, 18, 117, 53, 110, 51, 109, 73, 27, 53, 110, 4, 57, 39, 56, 23, 107)
| 95 | 18 | 117 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <unk> | <num> | <unk> | to a | <unk> | . He | <unk> | <num> | <unk> | . How many | <unk> | <unk> | each friend | <unk> | ? <eos> | CommonDiv | ilds |

### Top-10 (3 samples using it): (95, 27, 53, 110, 51, 109, 125, 99, 90, 63, 85, 97, 81, 122, 59, 129, 11, 103, 23, 107)
| 95 | 27 | 53 | 110 | 51 | 109 | 125 | 99 | 90 | 63 | 85 | 97 | 81 | 122 | 59 | 129 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | and <num> | <unk> | . If the | <unk> | <unk> | <unk> | equally among the | <unk> | , how many | <unk> | each | <unk> | <unk> | ? <eos> | CommonDiv | ilds |


## Multiplication (93 samples)
### Top-1 (4 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 40, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 40 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in each | <unk> | . How many | <unk> | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-2 (4 samples using it): (95, 27, 80, 20, 31, 97, 66, 109, 125, 99, 69, 47, 82, 39, 56, 66, 109, 66, 109, 15)
| 95 | 27 | 80 | 20 | 31 | 97 | 66 | 109 | 125 | 99 | 69 | 47 | 82 | 39 | 56 | 66 | 109 | 66 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | <unk> | <PER_1> <num> | <unk> | to | <unk> | to <PER_2> 's | <unk> | at <num> | miles | per | hour | . How far | <unk> | it | between <PER_1> 's | <unk> | and <PER_2> 's | <unk> | ? <eos> | Multiplication | ilds |

### Top-3 (3 samples using it): (95, 27, 80, 20, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 80 | 20 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | <unk> | for <num> | <unk> | at <num> | miles | per hour | . How far | <unk> | <PER_1> | <unk> | ? <eos> | Multiplication | ilds |

### Top-4 (3 samples using it): (95, 27, 53, 110, 69, 32, 90, 18, 117, 53, 110, 4, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 69 | 32 | 90 | 18 | 117 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | of | <unk> | . Each | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Multiplication | ilds |

### Top-5 (3 samples using it): (95, 27, 53, 110, 69, 32, 90, 18, 117, 53, 110, 118, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 69 | 32 | 90 | 18 | 117 | 53 | 110 | 118 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> | <unk> | <num> | <unk> | of | <unk> | . Each | <unk> | <unk> | <num> | <unk> | and there | <unk> | <num> | <unk> | in a | <unk> | . How many | <unk> | <unk> | <ORG_1> | <unk> | ? <eos> | Multiplication | ilds |

### Top-6 (2 samples using it): (95, 18, 117, 35, 127, 129, 11, 103, 23, 107)
| 95 | 18 | 117 | 35 | 127 | 129 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | <unk> | $ <num> | . How much | <unk> | <num> | <unk> | <unk> | ? <eos> | Multiplication | ilds |

### Top-7 (2 samples using it): (95, 18, 27, 53, 110, 4, 57, 39, 11, 103, 23, 107)
| 95 | 18 | 27 | 53 | 110 | 4 | 57 | 39 | 11 | 103 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <num> | <unk> | <unk> | ? <eos> | Multiplication | ilds |

### Top-8 (2 samples using it): (95, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 6, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | every | hour | . How many | miles | <unk> | he | <unk> | in <num> | <unk> | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (95, 18, 27, 53, 110, 118, 27, 53, 110, 104, 57, 84, 23, 33, 55)
| 95 | 18 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 104 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | <unk> | <num> | <unk> | . If there | <unk> | <num> | <unk> | , how many | <unk> | <unk> | there | in total | ? <eos> | Multiplication | ilds |

### Top-10 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 51, 109, 94, 57, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . There | <unk> | <num> | <unk> | on each | <unk> | . How many | <unk> | <unk> | there | in all | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (2 samples using it): (95, 27, 53, 110, 51, 109, 125, 99, 51, 109, 73, 27, 53, 110, 125, 99, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 51 | 109 | 125 | 99 | 51 | 109 | 73 | 27 | 53 | 110 | 125 | 99 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | and <num> | <unk> | on the | <unk> | . <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | now | there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-2 (1 samples using it): (95, 27, 53, 110, 51, 109, 90, 18, 117, 80, 20, 116, 18, 117, 80, 20, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 51 | 109 | 90 | 18 | 117 | 80 | 20 | 116 | 18 | 117 | 80 | 20 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | in her | <unk> | . Her | <unk> | <unk> | her <num> | <unk> | and her | <unk> | <unk> | her <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-3 (1 samples using it): (95, 18, 117, 53, 110, 69, 47, 125, 99, 90, 18, 117, 53, 110, 125, 99, 122, 49, 9, 84, 23, 33, 55)
| 95 | 18 | 117 | 53 | 110 | 69 | 47 | 125 | 99 | 90 | 18 | 117 | 53 | 110 | 125 | 99 | 122 | 49 | 9 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <num> | <unk> | during | <unk> | and <num> during dinner | <unk> | . The | <unk> | <unk> | <num> | <unk> | and <num> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (1 samples using it): (95, 27, 53, 110, 51, 109, 125, 99, 51, 109, 73, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 51 | 109 | 125 | 99 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | and <num> | <unk> | on the | <unk> | . <PER_1> | <unk> | <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | now | there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (95, 27, 98, 47, 125, 99, 51, 109, 90, 18, 117, 80, 20, 116, 18, 117, 80, 20, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 98 | 47 | 125 | 99 | 51 | 109 | 90 | 18 | 117 | 80 | 20 | 116 | 18 | 117 | 80 | 20 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | in her | <unk> | . Her | <unk> | <unk> | her <num> | <unk> | and her | <unk> | <unk> | her <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (1 samples using it): (95, 27, 53, 110, 118, 117, 35, 32, 26, 92, 71, 51, 109, 45, 104, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 118 | 117 | 35 | 32 | 26 | 92 | 71 | 51 | 109 | 45 | 104 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <unk> | <unk> | . <PER_1> | <unk> | $ <num> for | <unk> | , $ <num> for | <unk> | , and $ <num> | for | <unk> | . In total | , how much | <unk> | <unk> | she | <unk> | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (1 samples using it): (95, 27, 98, 47, 122, 71, 26, 34, 122, 71, 26, 92, 71, 82, 39, 56, 23, 6, 109, 38, 55)
| 95 | 27 | 98 | 47 | 122 | 71 | 26 | 34 | 122 | 71 | 26 | 92 | 71 | 82 | 39 | 56 | 23 | 6 | 109 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | a | <unk> | <unk> | for $ <num> | , a | <unk> | <unk> | for $ <num> | , and a <MISC_1> | <unk> | for $ <num> | . How much | <unk> | <PER_1> | <unk> | on | <unk> | <unk> | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (1 samples using it): (95, 27, 98, 47, 122, 71, 75, 132, 28, 72, 81, 34, 122, 73, 27, 98, 47, 122, 49, 9, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 98 | 47 | 122 | 71 | 75 | 132 | 28 | 72 | 81 | 34 | 122 | 73 | 27 | 98 | 47 | 122 | 49 | 9 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | , and <num> | <unk> | <unk> | . <PER_2> | <unk> | <PER_1> <num> new | <unk> | <unk> | . <PER_1> | <unk> | <num> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (95, 27, 80, 20, 102, 96, 109, 73, 117, 80, 20, 69, 47, 116, 117, 76, 97, 80, 20, 69, 32, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 80 | 20 | 102 | 96 | 109 | 73 | 117 | 80 | 20 | 69 | 47 | 116 | 117 | 76 | 97 | 80 | 20 | 69 | 32 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to <num> | <unk> | <unk> | this | <unk> | . He | <unk> | to <num> | <unk> | last | <unk> | , and | <unk> | to | <unk> | to <num> | <unk> | next | <unk> | . How many | <unk> | <unk> | he | <unk> | in all | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (1 samples using it): (95, 27, 53, 110, 118, 117, 12, 71, 26, 92, 71, 116, 117, 80, 20, 45, 59, 39, 56, 23, 6, 109, 15)
| 95 | 27 | 53 | 110 | 118 | 117 | 12 | 71 | 26 | 92 | 71 | 116 | 117 | 80 | 20 | 45 | 59 | 39 | 56 | 23 | 6 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | some | <unk> | . He | <unk> | <unk> | for $ <num> | , a | <unk> | for $ <num> | , and | <unk> | $ <num> on a | <unk> | . In total | , how much | <unk> | <PER_1> | <unk> | on | <unk> | ? <eos> | TimeVariantUnknownFinal | ai2 |


## Sum (20 samples)
### Top-1 (3 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Sum | ai2 |

### Top-2 (2 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 118, 117, 80, 20, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 118 | 117 | 80 | 20 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | . They | <unk> | for <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Sum | ai2 |

### Top-3 (1 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Sum | ai2 |

### Top-4 (1 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Sum | ai2 |

### Top-5 (1 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 51, 109, 32, 49, 9, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 51 | 109 | 32 | 49 | 9 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | from the | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | in total | ? <eos> | Sum | ai2 |

### Top-6 (1 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 53, 110, 51, 109, 94, 57, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | from the pear | <unk> | . How many | <unk> | <unk> | <unk> | in total | ? <eos> | Sum | ai2 |

### Top-7 (1 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 116, 27, 98, 47, 125, 99, 51, 109, 94, 57, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 116 | 27 | 98 | 47 | 125 | 99 | 51 | 109 | 94 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , <PER_2> | <unk> | <num> | <unk> | , and <PER_3> | <unk> | <num> | <unk> | and <num> | <unk> | , at the | <unk> | . How many | <unk> | <unk> | <unk> | in total | ? <eos> | Sum | ai2 |

### Top-8 (1 samples using it): (95, 108, 18, 117, 98, 20, 69, 102, 125, 99, 69, 32, 26, 92, 24, 32, 49, 9, 114, 57, 39, 11, 103, 23, 33, 55)
| 95 | 108 | 18 | 117 | 98 | 20 | 69 | 102 | 125 | 99 | 69 | 32 | 26 | 92 | 24 | 32 | 49 | 9 | 114 | 57 | 39 | 11 | 103 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <unk> | <num> | <unk> | of | <unk> | , <num> | <unk> | of | <unk> | , and <num> | <unk> | of | <unk> | . How many | <unk> | of | <unk> | <unk> | the | <unk> | <unk> | in all | ? <eos> | Sum | ai2 |

### Top-9 (1 samples using it): (95, 27, 53, 12, 51, 109, 73, 27, 53, 110, 69, 32, 26, 92, 24, 32, 26, 92, 24, 32, 49, 9, 114, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 12 | 51 | 109 | 73 | 27 | 53 | 110 | 69 | 32 | 26 | 92 | 24 | 32 | 26 | 92 | 24 | 32 | 49 | 9 | 114 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <unk> | <unk> | for a <unk> | <unk> | . She | <unk> | <num> | <unk> | of | <unk> | , <num> | <unk> | of <unk> | <unk> | , and <num> | <unk> | of | <unk> | . How many | <unk> | of <unk> | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Sum | ai2 |

### Top-10 (1 samples using it): (95, 108, 18, 27, 53, 110, 69, 47, 69, 102, 125, 99, 69, 47, 69, 32, 26, 92, 24, 47, 69, 32, 49, 9, 114, 9, 114, 57, 84, 23, 33, 55)
| 95 | 108 | 18 | 27 | 53 | 110 | 69 | 47 | 69 | 102 | 125 | 99 | 69 | 47 | 69 | 32 | 26 | 92 | 24 | 47 | 69 | 32 | 49 | 9 | 114 | 9 | 114 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | <unk> | <num> | <unk> | - | <unk> | of | <unk> | , <num> | <unk> | - | <unk> | of | <unk> | , and <num> | <unk> | - | <unk> | of | <unk> | . How many | <unk> | - | <unk> | of | <unk> | <unk> | <unk> | in all | ? <eos> | Sum | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (32 samples using it): (95, 27, 80, 20, 28, 72, 81, 94, 57, 39, 56, 23, 38, 55)
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

### Top-4 (10 samples using it): (95, 27, 53, 110, 28, 72, 81, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <MISC_1> | <unk> | <num> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ilds |

### Top-5 (8 samples using it): (95, 27, 53, 110, 125, 99, 88, 82, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 125 | 99 | 88 | 82 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per hour | . How long | <unk> | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (6 samples using it): (95, 27, 53, 110, 90, 18, 72, 81, 94, 57, 39, 56, 23, 107)
| 95 | 27 | 53 | 110 | 90 | 18 | 72 | 81 | 94 | 57 | 39 | 56 | 23 | 107 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_1> 's | <unk> | <unk> | <PER_1> <num> more | . How many | <unk> | <unk> | <PER_1> | <unk> | ? <eos> | Addition | ilds |

### Top-7 (6 samples using it): (95, 27, 53, 110, 28, 72, 81, 0, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 28 | 72 | 81 | 0 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . He | <unk> | <num> more | . Later , <PER_1> | <unk> | <num> | <unk> | at the | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (95, 27, 98, 47, 102, 28, 72, 81, 49, 9, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 98 | 47 | 102 | 28 | 72 | 81 | 49 | 9 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | . He | <unk> | <num> more | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | in all | ? <eos> | Addition | ilds |

### Top-9 (5 samples using it): (95, 27, 80, 20, 102, 28, 72, 81, 49, 9, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 80 | 20 | 102 | 28 | 72 | 81 | 49 | 9 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | with <num> | <unk> | <unk> | . She | <unk> | another <num> | . How many | <unk> | <unk> | <unk> | <ORG_1> | <unk> | with | ? <eos> | Addition | ilds |

### Top-10 (5 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 51, 109, 73, 27, 53, 110, 83, 96, 109, 49, 9, 75, 132, 96, 109, 15)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 83 | 96 | 109 | 49 | 9 | 75 | 132 | 96 | 109 | 15 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in a | <unk> | . <PER_1> | <unk> | <num> | <unk> | in a | <unk> | . <PER_2> | <unk> | <num> | <unk> | out | of the | <unk> | . How many | <unk> | <unk> | <unk> | in the | <unk> | ? <eos> | Subtraction | ilds |


## ai2 (316 samples)
### Top-1 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-2 (5 samples using it): (95, 27, 53, 110, 125, 99, 51, 109, 73, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now | there | in total | ? <eos> | Addition | ai2 |

### Top-3 (6 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-4 (4 samples using it): (95, 27, 53, 110, 125, 99, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 125 | 99 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <PER_2> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in all | ? <eos> | Addition | ai2 |

### Top-5 (4 samples using it): (95, 27, 98, 47, 125, 99, 118, 27, 53, 110, 4, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 98 | 47 | 125 | 99 | 118 | 27 | 53 | 110 | 4 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | . <ORG_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | they | <unk> | in total | ? <eos> | Addition | ai2 |

### Top-6 (4 samples using it): (95, 27, 53, 110, 51, 109, 90, 18, 117, 80, 20, 4, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 51 | 109 | 90 | 18 | 117 | 80 | 20 | 4 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | in his | <unk> | . His | <unk> | <unk> | him <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | now | ? <eos> | Addition | ai2 |

### Top-7 (4 samples using it): (95, 27, 53, 110, 51, 109, 73, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 33, 55)
| 95 | 27 | 53 | 110 | 51 | 109 | 73 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now | there | in total | ? <eos> | Addition | ai2 |

### Top-8 (4 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 51, 109, 94, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | and <PER_2> | <unk> | <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | they | <unk> | together | ? <eos> | Addition | ai2 |

### Top-9 (5 samples using it): (95, 27, 53, 110, 118, 27, 53, 110, 51, 109, 94, 57, 84, 23, 33, 55)
| 95 | 27 | 53 | 110 | 118 | 27 | 53 | 110 | 51 | 109 | 94 | 57 | 84 | 23 | 33 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | . There | <unk> | <num> | <unk> | on each | <unk> | . How many | <unk> | <unk> | there | in all | ? <eos> | Multiplication | ilds |

### Top-10 (3 samples using it): (95, 27, 98, 47, 102, 28, 72, 81, 34, 32, 49, 9, 57, 39, 56, 23, 38, 55)
| 95 | 27 | 98 | 47 | 102 | 28 | 72 | 81 | 34 | 32 | 49 | 9 | 57 | 39 | 56 | 23 | 38 | 55 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | <unk> | . <PER_2> | <unk> | <num> of <PER_1> <PER_3> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | now | ? <eos> | Subtraction | ai2 |


