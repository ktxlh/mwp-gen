Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-num-ai2-ilds-300-45-3-far-cp.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-num-ai2-ilds-300-45-3-far-cp.txt
k=10
n=1
# Overall - top templates
### Top-1 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-3 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-4 (38 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <PER_2> | . | <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-5 (30 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-6 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-7 (24 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |

### Top-8 (19 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-9 (18 samples using it): (92, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 92 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |

### Top-10 (15 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | <unk> | eat | <num> | flowers | each | . How many | flowers | total | did | the | <unk> | eat | ? <eos> | Multiplication | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-3 (38 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <PER_2> | . | <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-4 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-5 (24 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |

### Top-6 (30 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-7 (14 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to make | a | <unk> | - | shirt | . How many <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-8 (15 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-9 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-10 (14 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's <unk> | school | played | <num> | baseball | games | this | year | , <num> | of the | games | were | played | at | night | . She | <unk> | <num> | games | . How many | baseball | games | did | <PER_1> | <unk> | ? <eos> | Subtraction | ai2 |


## Subtraction (257 samples)
### Top-1 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-3 (38 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <PER_2> | . | <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-4 (30 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-5 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-6 (15 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | <unk> | eat | <num> | flowers | each | . How many | flowers | total | did | the | <unk> | eat | ? <eos> | Multiplication | ilds |

### Top-7 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-8 (7 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Last | week | <PER_1> | had | <num> | dollars | and <PER_2> | had | <num> | dollars | . <PER_1> | <unk> | cars | over the | weekend | and | now | has | <num> | dollars | . How much | money | did | <PER_1> | make <unk> | cars | ? <eos> | Subtraction | ai2 |

### Top-9 (13 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | bought | <num> | pieces | of | paper . She | used | <num> | pieces | of | the | paper | . How many | pieces | of | paper | does | she | have | left | ? <eos> | Subtraction | ilds |

### Top-10 (18 samples using it): (92, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 92 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |


## CommonDiv (95 samples)
### Top-1 (30 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-2 (19 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-3 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-4 (15 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | <unk> | eat | <num> | flowers | each | . How many | flowers | total | did | the | <unk> | eat | ? <eos> | Multiplication | ilds |

### Top-5 (18 samples using it): (92, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 92 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |

### Top-6 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-7 (13 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | bought | <num> | pieces | of | paper . She | used | <num> | pieces | of | the | paper | . How many | pieces | of | paper | does | she | have | left | ? <eos> | Subtraction | ilds |

### Top-8 (14 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | owns | <num> | dogs | . Each | day | , <num> | dog | <unk> | <num> | scoop | of | dog | food | and the <unk> | dog | <unk> | <num> | scoop | . <unk> | , how much | dog | food | do | the <num> | dogs | eat | each | day | ? <eos> | Addition | ai2 |

### Top-9 (4 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> <unk> ? <eos> | CommonDiv | ilds |

### Top-10 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |


## Multiplication (93 samples)
### Top-1 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-2 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (24 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |

### Top-4 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-5 (7 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-6 (19 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-7 (3 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-8 (38 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <PER_2> | . | <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-9 (3 samples using it): (7, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 7 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | bag | <unk> | <num> | pounds | of | oranges | . How many | pounds | of | oranges | are | in | <num> | bags | ? <eos> | Multiplication | ilds |

### Top-10 (15 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-2 (11 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-3 (7 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |

### Top-4 (14 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to make | a | <unk> | - | shirt | . How many <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-5 (5 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | truck | <unk> | <num> | pounds | of | sand | <unk> | to a | construction | yard | and | loses | <num> | pounds | of | sand | <unk> | the | <unk> | . How much | sand | does | the | truck | have | when it | <unk> | at the | yard | ? <eos> | Subtraction | ai2 |

### Top-6 (3 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently | in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-8 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-9 (6 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |

### Top-10 (12 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| This | afternoon | <PER_1> | left | school | , <unk> | the | bus | <num> | miles | , and then | walked | <num> | mile to | get | home | . How much <unk> | did | <PER_1> | ride | than | walk | ? <eos> | Subtraction | ai2 |


