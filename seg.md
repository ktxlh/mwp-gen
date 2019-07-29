# Analysis on segmentation
metadata_path=/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=/Users/shanglinghsu/mwp/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt
k=10
n=1
# 1. overall - top templates
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-3 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |

### Top-4 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |

### Top-5 (7 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| I walk <num> | mile | every <num> | minutes | . I walked <num> | miles | . How many | minutes | did it take | <unk> | ? <eos> | Multiplication | ilds |

### Top-6 (6 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-7 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-8 (6 samples using it): (271, 40, 178, 66, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | and <PER_2> found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Addition | ai2 |

### Top-9 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-10 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds |

### Distribution of solution type: the 74 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 4 (0.235) |13 (0.765) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |1 (0.125) |7 (0.875) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 7 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 6 (0.857) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 6 (0.857) |0 (0.000) |0 (0.000) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |1 (0.167) |5 (0.833) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |6 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 5 (0.833) |0 (0.000) |0 (0.000) |1 (0.167) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 74 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 17 (1.000) |0 (0.000) |
| top-2 | 8 (1.000) |0 (0.000) |
| top-3 | 0 (0.000) |7 (1.000) |
| top-4 | 7 (1.000) |0 (0.000) |
| top-5 | 1 (0.143) |6 (0.857) |
| top-6 | 6 (1.000) |0 (0.000) |
| top-7 | 6 (1.000) |0 (0.000) |
| top-8 | 1 (0.167) |5 (0.833) |
| top-9 | 5 (1.000) |0 (0.000) |
| top-10 | 5 (1.000) |0 (0.000) |

# 2. solution type - top templates
## Addition (258 samples)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |

### Top-2 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |

### Top-3 (7 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| I walk <num> | mile | every <num> | minutes | . I walked <num> | miles | . How many | minutes | did it take | <unk> | ? <eos> | Multiplication | ilds |

### Top-4 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds |

### Top-5 (5 samples using it): (271, 40, 68, 228, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 228 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | peanuts | . <LOC_1> has <num> | more | than <PER_1> | . How many | peanuts | does <LOC_1> have | ? <eos> | Addition | ilds |

### Top-6 (6 samples using it): (271, 40, 178, 66, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | and <PER_2> found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Addition | ai2 |

### Top-7 (5 samples using it): (161, 260, 180, 68, 228, 107, 45, 143, 104, 85, 84)
| 161 | 260 | 180 | 68 | 228 | 107 | 45 | 143 | 104 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | bottle | caps | . He buys <num> | more | . How many | bottle | caps | does <PER_1> have | in all | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (271, 40, 186, 132, 186, 132, 99, 230, 229, 56, 245, 264, 95, 3, 187, 107, 45, 3, 75, 139)
| 271 | 40 | 186 | 132 | 186 | 132 | 99 | 230 | 229 | 56 | 245 | 264 | 95 | 3 | 187 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | bananas | in a | pile | on the | desk | . Each | banana | comes in a | package | of <num> | . <num> | bananas | are added to the | pile | . How many | bananas | are there in the | pile | ? <eos> | Addition | ilds |

### Top-9 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-10 (4 samples using it): (271, 40, 122, 165, 107, 45, 104, 85, 84)
| 271 | 40 | 122 | 165 | 107 | 45 | 104 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | apples | . <PER_2> | gives <PER_1> <num> more | . How many | apples | does <PER_1> have | in all | ? <eos> | Addition | ilds |

