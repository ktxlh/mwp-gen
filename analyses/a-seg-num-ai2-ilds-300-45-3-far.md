Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-num-ai2-ilds-300-45-3-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-num-ai2-ilds-300-45-3-far.txt
k=10
n=1
# Overall - top templates
### Top-1 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-2 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-3 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-4 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-5 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-6 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-7 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (14 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> ? | <eos> | Multiplication | ilds |

### Top-9 (12 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently | in the | <unk> | . Park | <unk> | <unk> | <unk> | <unk> | <unk> | <unk> | . When the | <unk> | <unk> | <unk> | there | <unk> | <unk> | <num> | <unk> | <unk> | in the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | <unk> ? | <eos> | Subtraction | ai2 |

### Top-10 (5 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . It | <unk> | <num> | <unk> | to | <unk> | the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | when the | <unk> | <unk> | <unk> ? | <eos> | TimeVariantUnknownFinal | ai2 |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-2 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-3 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-4 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-5 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-6 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-7 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (4 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total ? | <eos> | Addition | ai2 |

### Top-9 (12 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently | in the | <unk> | . Park | <unk> | <unk> | <unk> | <unk> | <unk> | <unk> | . When the | <unk> | <unk> | <unk> | there | <unk> | <unk> | <num> | <unk> | <unk> | in the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | <unk> ? | <eos> | Subtraction | ai2 |

### Top-10 (2 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | and | <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total ? | <eos> | Addition | ai2 |


## Subtraction (257 samples)
### Top-1 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-2 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-3 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-4 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-5 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-6 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-7 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (12 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently | in the | <unk> | . Park | <unk> | <unk> | <unk> | <unk> | <unk> | <unk> | . When the | <unk> | <unk> | <unk> | there | <unk> | <unk> | <num> | <unk> | <unk> | in the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | <unk> ? | <eos> | Subtraction | ai2 |

### Top-9 (2 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | in the | <unk> | <unk> | . Before | <unk> | <unk> | to <unk> the | <unk> | , <num> | <unk> | of | <unk> | <unk> | into the <unk> | . A | total | of | <num> | <unk> | of | <unk> | <unk> | before the | <unk> | <unk> | <unk> | . How many | <unk> | of | <unk> | <unk> | <unk> the | <unk> | <unk> | <unk> the | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-10 (14 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> ? | <eos> | Multiplication | ilds |


## CommonDiv (95 samples)
### Top-1 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-2 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-3 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-4 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-5 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-6 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-7 (14 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> ? | <eos> | Multiplication | ilds |


## Multiplication (93 samples)
### Top-1 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-2 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-3 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-4 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-5 (14 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> ? | <eos> | Multiplication | ilds |

### Top-6 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-7 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-8 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-2 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-3 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-5 (2 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | and <num> | <unk> | on the | <unk> | . <PER_1> | <unk> | <num> | <unk> | and <num> | <unk> | on the | <unk> | . How many | <unk> | <unk> | now there | in total ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (5 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . It | <unk> | <num> | <unk> | to | <unk> | the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | when the | <unk> | <unk> | <unk> ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-8 (1 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | <unk> <unk> | on a | <unk> | <unk> | in the | <unk> | . On the first | <unk> | , they | <unk> | from their | <unk> | to the | <unk> | . <unk> | , they | <unk> | <num> | <unk> | from the | <unk> | to a | <unk> | , and <num> | <unk> | from the | <unk> | to a | <unk> | . Then they | <unk> | <num> | <unk> | from the | <unk> | to the | <unk> | . How many miles | <unk> | <PER_1> 's | <unk> <unk> | in all ? | <eos> | TimeVariantUnknownFinal | ai2 |


## Sum (20 samples)
### Top-1 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-2 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-3 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-4 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-6 (5 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . It | <unk> | <num> | <unk> | to | <unk> | the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | when the | <unk> | <unk> | <unk> ? | <eos> | TimeVariantUnknownFinal | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-2 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-3 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-4 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-5 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-6 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-7 (14 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <unk> | <num> | <unk> | . How much | <unk> | <num> | <unk> | <unk> ? | <eos> | Multiplication | ilds |

### Top-8 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (42, 47, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 42 | 47 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | <unk> | <unk> | down the <unk> | . <num> | more | <unk> | <unk> | down the | <unk> | . How many | <unk> | <unk> | down the <unk> ? | <eos> | Addition | ilds |


## ai2 (316 samples)
### Top-1 (145 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <MISC_1> | <unk> | . How many | <unk> | she | <unk> | to | <unk> | away | so that she | <unk> | <unk> | <num> | <unk> | <unk> | ? | <eos> | Subtraction | ilds |

### Top-2 (113 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <unk> | of | <unk> | into | <unk> | of | <num> | . <PER_1> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <unk> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-3 (74 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to | <unk> | a | <num> | <unk> | <unk> | for | <unk> | . He | <unk> | already | <unk> | <num> | <unk> | . How many | <unk> | <unk> | he | <unk> | <unk> | to | <unk> | ? | <eos> | Subtraction | ilds |

### Top-4 (170 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | <unk> | , but | the | <unk> | <unk> | <num> | <unk> | . How many | <unk> | <unk> | <PER_1> | <unk> | ? | <eos> | Subtraction | ai2 |

### Top-5 (47 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | to the | <unk> | <num> | <unk> | last | <unk> | . She | <unk> | <num> | <unk> | <unk> | each | <unk> | she | <unk> | to the | <unk> | . How many | <unk> | <unk> | <unk> | <PER_1> | <unk> | last | <unk> | ? | <eos> | Multiplication | ilds |

### Top-6 (27 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . How many | <unk> | <unk> | <unk> | the | <unk> | <unk> | when the | <unk> | <unk> | <unk> | ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (142 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | <unk> | <PER_1> | <unk> | ? | <eos> | CommonDiv | ilds |

### Top-8 (12 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently | in the | <unk> | . Park | <unk> | <unk> | <unk> | <unk> | <unk> | <unk> | . When the | <unk> | <unk> | <unk> | there | <unk> | <unk> | <num> | <unk> | <unk> | in the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | <unk> ? | <eos> | Subtraction | ai2 |

### Top-9 (5 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | <unk> | currently in the | <unk> | . Park | <unk> | <unk> | <unk> | <num> | <unk> | <unk> | <unk> | and <num> | <unk> | <unk> | <unk> | . It | <unk> | <num> | <unk> | to | <unk> | the | <unk> | . How many | <unk> | <unk> | <unk> the | <unk> | <unk> | when the | <unk> | <unk> | <unk> ? | <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (4 samples using it): (38, 84, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132, 86, 0, 132)
| 38 | 84 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | 86 | 0 | 132 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | <unk> | <num> | <unk> | in the | <unk> | . <PER_1> | <unk> | <num> | <unk> | in the | <unk> | . How many | <unk> | <unk> | now there | in total ? | <eos> | Addition | ai2 |