## Sum (20 samples)
### Top-1 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-2 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-3 (4 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | weighs | <num> | pounds | . | <MISC_1> | weighs | <num> | pounds | . | <PER_2> | weighs | <num> | pounds | . How much | <unk> | is | <PER_1> | than <PER_3> | ? <eos> | Subtraction | ilds |

### Top-4 (14 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | owns | <num> | dogs | . Each | day | , <num> | dog | <unk> | <num> | scoop | of | dog | food | and the <unk> | dog | <unk> | <num> | scoop | . <unk> | , how much | dog | food | do | the <num> | dogs | eat | each | day | ? <eos> | Addition | ai2 |

### Top-5 (11 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-6 (14 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's <unk> | school | played | <num> | baseball | games | this | year | , <num> | of the | games | were | played | at | night | . She | <unk> | <num> | games | . How many | baseball | games | did | <PER_1> | <unk> | ? <eos> | Subtraction | ai2 |

### Top-7 (1 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> <unk> | <unk> | <num> | truck | - | load | of | sand | , <num> | truck | - | load | of | <unk> | , and <num> | truck | - | load | of | cement | . How many | truck | - | <unk> | of | material | were | needed | in all ? <eos> | Sum | ai2 |

### Top-8 (4 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | baking | a | cake | . The | recipe | <unk> | for <num> | cups | of | flour | and <num> | cups | of | sugar | . She | already | put | in <num> | cups | of | flour | . How many | cups | of | flour | does | she | need | to | add | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently | in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (4 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | put | <unk> | <unk> | into the | <unk> | on | <unk> | night | . She | <unk> | that the | restaurant | had | <num> | <unk> | filled | with | <unk> | , <num> | <unk> | filled | with | <unk> | , and <num> | <unk> | filled | with | peaches | . How many <unk> | <unk> | did | the restaurant | have | in all ? <eos> | Sum | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-3 (38 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <PER_2> | . | <PER_3> | takes | <num> | away | . How many | <MISC_1> | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-4 (30 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-5 (19 samples using it): (109, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40)
| 109 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-6 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |

### Top-7 (24 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |

### Top-8 (15 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | <unk> | eat | <num> | flowers | each | . How many | flowers | total | did | the | <unk> | eat | ? <eos> | Multiplication | ilds |

### Top-9 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-10 (18 samples using it): (92, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 92 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |


## ai2 (316 samples)
### Top-1 (92 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked | <num> | oranges | and | <PER_2> | picked | <num> | oranges | . | <PER_3> | picked | <num> | pears | . How many | oranges | were | picked | in total | ? <eos> | Addition | ai2 |

### Top-2 (132 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | cards | . | <PER_2> | takes | <num> | away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-3 (39 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie . | <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |

### Top-4 (12 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| This | afternoon | <PER_1> | left | school | , <unk> | the | bus | <num> | miles | , and then | walked | <num> | mile to | get | home | . How much <unk> | did | <PER_1> | ride | than | walk | ? <eos> | Subtraction | ai2 |

### Top-5 (14 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's <unk> | school | played | <num> | baseball | games | this | year | , <num> | of the | games | were | played | at | night | . She | <unk> | <num> | games | . How many | baseball | games | did | <PER_1> | <unk> | ? <eos> | Subtraction | ai2 |

### Top-6 (14 samples using it): (64, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119)
| 64 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to make | a | <unk> | - | shirt | . How many <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-7 (24 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |

### Top-8 (15 samples using it): (37, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 37 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | boxes | of | pencils | . Each | box | holds | <num> | pencils | . How many | pencils | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-9 (18 samples using it): (92, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 92 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |

### Top-10 (26 samples using it): (47, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103, 45, 119, 40, 67, 103)
| 47 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | 45 | 119 | 40 | 67 | 103 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | made | <num> | hamburgers | and <num> | hot | dogs | to | serve | during | lunch | . <unk> | <num> | hamburgers | were | <unk> | served | . How many hamburgers | were | over ? <eos> | Subtraction | ai2 |