### Distribution of solution type: the 68 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 7 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 6 (0.857) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 6 (0.857) |0 (0.000) |0 (0.000) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 5 (0.833) |0 (0.000) |0 (0.000) |1 (0.167) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 4 (0.235) |13 (0.765) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 68 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |7 (1.000) |
| top-2 | 7 (1.000) |0 (0.000) |
| top-3 | 1 (0.143) |6 (0.857) |
| top-4 | 5 (1.000) |0 (0.000) |
| top-5 | 5 (1.000) |0 (0.000) |
| top-6 | 1 (0.167) |5 (0.833) |
| top-7 | 5 (1.000) |0 (0.000) |
| top-8 | 5 (1.000) |0 (0.000) |
| top-9 | 17 (1.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |

## Subtraction (254 samples)
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-2 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-3 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-4 (5 samples using it): (271, 40, 178, 66, 164, 214, 139)
| 271 | 40 | 178 | 66 | 164 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> weighs <num> | pounds | . <PER_2> weighs <num> | pounds | . How much heavier | is <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-5 (4 samples using it): (271, 40, 99, 230, 229, 165, 107, 45, 214, 139)
| 271 | 40 | 99 | 230 | 229 | 165 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <num> | oranges | . He | shares | <num> | with <PER_2> | . How many | oranges | will <PER_3> have | ? <eos> | Subtraction | ilds |

### Top-6 (4 samples using it): (271, 40, 186, 132, 13, 196, 47, 49, 139)
| 271 | 40 | 186 | 132 | 13 | 196 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | oranges | in a | box | . <PER_1> takes <num> | oranges | . How many | are left | ? <eos> | Subtraction | ilds |

### Top-7 (4 samples using it): (271, 40, 157, 265, 87, 238, 263, 75, 139)
| 271 | 40 | 157 | 265 | 87 | 238 | 263 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> baked <num> | muffins | . How many more | muffins | does <PER_1> have | to bake to | have <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-8 (4 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | dimes | and <num> | pennies | in her | bank | . Her | dad | borrowed <num> | pennies | from <PER_1> | . How many | pennies | does she have now | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (271, 40, 203, 196, 219, 197, 39, 139)
| 271 | 40 | 203 | 196 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> ran <num> | mile | and walked <num> | mile | . How much farther | did <PER_1> run than | walk | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (271, 40, 186, 132, 13, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 13 | 92 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | pennies | in his | bank | . He spent <num> | of his | pennies | . How many | pennies | does he have now | ? <eos> | Subtraction | ai2 |

### Distribution of solution type: the 55 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 4 (0.235) |13 (0.765) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |6 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 55 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 17 (1.000) |0 (0.000) |
| top-2 | 6 (1.000) |0 (0.000) |
| top-3 | 5 (1.000) |0 (0.000) |
| top-4 | 5 (1.000) |0 (0.000) |
| top-5 | 4 (1.000) |0 (0.000) |
| top-6 | 4 (1.000) |0 (0.000) |
| top-7 | 4 (1.000) |0 (0.000) |
| top-8 | 0 (0.000) |4 (1.000) |
| top-9 | 0 (0.000) |3 (1.000) |
| top-10 | 0 (0.000) |3 (1.000) |

## CommonDiv (97 samples)
### Top-1 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-2 (6 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-3 (5 samples using it): (271, 40, 232, 230, 229, 56, 89, 95, 3, 75, 253, 139)
| 271 | 40 | 232 | 230 | 229 | 56 | 89 | 95 | 3 | 75 | 253 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | erasers | . If he | shares | them among <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-4 (4 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 39, 139)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> | jogging | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (271, 40, 133, 162, 251, 72, 222, 254, 45, 214, 139)
| 271 | 40 | 133 | 162 | 251 | 72 | 222 | 254 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> sold <num> | boxes | of <MISC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does <PER_1> need | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (271, 40, 186, 132, 233, 172, 107, 45, 3, 75, 139)
| 271 | 40 | 186 | 132 | 233 | 172 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> is inviting <num> | friends | to a | party | . He has <num> | cookies | . How many | cookies | will each friend | get | ? <eos> | CommonDiv | ilds |

### Top-7 (4 samples using it): (271, 40, 186, 132, 177, 119, 196, 89, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 177 | 119 | 196 | 89 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | candies | stored in | boxes | . If there | are <num> | boxes | , how many | candies | must go in each | box | ? <eos> | CommonDiv | ilds |

### Top-8 (4 samples using it): (51, 160, 40, 17, 180, 237, 163, 245, 233, 172, 107, 45, 214, 139)
| 51 | 160 | 40 | 17 | 180 | 237 | 163 | 245 | 233 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> wants | to split a | collection | of | peanuts | into | groups | of <num> | . <PER_1> has <num> | peanuts | . How many | groups | will be created | ? <eos> | CommonDiv | ilds |

### Top-9 (4 samples using it): (271, 40, 186, 132, 203, 196, 44, 198, 183, 202, 2, 34, 153, 108, 85, 84)
| 271 | 40 | 186 | 132 | 203 | 196 | 44 | 198 | 183 | 202 | 2 | 34 | 153 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | students | in the | class | and <num> | apples | . If the | apples | are divided equally | among the | students | , how many | does each | student | get | ? <eos> | CommonDiv | ilds |

### Top-10 (4 samples using it): (96, 95, 3, 71, 132, 13, 221, 203, 196, 92, 260, 180, 157, 265, 142, 76, 75, 139)
| 96 | 95 | 3 | 71 | 132 | 13 | 221 | 203 | 196 | 92 | 260 | 180 | 157 | 265 | 142 | 76 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | school | is planning a | field | trip | . There are <num> | students | and <num> | seats | on each | school | bus | . How many | buses | are needed | to take the | trip | ? <eos> | CommonDiv | ilds |

### Distribution of solution type: the 47 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |1 (0.125) |7 (0.875) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |1 (0.167) |5 (0.833) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 47 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 8 (1.000) |0 (0.000) |
| top-2 | 6 (1.000) |0 (0.000) |
| top-3 | 5 (1.000) |0 (0.000) |
| top-4 | 4 (1.000) |0 (0.000) |
| top-5 | 4 (1.000) |0 (0.000) |
| top-6 | 4 (1.000) |0 (0.000) |
| top-7 | 4 (1.000) |0 (0.000) |
| top-8 | 4 (1.000) |0 (0.000) |
| top-9 | 4 (1.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |

## Multiplication (93 samples)
### Top-1 (5 samples using it): (90, 119, 196, 148, 42, 182, 53, 219, 197, 84)
| 90 | 119 | 196 | 148 | 42 | 182 | 53 | 219 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> wandered | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |

### Top-2 (4 samples using it): (271, 40, 17, 180, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | boxes | of | peanuts | . Each | box | holds <num> | peanuts | . How many | peanuts | does <PER_1> have | ? <eos> | Multiplication | ilds |

### Top-3 (3 samples using it): (271, 40, 186, 132, 272, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | crayons | in each | box | . How many | crayons | are in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-4 (3 samples using it): (271, 40, 17, 180, 99, 230, 229, 196, 178, 66, 21, 22, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 196 | 178 | 66 | 21 | 22 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | boxes | of | eggs | . Each | box | holds <num> | eggs | and there are <num> | boxes | in a | <unk> | . How many | eggs | does <PER_1> have | ? <eos> | Multiplication | ilds |

### Top-5 (3 samples using it): (200, 205, 243, 160, 40, 148, 42, 182, 53, 219, 197, 270, 59, 270, 75, 139)
| 200 | 205 | 243 | 160 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 270 | 59 | 270 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It took <PER_1> <num> | hours | to stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-6 (3 samples using it): (271, 40, 93, 180, 131, 236, 178, 66, 147, 234, 270, 172, 107, 45, 142, 76, 75, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 270 | 172 | 107 | 45 | 142 | 76 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> went to the | store | <num> | times | last | month | . He buys <num> | bananas | each | time | he goes to the | store | . How many | bananas | did <PER_1> buy | last | month | ? <eos> | Multiplication | ilds |

### Top-7 (2 samples using it): (41, 205, 25, 54, 98, 256, 85, 84)
| 41 | 205 | 25 | 54 | 98 | 256 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | costs $ <num> | . How much | do <num> | tickets | cost | ? <eos> | Multiplication | ilds |

### Top-8 (2 samples using it): (41, 205, 93, 180, 177, 119, 196, 89, 95, 3, 75, 139)
| 41 | 205 | 93 | 180 | 177 | 119 | 196 | 89 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | candies | . If there | are <num> | children | , how many | candies | are there in | total | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (41, 205, 119, 196, 69, 12, 119, 196, 144, 265, 10, 3, 75, 139)
| 41 | 205 | 119 | 196 | 69 | 12 | 119 | 196 | 144 | 265 | 10 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | bottle | caps | . If there | are <num> | children | , how many | bottle | caps | are there in | total | ? <eos> | Multiplication | ilds |

### Top-10 (1 samples using it): (41, 205, 119, 196, 164, 153, 108, 85, 84)
| 41 | 205 | 119 | 196 | 164 | 153 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <unk> | pencil | weighs <num> | grams | . How much | do <num> | pencils | weigh | ? <eos> | Multiplication | ilds |

### Distribution of solution type: the 28 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 28 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 5 (1.000) |0 (0.000) |
| top-2 | 4 (1.000) |0 (0.000) |
| top-3 | 3 (1.000) |0 (0.000) |
| top-4 | 3 (1.000) |0 (0.000) |
| top-5 | 3 (1.000) |0 (0.000) |
| top-6 | 3 (1.000) |0 (0.000) |
| top-7 | 2 (1.000) |0 (0.000) |
| top-8 | 2 (1.000) |0 (0.000) |
| top-9 | 2 (1.000) |0 (0.000) |
| top-10 | 1 (1.000) |0 (0.000) |

## TimeVariantUnknownFinal (35 samples)
### Top-1 (2 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 13, 221, 203, 196, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 13 | 221 | 203 | 196 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> placed <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-2 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served <num> | cakes | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | cakes | yesterday | . How many | cakes | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-3 (1 samples using it): (271, 40, 177, 119, 196, 68, 228, 172, 107, 45, 214, 139)
| 271 | 40 | 177 | 119 | 196 | 68 | 228 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> <MISC_1> | cards | . <PER_2> gave | her <num> new <MISC_1> | cards | . <PER_1> bought <num> | <MISC_1> | cards | . How many <MISC_1> | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (1 samples using it): (271, 40, 186, 132, 99, 230, 229, 66, 147, 234, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 66 | 147 | 234 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | dimes | in her | bank | . Her | dad | gave her <num> | dimes | and her | mother | gave her <num> | dimes | . How many | dimes | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 178, 66, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> placed <num> | pencils | on the | desk | . How many | pencils | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 56, 203, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 56 | 203 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served <num> | pies | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | pies | and <num> | pizzas | yesterday | . How many | pies | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (1 samples using it): (41, 205, 177, 119, 196, 80, 237, 163, 82, 202, 2, 67, 144, 265, 252, 139)
| 41 | 205 | 177 | 119 | 196 | 80 | 237 | 163 | 82 | 202 | 2 | 67 | 144 | 265 | 252 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <unk> <unk> | <unk> | . <PER_1> paid | $ <num> for | <unk> | , $ <num> | for | apples | , and $ <num> | for | peaches | . In total | , how much | money | did she spend | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (1 samples using it): (161, 260, 180, 245, 257, 71, 132, 245, 137, 221, 245, 219, 197, 39, 253, 139)
| 161 | 260 | 180 | 245 | 257 | 71 | 132 | 245 | 137 | 221 | 245 | 219 | 197 | 39 | 253 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> purchased a | football | game | for $ <num> | , a | <unk> | game | for $ <num> | , and a <MISC_1> | game | for $ <num> | . How much | did <PER_1> spend on | video | games | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 56, 258, 198, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 56 | 258 | 198 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | quarters | and <num> | pennies | in her | bank | . Her | dad | gave her <num> | pennies | and her | mother | gave her <num> | pennies | . How many | pennies | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (1 samples using it): (161, 260, 180, 82, 78, 177, 119, 196, 69, 13, 196, 22, 107, 45, 143, 214, 139)
| 161 | 260 | 180 | 82 | 78 | 177 | 119 | 196 | 69 | 13 | 196 | 22 | 107 | 45 | 143 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | baseball | cards | , and <num> | were torn | . <PER_2> gave | <PER_1> <num> new | baseball | cards | . <PER_1> bought <num> | baseball | cards | . How many | baseball | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Distribution of solution type: the 11 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 11 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |2 (1.000) |
| top-2 | 0 (0.000) |1 (1.000) |
| top-3 | 0 (0.000) |1 (1.000) |
| top-4 | 0 (0.000) |1 (1.000) |
| top-5 | 0 (0.000) |1 (1.000) |
| top-6 | 0 (0.000) |1 (1.000) |
| top-7 | 0 (0.000) |1 (1.000) |
| top-8 | 0 (0.000) |1 (1.000) |
| top-9 | 0 (0.000) |1 (1.000) |
| top-10 | 0 (0.000) |1 (1.000) |

## Sum (25 samples)
### Top-1 (3 samples using it): (271, 40, 178, 66, 247, 119, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | , <PER_2> has <num> | books | , and <PER_3> | has <num> | books | . How many | books | do they have | together | ? <eos> | Sum | ai2 |

### Top-2 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 |

### Top-3 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 267 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> blue | balloons | , <PER_2> has <num> | blue | balloons | , and <PER_3> | has <num> blue | balloons | . How many blue | balloons | do they have | in all | ? <eos> | Sum | ai2 |

### Top-4 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 203, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 203 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | limes | , <PER_2> picked <num> | limes | , and <PER_3> | picked <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were picked | in total | ? <eos> | Sum | ai2 |

### Top-5 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 12, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 12 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> grew <num> | pumpkins | , <PER_2> grew <num> | pumpkins | , and <PER_3> | grew <num> | pumpkins | . They worked | for <num> | days | on the | farm | . How many | pumpkins | did they grow | in all | ? <eos> | Sum | ai2 |

### Top-6 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 99, 230, 229, 56, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 99 | 230 | 229 | 56 | 267 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> red | balloons | , <PER_2> has <num> | red | balloons | , and <PER_3> | has <num> red | balloons | . The | balloons | cost <num> | dollars | . How many red | balloons | do they have | in all | ? <eos> | Sum | ai2 |

### Top-7 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 67, 78, 247, 119, 78, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 67 | 78 | 247 | 119 | 78 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . When they | cleaned them | , they discovered | that <num> | were cracked | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 |

### Top-8 (1 samples using it): (271, 40, 178, 66, 247, 119, 196, 257, 71, 132, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 257 | 71 | 132 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | plums | , <PER_2> picked <num> | plums | , and <PER_3> | picked <num> | plums | from the | <unk> | tree | . How many | plums | were picked | in total | ? <eos> | Sum | ai2 |

### Top-9 (1 samples using it): (261, 260, 180, 148, 42, 182, 53, 27, 251, 72, 222, 27, 251, 72, 222, 162, 251, 72, 222, 98, 256, 108, 85, 84)
| 261 | 260 | 180 | 148 | 42 | 182 | 53 | 27 | 251 | 72 | 222 | 27 | 251 | 72 | 222 | 162 | 251 | 72 | 222 | 98 | 256 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | company | <unk> <num> | ton | of | <unk> | , <num> | ton | of | <unk> | , and <num> | ton | of | <unk> | . How many | tons | of | <unk> | did the | company | <unk> | in all | ? <eos> | Sum | ai2 |

### Top-10 (1 samples using it): (271, 40, 257, 71, 132, 13, 42, 182, 53, 27, 251, 72, 222, 27, 251, 72, 222, 162, 251, 72, 222, 252, 139)
| 271 | 40 | 257 | 71 | 132 | 13 | 42 | 182 | 53 | 27 | 251 | 72 | 222 | 27 | 251 | 72 | 222 | 162 | 251 | 72 | 222 | 252 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> made trail | mix | for a | <unk> | trip | . She used <num> | pound | of | peanuts | , <num> | pound | of chocolate | <unk> | , and <num> | pound | of | <unk> | . How many | pounds | of trail | mix | did <PER_1> make | ? <eos> | Sum | ai2 |

### Distribution of solution type: the 18 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 18 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |3 (1.000) |
| top-2 | 0 (0.000) |2 (1.000) |
| top-3 | 0 (0.000) |2 (1.000) |
| top-4 | 0 (0.000) |2 (1.000) |
| top-5 | 0 (0.000) |2 (1.000) |
| top-6 | 0 (0.000) |2 (1.000) |
| top-7 | 0 (0.000) |2 (1.000) |
| top-8 | 0 (0.000) |1 (1.000) |
| top-9 | 0 (0.000) |1 (1.000) |
| top-10 | 0 (0.000) |1 (1.000) |

# 3. dataset - top templates
## ilds (449 samples)
### Top-1 (17 samples using it): (271, 40, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | oranges | . <PER_2> takes <num> | away | . How many | oranges | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-2 (8 samples using it): (271, 40, 148, 42, 182, 53, 219, 197, 39, 139)
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> strolled <num> | miles | at <num> | miles | per | hour | . How long | did <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-3 (7 samples using it): (271, 40, 13, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> collects <num> | candies | . <PER_1> 's | father | gives <PER_1> <num> more | . How many | candies | does <PER_1> have | ? <eos> | Addition | ilds |

### Top-4 (6 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 84)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> <unk> <num> | miles | at <num> | miles | per | hour | , how long | was <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-5 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-6 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-7 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (90, 119, 196, 148, 42, 182, 53, 219, 197, 84)
| 90 | 119 | 196 | 148 | 42 | 182 | 53 | 219 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> wandered | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |

### Top-9 (5 samples using it): (271, 40, 178, 66, 164, 214, 139)
| 271 | 40 | 178 | 66 | 164 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> weighs <num> | pounds | . <PER_2> weighs <num> | pounds | . How much heavier | is <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-10 (5 samples using it): (271, 40, 68, 228, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 228 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | peanuts | . <LOC_1> has <num> | more | than <PER_1> | . How many | peanuts | does <LOC_1> have | ? <eos> | Addition | ilds |

### Distribution of solution type: the 69 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 4 (0.235) |13 (0.765) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |1 (0.125) |7 (0.875) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 6 (0.857) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |1 (0.167) |5 (0.833) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |6 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 69 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 17 (1.000) |0 (0.000) |
| top-2 | 8 (1.000) |0 (0.000) |
| top-3 | 7 (1.000) |0 (0.000) |
| top-4 | 6 (1.000) |0 (0.000) |
| top-5 | 6 (1.000) |0 (0.000) |
| top-6 | 5 (1.000) |0 (0.000) |
| top-7 | 5 (1.000) |0 (0.000) |
| top-8 | 5 (1.000) |0 (0.000) |
| top-9 | 5 (1.000) |0 (0.000) |
| top-10 | 5 (1.000) |0 (0.000) |

## ai2 (316 samples)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |

### Top-2 (7 samples using it): (271, 40, 93, 180, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| I walk <num> | mile | every <num> | minutes | . I walked <num> | miles | . How many | minutes | did it take | <unk> | ? <eos> | Multiplication | ilds |

### Top-3 (6 samples using it): (271, 40, 178, 66, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | and <PER_2> found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Addition | ai2 |

### Top-4 (5 samples using it): (271, 40, 186, 132, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | quarters | in her | bank | . Her | dad | gave her <num> | quarters | . How many | quarters | does she have now | ? <eos> | Addition | ai2 |

### Top-5 (4 samples using it): (271, 40, 13, 221, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 13 | 221 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | plums | and <PER_2> picked <num> | plums | . <PER_3> picked <num> | pears | . How many | plums | were picked | in all | ? <eos> | Addition | ai2 |

### Top-6 (4 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | dimes | and <num> | pennies | in her | bank | . Her | dad | borrowed <num> | pennies | from <PER_1> | . How many | pennies | does she have now | ? <eos> | Subtraction | ai2 |

### Top-7 (4 samples using it): (271, 40, 93, 180, 131, 236, 178, 66, 21, 22, 107, 45, 3, 75, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 178 | 66 | 21 | 22 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | scissors | and <num> | pencils | in the | drawer | . <PER_1> placed <num> | scissors | in the | drawer | . How many | scissors | are now there in | total | ? <eos> | Addition | ai2 |

### Top-8 (3 samples using it): (271, 40, 203, 196, 219, 197, 39, 139)
| 271 | 40 | 203 | 196 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> ran <num> | mile | and walked <num> | mile | . How much farther | did <PER_1> run than | walk | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (271, 40, 186, 132, 13, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 13 | 92 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | pennies | in his | bank | . He spent <num> | of his | pennies | . How many | pennies | does he have now | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (271, 40, 186, 132, 247, 119, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 247 | 119 | 92 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | on the | beach | , she gave | <PER_2> <num> | of the | seashells | . How many | seashells | does she now have | ? <eos> | Subtraction | ai2 |

### Distribution of solution type: the 46 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 7 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 6 (0.857) |0 (0.000) |0 (0.000) |1 (0.143) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 5 (0.833) |0 (0.000) |0 (0.000) |1 (0.167) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 3 (0.600) |1 (0.200) |1 (0.200) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 46 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |7 (1.000) |
| top-2 | 1 (0.143) |6 (0.857) |
| top-3 | 1 (0.167) |5 (0.833) |
| top-4 | 1 (0.200) |4 (0.800) |
| top-5 | 0 (0.000) |4 (1.000) |
| top-6 | 0 (0.000) |4 (1.000) |
| top-7 | 0 (0.000) |4 (1.000) |
| top-8 | 0 (0.000) |3 (1.000) |
| top-9 | 0 (0.000) |3 (1.000) |
| top-10 | 0 (0.000) |3 (1.000) |

# 4. Pure templates: specific solution type
## Addition (258 samples)
### Top-1 (7 samples using it): (271, 40, 178, 66, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | . <PER_2> has <num> | books | . How many | books | do they have | together | ? <eos> | Addition | ai2 |

### Top-4 (5 samples using it): (271, 40, 44, 198, 118, 23, 47, 49, 139)
| 271 | 40 | 44 | 198 | 118 | 23 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | blocks | . <num> | blocks | more | are added | . How many | are there total | ? <eos> | Addition | ilds |

### Top-5 (5 samples using it): (271, 40, 68, 228, 0, 107, 45, 214, 139)
| 271 | 40 | 68 | 228 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | peanuts | . <LOC_1> has <num> | more | than <PER_1> | . How many | peanuts | does <LOC_1> have | ? <eos> | Addition | ilds |

### Top-7 (5 samples using it): (161, 260, 180, 68, 228, 107, 45, 143, 104, 85, 84)
| 161 | 260 | 180 | 68 | 228 | 107 | 45 | 143 | 104 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | bottle | caps | . He buys <num> | more | . How many | bottle | caps | does <PER_1> have | in all | ? <eos> | Addition | ilds |

### Top-8 (5 samples using it): (271, 40, 186, 132, 186, 132, 99, 230, 229, 56, 245, 264, 95, 3, 187, 107, 45, 3, 75, 139)
| 271 | 40 | 186 | 132 | 186 | 132 | 99 | 230 | 229 | 56 | 245 | 264 | 95 | 3 | 187 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | bananas | in a | pile | on the | desk | . Each | banana | comes in a | package | of <num> | . <num> | bananas | are added to the | pile | . How many | bananas | are there in the | pile | ? <eos> | Addition | ilds |

### Top-10 (4 samples using it): (271, 40, 122, 165, 107, 45, 104, 85, 84)
| 271 | 40 | 122 | 165 | 107 | 45 | 104 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | apples | . <PER_2> | gives <PER_1> <num> more | . How many | apples | does <PER_1> have | in all | ? <eos> | Addition | ilds |

### Top-11 (4 samples using it): (271, 40, 13, 221, 13, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 13 | 221 | 13 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | plums | and <PER_2> picked <num> | plums | . <PER_3> picked <num> | pears | . How many | plums | were picked | in all | ? <eos> | Addition | ai2 |

### Top-12 (4 samples using it): (271, 40, 177, 119, 196, 68, 0, 107, 45, 214, 139)
| 271 | 40 | 177 | 119 | 196 | 68 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | tickets | . <PER_2> has | with <num> | tickets | . <PER_2> finds | another <num> | . How many | tickets | does <PER_2> end with | ? <eos> | Addition | ilds |

### Top-13 (4 samples using it): (271, 40, 93, 180, 131, 236, 178, 66, 21, 22, 107, 45, 3, 75, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 178 | 66 | 21 | 22 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | scissors | and <num> | pencils | in the | drawer | . <PER_1> placed <num> | scissors | in the | drawer | . How many | scissors | are now there in | total | ? <eos> | Addition | ai2 |

### Top-14 (3 samples using it): (271, 40, 68, 0, 107, 45, 104, 85, 84)
| 271 | 40 | 68 | 0 | 107 | 45 | 104 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | candies | . She buys <num> | more | . How many | candies | does <PER_1> have | in all | ? <eos> | Addition | ilds |

### Distribution of solution type: the 46 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 7 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-11 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-12 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-13 | 4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-14 | 3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 46 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |7 (1.000) |
| top-4 | 5 (1.000) |0 (0.000) |
| top-5 | 5 (1.000) |0 (0.000) |
| top-7 | 5 (1.000) |0 (0.000) |
| top-8 | 5 (1.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |
| top-11 | 0 (0.000) |4 (1.000) |
| top-12 | 4 (1.000) |0 (0.000) |
| top-13 | 0 (0.000) |4 (1.000) |
| top-14 | 3 (1.000) |0 (0.000) |

## Subtraction (254 samples)
### Top-2 (6 samples using it): (271, 40, 209, 3, 187, 107, 45, 214, 139)
| 271 | 40 | 209 | 3 | 187 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | blocks | . <num> | are eaten by a | hippopotamus | . How many | blocks | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-3 (5 samples using it): (271, 40, 13, 107, 45, 214, 139)
| 271 | 40 | 13 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | cards | . She loses <num> | . How many | cards | will <PER_1> have | ? <eos> | Subtraction | ilds |

### Top-4 (5 samples using it): (271, 40, 178, 66, 164, 214, 139)
| 271 | 40 | 178 | 66 | 164 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - |
| <PER_1> weighs <num> | pounds | . <PER_2> weighs <num> | pounds | . How much heavier | is <PER_1> than <PER_2> | ? <eos> | Subtraction | ilds |

### Top-5 (4 samples using it): (271, 40, 99, 230, 229, 165, 107, 45, 214, 139)
| 271 | 40 | 99 | 230 | 229 | 165 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <num> | oranges | . He | shares | <num> | with <PER_2> | . How many | oranges | will <PER_3> have | ? <eos> | Subtraction | ilds |

### Top-6 (4 samples using it): (271, 40, 186, 132, 13, 196, 47, 49, 139)
| 271 | 40 | 186 | 132 | 13 | 196 | 47 | 49 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | oranges | in a | box | . <PER_1> takes <num> | oranges | . How many | are left | ? <eos> | Subtraction | ilds |

### Top-7 (4 samples using it): (271, 40, 157, 265, 87, 238, 263, 75, 139)
| 271 | 40 | 157 | 265 | 87 | 238 | 263 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> baked <num> | muffins | . How many more | muffins | does <PER_1> have | to bake to | have <num> | muffins | ? <eos> | Subtraction | ilds |

### Top-8 (4 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 196, 0, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 196 | 0 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | dimes | and <num> | pennies | in her | bank | . Her | dad | borrowed <num> | pennies | from <PER_1> | . How many | pennies | does she have now | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (271, 40, 203, 196, 219, 197, 39, 139)
| 271 | 40 | 203 | 196 | 219 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| <PER_1> ran <num> | mile | and walked <num> | mile | . How much farther | did <PER_1> run than | walk | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (271, 40, 186, 132, 13, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 13 | 92 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | pennies | in his | bank | . He spent <num> | of his | pennies | . How many | pennies | does he have now | ? <eos> | Subtraction | ai2 |

### Top-11 (3 samples using it): (271, 40, 186, 132, 247, 119, 92, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 247 | 119 | 92 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | on the | beach | , she gave | <PER_2> <num> | of the | seashells | . How many | seashells | does she now have | ? <eos> | Subtraction | ai2 |

### Distribution of solution type: the 41 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-2 | 0 (0.000) |6 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-11 | 0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 41 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-2 | 6 (1.000) |0 (0.000) |
| top-3 | 5 (1.000) |0 (0.000) |
| top-4 | 5 (1.000) |0 (0.000) |
| top-5 | 4 (1.000) |0 (0.000) |
| top-6 | 4 (1.000) |0 (0.000) |
| top-7 | 4 (1.000) |0 (0.000) |
| top-8 | 0 (0.000) |4 (1.000) |
| top-9 | 0 (0.000) |3 (1.000) |
| top-10 | 0 (0.000) |3 (1.000) |
| top-11 | 0 (0.000) |3 (1.000) |

## CommonDiv (97 samples)
### Top-3 (5 samples using it): (271, 40, 232, 230, 229, 56, 89, 95, 3, 75, 253, 139)
| 271 | 40 | 232 | 230 | 229 | 56 | 89 | 95 | 3 | 75 | 253 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | erasers | . If he | shares | them among <num> | friends | , how many | erasers | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-4 (4 samples using it): (145, 40, 148, 42, 182, 53, 34, 197, 39, 139)
| 145 | 40 | 148 | 42 | 182 | 53 | 34 | 197 | 39 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> <unk> <num> | kilometers | at <num> | kilometers | per | hour | , how long | was <PER_1> | jogging | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (271, 40, 133, 162, 251, 72, 222, 254, 45, 214, 139)
| 271 | 40 | 133 | 162 | 251 | 72 | 222 | 254 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> sold <num> | boxes | of <MISC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does <PER_1> need | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (271, 40, 186, 132, 233, 172, 107, 45, 3, 75, 139)
| 271 | 40 | 186 | 132 | 233 | 172 | 107 | 45 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> is inviting <num> | friends | to a | party | . He has <num> | cookies | . How many | cookies | will each friend | get | ? <eos> | CommonDiv | ilds |

### Top-7 (4 samples using it): (271, 40, 186, 132, 177, 119, 196, 89, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 177 | 119 | 196 | 89 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | candies | stored in | boxes | . If there | are <num> | boxes | , how many | candies | must go in each | box | ? <eos> | CommonDiv | ilds |

### Top-8 (4 samples using it): (51, 160, 40, 17, 180, 237, 163, 245, 233, 172, 107, 45, 214, 139)
| 51 | 160 | 40 | 17 | 180 | 237 | 163 | 245 | 233 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> wants | to split a | collection | of | peanuts | into | groups | of <num> | . <PER_1> has <num> | peanuts | . How many | groups | will be created | ? <eos> | CommonDiv | ilds |

### Top-9 (4 samples using it): (271, 40, 186, 132, 203, 196, 44, 198, 183, 202, 2, 34, 153, 108, 85, 84)
| 271 | 40 | 186 | 132 | 203 | 196 | 44 | 198 | 183 | 202 | 2 | 34 | 153 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | students | in the | class | and <num> | apples | . If the | apples | are divided equally | among the | students | , how many | does each | student | get | ? <eos> | CommonDiv | ilds |

### Top-10 (4 samples using it): (96, 95, 3, 71, 132, 13, 221, 203, 196, 92, 260, 180, 157, 265, 142, 76, 75, 139)
| 96 | 95 | 3 | 71 | 132 | 13 | 221 | 203 | 196 | 92 | 260 | 180 | 157 | 265 | 142 | 76 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | school | is planning a | field | trip | . There are <num> | students | and <num> | seats | on each | school | bus | . How many | buses | are needed | to take the | trip | ? <eos> | CommonDiv | ilds |

### Top-11 (4 samples using it): (271, 40, 183, 73, 186, 132, 122, 73, 148, 42, 182, 53, 55, 177, 119, 196, 89, 95, 3, 75, 139)
| 271 | 40 | 183 | 73 | 186 | 132 | 122 | 73 | 148 | 42 | 182 | 53 | 55 | 177 | 119 | 196 | 89 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | oranges | that must be | put away | in | boxes | . <PER_2> comes | to help | and brings <num> | cookies | to | share | with <PER_1> | . If there | are <num> | boxes | , how many | oranges | must go in each | box | ? <eos> | CommonDiv | ilds |

### Top-12 (3 samples using it): (145, 40, 23, 199, 251, 72, 222, 43, 59, 76, 75, 253, 139)
| 145 | 40 | 23 | 199 | 251 | 72 | 222 | 43 | 59 | 76 | 75 | 253 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> sold <num> | boxes | of <MISC_1> | , how many | cases | of <num> | boxes | does <MISC_2> | <unk> | from the | cookie | mom | ? <eos> | CommonDiv | ilds |

### Distribution of solution type: the 40 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-3 | 0 (0.000) |0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-11 | 0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-12 | 0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 40 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-3 | 5 (1.000) |0 (0.000) |
| top-4 | 4 (1.000) |0 (0.000) |
| top-5 | 4 (1.000) |0 (0.000) |
| top-6 | 4 (1.000) |0 (0.000) |
| top-7 | 4 (1.000) |0 (0.000) |
| top-8 | 4 (1.000) |0 (0.000) |
| top-9 | 4 (1.000) |0 (0.000) |
| top-10 | 4 (1.000) |0 (0.000) |
| top-11 | 4 (1.000) |0 (0.000) |
| top-12 | 3 (1.000) |0 (0.000) |

## Multiplication (93 samples)
### Top-1 (5 samples using it): (90, 119, 196, 148, 42, 182, 53, 219, 197, 84)
| 90 | 119 | 196 | 148 | 42 | 182 | 53 | 219 | 197 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> wandered | for <num> | hours | at <num> | miles | per | hour | . How far | did <PER_1> go | ? <eos> | Multiplication | ilds |

### Top-2 (4 samples using it): (271, 40, 17, 180, 99, 230, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | boxes | of | peanuts | . Each | box | holds <num> | peanuts | . How many | peanuts | does <PER_1> have | ? <eos> | Multiplication | ilds |

### Top-3 (3 samples using it): (271, 40, 186, 132, 272, 95, 3, 75, 139)
| 271 | 40 | 186 | 132 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | crayons | in each | box | . How many | crayons | are in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-4 (3 samples using it): (271, 40, 17, 180, 99, 230, 229, 196, 178, 66, 21, 22, 107, 45, 214, 139)
| 271 | 40 | 17 | 180 | 99 | 230 | 229 | 196 | 178 | 66 | 21 | 22 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | boxes | of | eggs | . Each | box | holds <num> | eggs | and there are <num> | boxes | in a | <unk> | . How many | eggs | does <PER_1> have | ? <eos> | Multiplication | ilds |

### Top-5 (3 samples using it): (200, 205, 243, 160, 40, 148, 42, 182, 53, 219, 197, 270, 59, 270, 75, 139)
| 200 | 205 | 243 | 160 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 270 | 59 | 270 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It took <PER_1> <num> | hours | to stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-6 (3 samples using it): (271, 40, 93, 180, 131, 236, 178, 66, 147, 234, 270, 172, 107, 45, 142, 76, 75, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 270 | 172 | 107 | 45 | 142 | 76 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> went to the | store | <num> | times | last | month | . He buys <num> | bananas | each | time | he goes to the | store | . How many | bananas | did <PER_1> buy | last | month | ? <eos> | Multiplication | ilds |

### Top-7 (2 samples using it): (41, 205, 25, 54, 98, 256, 85, 84)
| 41 | 205 | 25 | 54 | 98 | 256 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - |
| Each | <unk> | costs $ <num> | . How much | do <num> | tickets | cost | ? <eos> | Multiplication | ilds |

### Top-8 (2 samples using it): (41, 205, 93, 180, 177, 119, 196, 89, 95, 3, 75, 139)
| 41 | 205 | 93 | 180 | 177 | 119 | 196 | 89 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | candies | . If there | are <num> | children | , how many | candies | are there in | total | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (41, 205, 119, 196, 69, 12, 119, 196, 144, 265, 10, 3, 75, 139)
| 41 | 205 | 119 | 196 | 69 | 12 | 119 | 196 | 144 | 265 | 10 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | bottle | caps | . If there | are <num> | children | , how many | bottle | caps | are there in | total | ? <eos> | Multiplication | ilds |

### Top-10 (1 samples using it): (41, 205, 119, 196, 164, 153, 108, 85, 84)
| 41 | 205 | 119 | 196 | 164 | 153 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| <unk> | pencil | weighs <num> | grams | . How much | do <num> | pencils | weigh | ? <eos> | Multiplication | ilds |

### Distribution of solution type: the 28 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |5 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |4 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 28 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 5 (1.000) |0 (0.000) |
| top-2 | 4 (1.000) |0 (0.000) |
| top-3 | 3 (1.000) |0 (0.000) |
| top-4 | 3 (1.000) |0 (0.000) |
| top-5 | 3 (1.000) |0 (0.000) |
| top-6 | 3 (1.000) |0 (0.000) |
| top-7 | 2 (1.000) |0 (0.000) |
| top-8 | 2 (1.000) |0 (0.000) |
| top-9 | 2 (1.000) |0 (0.000) |
| top-10 | 1 (1.000) |0 (0.000) |

## TimeVariantUnknownFinal (35 samples)
### Top-1 (2 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 13, 221, 203, 196, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 13 | 221 | 203 | 196 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> placed <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-2 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served <num> | cakes | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | cakes | yesterday | . How many | cakes | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-3 (1 samples using it): (271, 40, 177, 119, 196, 68, 228, 172, 107, 45, 214, 139)
| 271 | 40 | 177 | 119 | 196 | 68 | 228 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> <MISC_1> | cards | . <PER_2> gave | her <num> new <MISC_1> | cards | . <PER_1> bought <num> | <MISC_1> | cards | . How many <MISC_1> | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (1 samples using it): (271, 40, 186, 132, 99, 230, 229, 66, 147, 234, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 186 | 132 | 99 | 230 | 229 | 66 | 147 | 234 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | dimes | in her | bank | . Her | dad | gave her <num> | dimes | and her | mother | gave her <num> | dimes | . How many | dimes | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (271, 40, 131, 236, 93, 180, 131, 236, 178, 66, 147, 234, 272, 95, 3, 75, 139)
| 271 | 40 | 131 | 236 | 93 | 180 | 131 | 236 | 178 | 66 | 147 | 234 | 272 | 95 | 3 | 75 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There are <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> placed <num> | pencils | on the | desk | . How many | pencils | are now there in | total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (1 samples using it): (41, 205, 148, 42, 182, 53, 215, 71, 132, 99, 230, 229, 56, 203, 196, 69, 52, 227, 32, 85, 84)
| 41 | 205 | 148 | 42 | 182 | 53 | 215 | 71 | 132 | 99 | 230 | 229 | 56 | 203 | 196 | 69 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served <num> | pies | during | lunch | and <num> during | dinner | today | . The | restaurant | served <num> | pies | and <num> | pizzas | yesterday | . How many | pies | were served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (1 samples using it): (41, 205, 177, 119, 196, 80, 237, 163, 82, 202, 2, 67, 144, 265, 252, 139)
| 41 | 205 | 177 | 119 | 196 | 80 | 237 | 163 | 82 | 202 | 2 | 67 | 144 | 265 | 252 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <unk> <unk> | <unk> | . <PER_1> paid | $ <num> for | <unk> | , $ <num> | for | apples | , and $ <num> | for | peaches | . In total | , how much | money | did she spend | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (1 samples using it): (161, 260, 180, 245, 257, 71, 132, 245, 137, 221, 245, 219, 197, 39, 253, 139)
| 161 | 260 | 180 | 245 | 257 | 71 | 132 | 245 | 137 | 221 | 245 | 219 | 197 | 39 | 253 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> purchased a | football | game | for $ <num> | , a | <unk> | game | for $ <num> | , and a <MISC_1> | game | for $ <num> | . How much | did <PER_1> spend on | video | games | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (271, 40, 93, 180, 131, 236, 99, 230, 229, 56, 258, 198, 229, 172, 107, 45, 214, 139)
| 271 | 40 | 93 | 180 | 131 | 236 | 99 | 230 | 229 | 56 | 258 | 198 | 229 | 172 | 107 | 45 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | quarters | and <num> | pennies | in her | bank | . Her | dad | gave her <num> | pennies | and her | mother | gave her <num> | pennies | . How many | pennies | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (1 samples using it): (161, 260, 180, 82, 78, 177, 119, 196, 69, 13, 196, 22, 107, 45, 143, 214, 139)
| 161 | 260 | 180 | 82 | 78 | 177 | 119 | 196 | 69 | 13 | 196 | 22 | 107 | 45 | 143 | 214 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> had <num> | baseball | cards | , and <num> | were torn | . <PER_2> gave | <PER_1> <num> new | baseball | cards | . <PER_1> bought <num> | baseball | cards | . How many | baseball | cards | does <PER_1> have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Distribution of solution type: the 11 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 11 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |2 (1.000) |
| top-2 | 0 (0.000) |1 (1.000) |
| top-3 | 0 (0.000) |1 (1.000) |
| top-4 | 0 (0.000) |1 (1.000) |
| top-5 | 0 (0.000) |1 (1.000) |
| top-6 | 0 (0.000) |1 (1.000) |
| top-7 | 0 (0.000) |1 (1.000) |
| top-8 | 0 (0.000) |1 (1.000) |
| top-9 | 0 (0.000) |1 (1.000) |
| top-10 | 0 (0.000) |1 (1.000) |

## Sum (25 samples)
### Top-1 (3 samples using it): (271, 40, 178, 66, 247, 119, 196, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> | books | , <PER_2> has <num> | books | , and <PER_3> | has <num> | books | . How many | books | do they have | together | ? <eos> | Sum | ai2 |

### Top-2 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 |

### Top-3 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 267 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> blue | balloons | , <PER_2> has <num> | blue | balloons | , and <PER_3> | has <num> blue | balloons | . How many blue | balloons | do they have | in all | ? <eos> | Sum | ai2 |

### Top-4 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 203, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 203 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | limes | , <PER_2> picked <num> | limes | , and <PER_3> | picked <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were picked | in total | ? <eos> | Sum | ai2 |

### Top-5 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 12, 119, 196, 147, 234, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 12 | 119 | 196 | 147 | 234 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> grew <num> | pumpkins | , <PER_2> grew <num> | pumpkins | , and <PER_3> | grew <num> | pumpkins | . They worked | for <num> | days | on the | farm | . How many | pumpkins | did they grow | in all | ? <eos> | Sum | ai2 |

### Top-6 (2 samples using it): (271, 40, 68, 228, 198, 247, 119, 196, 99, 230, 229, 56, 267, 227, 32, 85, 84)
| 271 | 40 | 68 | 228 | 198 | 247 | 119 | 196 | 99 | 230 | 229 | 56 | 267 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> has <num> red | balloons | , <PER_2> has <num> | red | balloons | , and <PER_3> | has <num> red | balloons | . The | balloons | cost <num> | dollars | . How many red | balloons | do they have | in all | ? <eos> | Sum | ai2 |

### Top-7 (2 samples using it): (271, 40, 178, 66, 247, 119, 196, 147, 234, 67, 78, 247, 119, 78, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 147 | 234 | 67 | 78 | 247 | 119 | 78 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> found <num> | seashells | , <PER_2> found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . When they | cleaned them | , they discovered | that <num> | were cracked | . How many | seashells | did they find | together | ? <eos> | Sum | ai2 |

### Top-8 (1 samples using it): (271, 40, 178, 66, 247, 119, 196, 257, 71, 132, 52, 227, 32, 85, 84)
| 271 | 40 | 178 | 66 | 247 | 119 | 196 | 257 | 71 | 132 | 52 | 227 | 32 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> picked <num> | plums | , <PER_2> picked <num> | plums | , and <PER_3> | picked <num> | plums | from the | <unk> | tree | . How many | plums | were picked | in total | ? <eos> | Sum | ai2 |

### Top-9 (1 samples using it): (261, 260, 180, 148, 42, 182, 53, 27, 251, 72, 222, 27, 251, 72, 222, 162, 251, 72, 222, 98, 256, 108, 85, 84)
| 261 | 260 | 180 | 148 | 42 | 182 | 53 | 27 | 251 | 72 | 222 | 27 | 251 | 72 | 222 | 162 | 251 | 72 | 222 | 98 | 256 | 108 | 85 | 84 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | company | <unk> <num> | ton | of | <unk> | , <num> | ton | of | <unk> | , and <num> | ton | of | <unk> | . How many | tons | of | <unk> | did the | company | <unk> | in all | ? <eos> | Sum | ai2 |

### Top-10 (1 samples using it): (271, 40, 257, 71, 132, 13, 42, 182, 53, 27, 251, 72, 222, 27, 251, 72, 222, 162, 251, 72, 222, 252, 139)
| 271 | 40 | 257 | 71 | 132 | 13 | 42 | 182 | 53 | 27 | 251 | 72 | 222 | 27 | 251 | 72 | 222 | 162 | 251 | 72 | 222 | 252 | 139 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> made trail | mix | for a | <unk> | trip | . She used <num> | pound | of | peanuts | , <num> | pound | of chocolate | <unk> | , and <num> | pound | of | <unk> | . How many | pounds | of trail | mix | did <PER_1> make | ? <eos> | Sum | ai2 |

### Distribution of solution type: the 18 samples using all top-10 templates
|   | Addition | Subtraction | CommonDiv | Multiplication | TimeVariantUnknownFinal | Sum | SubtractionTimeVariantUnknownFinal | skip | TimeVariantUnknownInitial |
| - | - | - | - | - | - | - | - | - | - |
| top-1 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |3 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-2 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-3 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-4 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-5 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-6 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-7 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |2 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-8 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-9 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
| top-10 | 0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |0 (0.000) |1 (1.000) |0 (0.000) |0 (0.000) |0 (0.000) |
### Distribution of source: the 18 samples using all top-10 templates
|   | ilds | ai2 |
| - | - | - |
| top-1 | 0 (0.000) |3 (1.000) |
| top-2 | 0 (0.000) |2 (1.000) |
| top-3 | 0 (0.000) |2 (1.000) |
| top-4 | 0 (0.000) |2 (1.000) |
| top-5 | 0 (0.000) |2 (1.000) |
| top-6 | 0 (0.000) |2 (1.000) |
| top-7 | 0 (0.000) |2 (1.000) |
| top-8 | 0 (0.000) |1 (1.000) |
| top-9 | 0 (0.000) |1 (1.000) |
| top-10 | 0 (0.000) |1 (1.000) |

