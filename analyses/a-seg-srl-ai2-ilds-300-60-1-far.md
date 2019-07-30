Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='gens/gen-srl-ai2-ilds-300-60-1-far.md', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-60-1-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-60-1-far.txt
k=10
n=1
# Overall - top templates
### Top-1 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-2 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-3 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-4 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-5 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-6 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-7 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-8 (29 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-9 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-10 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-2 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-3 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-4 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-5 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-6 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-7 (16 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . <num> | are | eaten | by a | hippopotamus | . How many | bottle | caps | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-8 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-9 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-10 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |


## Subtraction (257 samples)
### Top-1 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-2 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-3 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-4 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-5 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-6 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-7 (13 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | needs | to | read | a | <num> | <unk> | book | for | school | . He | has | already | read | <num> | pages | . How many | pages | does | he | have | left | to | read | ? <eos> | Subtraction | ilds |

### Top-8 (16 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-9 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |

### Top-10 (16 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | bottle | caps | . <num> | are | eaten | by a | hippopotamus | . How many | bottle | caps | will | <PER_1> | have | ? <eos> | Subtraction | ilds |


## CommonDiv (95 samples)
### Top-1 (29 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-2 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-3 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-4 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-5 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-6 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-7 (10 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | bought | <num> <unk> | <unk> | . She | has | <num> | children | . She | would | <unk> | to | <unk> the | <unk> | among her | children | so | that | each | child | gets | the | same | <unk> | . How many | <unk> | would | each | child | get | ? <eos> | CommonDiv | ilds |

### Top-8 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-9 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-10 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |


## Multiplication (93 samples)
### Top-1 (29 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-2 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-3 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-4 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-5 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-6 (16 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-7 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-8 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-9 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-10 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |

### Top-2 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |

### Top-3 (13 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | popular | trees | currently | in the | park | . Park | workers | will | plant | <num> | popular | trees | today | . How many | popular | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-4 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-5 (12 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> short | trees | and <num> | tall | trees | currently | in the | park | . Park | workers | will | plant | <num> | short | trees | today | . How many | short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-6 (7 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | chocolate | <unk> | cookie | recipe | <unk> | for <num> | cups | of | chocolate | <unk> | . You | <unk> | to | make | <num> | <unk> | for a | bake | sale | . How many | cups | of | chocolate | <unk> | will | be | needed | to | make | all the | cookie | <unk> | ? <eos> | Multiplication | ilds |

### Top-7 (3 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently | in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-9 (7 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | minutes | to | bake | one | <unk> | of | cookies | . How long | will | it | take | to | bake | <num> | <unk> | of | cookies | ? <eos> | Multiplication | ilds |

### Top-10 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |


## Sum (20 samples)
### Top-1 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-2 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-3 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-4 (13 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | popular | trees | currently | in the | park | . Park | workers | will | plant | <num> | popular | trees | today | . How many | popular | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-5 (7 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | minutes | to | bake | one | <unk> | of | cookies | . How long | will | it | take | to | bake | <num> | <unk> | of | cookies | ? <eos> | Multiplication | ilds |

### Top-6 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-7 (6 samples using it): (14, 11, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 14 | 11 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | fruit | farm | packs | oranges | in | boxes | that | hold | <num> | each | . <unk> | day | it | packs | <num> | oranges | . How many | boxes | did | they | use | ? <eos> | CommonDiv | ilds |

### Top-8 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (14, 11, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 14 | 11 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | are | <unk> | a | book | with <num> | pages | . If you | <unk> | to | read | the same | number | of | pages | each | night | , how many | would | you | have | to | read | each | night | to | <unk> | in <num> | days | ? <eos> | CommonDiv | ilds |

### Top-10 (1 samples using it): (50, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 50 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | made | <unk> | in the | <unk> | . She | used | <num> | cup | of | strawberries | , <num> | cup | of | <unk> | , and <num> | cup | of | orange | <unk> | . How many | cups of <unk> | did | <PER_1> | use | for the | <unk> | ? <eos> | Sum | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-2 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-3 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-4 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-5 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |

### Top-6 (29 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-7 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-8 (16 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-9 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-10 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |


## ai2 (316 samples)
### Top-1 (72 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to | make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |

### Top-2 (40 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |

### Top-3 (97 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many | <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-4 (49 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |

### Top-5 (44 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-6 (26 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | feet | of | <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |

### Top-7 (13 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | popular | trees | currently | in the | park | . Park | workers | will | plant | <num> | popular | trees | today | . How many | popular | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-8 (36 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| You | have | <num> | cookies | and | <unk> | to | share | them | equally | with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |

### Top-9 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |

### Top-10 (19 samples using it): (31, 8, 23, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32, 52, 46, 7, 32)
| 31 | 8 | 23 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | 52 | 46 | 7 | 32 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Mrs. <PER_1> | <unk> | <num> | ounces | of | <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |


