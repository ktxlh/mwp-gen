Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='gens/gen-srl-ai2-ilds-300-55-5-far.md', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-55-5-far.txt')
# Analysis on segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-55-5-far.txt
k=10
n=1
# Overall - top templates
### Top-1 (5 samples using it): (161, 7, 98, 154, 76, 218, 261, 98, 94, 161, 125, 196)
| 161 | 7 | 98 | 154 | 76 | 218 | 261 | 98 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (5 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 148, 42, 217, 112)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 148 | 42 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | carrots | . <PER_2> | grew <num> | carrots | . How many | carrots | did they | grow | in total | ? <eos> | Addition | ai2 |

### Top-3 (5 samples using it): (161, 7, 98, 274, 38, 42, 219, 261, 98, 94, 161, 76, 2)
| 161 | 7 | 98 | 274 | 38 | 42 | 219 | 261 | 98 | 94 | 161 | 76 | 2 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-4 (5 samples using it): (161, 7, 98, 215, 68, 76, 218, 261, 98, 177, 9, 161, 225, 217, 112)
| 161 | 7 | 98 | 215 | 68 | 76 | 218 | 261 | 98 | 177 | 9 | 161 | 225 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-5 (4 samples using it): (161, 7, 98, 61, 263, 20, 257, 94, 161, 125, 196)
| 161 | 7 | 98 | 61 | 263 | 20 | 257 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | strolled <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 83, 54, 251)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 83 | 54 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | books | . <PER_2> | has <num> | books | . How many | books | do | they have together | ? <eos> | Addition | ai2 |

### Top-7 (4 samples using it): (161, 76, 218, 177, 178, 117, 171, 261, 98, 94, 161, 98, 118, 251)
| 161 | 76 | 218 | 177 | 178 | 117 | 171 | 261 | 98 | 94 | 161 | 98 | 118 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | pencils | . He | gives <num> | to <PER_2> | . How many | pencils | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-8 (4 samples using it): (161, 7, 98, 274, 81, 219, 10, 257, 98, 93, 144, 200, 196)
| 161 | 7 | 98 | 274 | 81 | 219 | 10 | 257 | 98 | 93 | 144 | 200 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-9 (4 samples using it): (161, 9, 121, 144, 211, 102, 98, 274, 38, 55, 202, 232, 250, 186, 107, 224, 251)
| 161 | 9 | 121 | 144 | 211 | 102 | 98 | 274 | 38 | 55 | 202 | 232 | 250 | 186 | 107 | 224 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-10 (4 samples using it): (161, 7, 98, 274, 177, 98, 274, 12, 21, 42, 61, 15, 37, 7, 98, 57)
| 161 | 7 | 98 | 274 | 177 | 98 | 274 | 12 | 21 | 42 | 61 | 15 | 37 | 7 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is each | group | ? <eos> | CommonDiv | ilds |


# Solution type - top templates
## Addition (267 samples)
### Top-1 (5 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 148, 42, 217, 112)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 148 | 42 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | carrots | . <PER_2> | grew <num> | carrots | . How many | carrots | did they | grow | in total | ? <eos> | Addition | ai2 |

### Top-2 (5 samples using it): (161, 7, 98, 274, 38, 42, 219, 261, 98, 94, 161, 76, 2)
| 161 | 7 | 98 | 274 | 38 | 42 | 219 | 261 | 98 | 94 | 161 | 76 | 2 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-3 (5 samples using it): (161, 7, 98, 215, 68, 76, 218, 261, 98, 177, 9, 161, 225, 217, 112)
| 161 | 7 | 98 | 215 | 68 | 76 | 218 | 261 | 98 | 177 | 9 | 161 | 225 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-4 (4 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 83, 54, 251)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 83 | 54 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | books | . <PER_2> | has <num> | books | . How many | books | do | they have together | ? <eos> | Addition | ai2 |

### Top-5 (3 samples using it): (161, 7, 98, 264, 67, 156, 138, 41, 266, 221, 251)
| 161 | 7 | 98 | 264 | 67 | 156 | 138 | 41 | 266 | 221 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | cards | . <num> | cards more | are | added | . How many | are | there total | ? <eos> | Addition | ilds |

### Top-6 (3 samples using it): (161, 76, 218, 177, 178, 76, 218, 261, 98, 194, 51, 191, 173, 86)
| 161 | 76 | 218 | 177 | 178 | 76 | 218 | 261 | 98 | 194 | 51 | 191 | 173 | 86 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | apples | . She | finds | another <num> | . How many | apples | does | <PER_1> | end | with | ? <eos> | Addition | ilds |

### Top-7 (3 samples using it): (161, 7, 98, 123, 9, 171, 261, 98, 94, 161, 9, 107, 31)
| 161 | 7 | 98 | 123 | 9 | 171 | 261 | 98 | 94 | 161 | 9 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | oranges | . He | finds | another <num> | . How many | oranges | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-8 (3 samples using it): (161, 7, 98, 99, 207, 274, 261, 98, 200, 106, 83, 107, 31)
| 161 | 7 | 98 | 99 | 207 | 274 | 261 | 98 | 200 | 106 | 83 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | tickets | . <PER_2> | gives | <PER_1> <num> more | . How many | tickets | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-9 (3 samples using it): (161, 7, 98, 61, 7, 98, 166, 48, 41, 153, 148, 42, 86)
| 161 | 7 | 98 | 61 | 7 | 98 | 166 | 48 | 41 | 153 | 148 | 42 | 86 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . How many | seashells | did they | find together | ? <eos> | Addition | ai2 |

### Top-10 (3 samples using it): (161, 7, 98, 178, 136, 109, 261, 98, 94, 161, 9, 107, 31)
| 161 | 7 | 98 | 178 | 136 | 109 | 261 | 98 | 94 | 161 | 9 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | stickers | . She | gets | <num> more from <PER_2> | . How many | stickers | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |


## Subtraction (257 samples)
### Top-1 (5 samples using it): (161, 7, 98, 154, 76, 218, 261, 98, 94, 161, 125, 196)
| 161 | 7 | 98 | 154 | 76 | 218 | 261 | 98 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (4 samples using it): (161, 76, 218, 177, 178, 117, 171, 261, 98, 94, 161, 98, 118, 251)
| 161 | 76 | 218 | 177 | 178 | 117 | 171 | 261 | 98 | 94 | 161 | 98 | 118 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | pencils | . He | gives <num> | to <PER_2> | . How many | pencils | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-3 (3 samples using it): (161, 148, 43, 107, 137, 209, 155, 43, 206, 76, 62, 251)
| 161 | 148 | 43 | 107 | 137 | 209 | 155 | 43 | 206 | 76 | 62 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | oranges | in a | box | . <PER_1> | takes <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-4 (3 samples using it): (161, 76, 218, 177, 178, 117, 171, 261, 98, 194, 51, 191, 173, 86)
| 161 | 76 | 218 | 177 | 178 | 117 | 171 | 261 | 98 | 194 | 51 | 191 | 173 | 86 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | eggs | . He | gives <num> | to <MISC_1> | . How many | eggs | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-5 (3 samples using it): (161, 258, 177, 98, 99, 62, 109, 177, 98, 151, 177, 98, 194, 51, 258, 196)
| 161 | 258 | 177 | 98 | 99 | 62 | 109 | 177 | 98 | 151 | 177 | 98 | 194 | 51 | 258 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | baseball | cards | . <PER_2> | bought <num> | of <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |

### Top-6 (3 samples using it): (161, 7, 98, 166, 98, 99, 186, 80, 153, 166, 98, 41, 153, 7, 207, 166, 98, 57)
| 161 | 7 | 98 | 166 | 98 | 99 | 186 | 80 | 153 | 166 | 98 | 41 | 153 | 7 | 207 | 166 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | removes <num> | pencils | from a | jar | . There | were | originally <num> | pencils | in the | jar | . How many | pencils | are | left | in the | jar | ? <eos> | Subtraction | ilds |

### Top-7 (3 samples using it): (161, 7, 98, 61, 263, 221, 103, 13, 258, 166, 98, 61, 41, 153, 83, 54, 115, 251)
| 161 | 7 | 98 | 61 | 263 | 221 | 103 | 13 | 258 | 166 | 98 | 61 | 41 | 153 | 83 | 54 | 115 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found <num> | seashells | and <num> | <unk> | on the | beach | . She | gave <num> | of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |

### Top-8 (3 samples using it): (161, 223, 121, 144, 43, 18, 142, 255, 99, 62, 109, 177, 98, 151, 177, 98, 200, 106, 197, 74, 251)
| 161 | 223 | 121 | 144 | 43 | 18 | 142 | 255 | 99 | 62 | 109 | 177 | 98 | 151 | 177 | 98 | 200 | 106 | 197 | 74 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought <num> | of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (161, 7, 98, 166, 98, 264, 7, 98, 240, 77, 209, 7, 98, 274, 59, 151, 177, 186, 207, 166, 98, 57)
| 161 | 7 | 98 | 166 | 98 | 264 | 7 | 98 | 240 | 77 | 209 | 7 | 98 | 274 | 59 | 151 | 177 | 186 | 207 | 166 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | candies | in a | box | . <PER_1> | has <num> | candies | in a | bag | . <PER_2> | takes <num> | candies | out of the | box | . How many | candies | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-10 (2 samples using it): (161, 7, 98, 123, 203, 261, 98, 94, 161, 125, 196)
| 161 | 7 | 98 | 123 | 203 | 261 | 98 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | cards | . She | loses <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |


## CommonDiv (95 samples)
### Top-1 (4 samples using it): (161, 7, 98, 61, 263, 20, 257, 94, 161, 125, 196)
| 161 | 7 | 98 | 61 | 263 | 20 | 257 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | strolled <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-2 (4 samples using it): (161, 7, 98, 274, 81, 219, 10, 257, 98, 93, 144, 200, 196)
| 161 | 7 | 98 | 274 | 81 | 219 | 10 | 257 | 98 | 93 | 144 | 200 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-3 (4 samples using it): (161, 9, 121, 144, 211, 102, 98, 274, 38, 55, 202, 232, 250, 186, 107, 224, 251)
| 161 | 9 | 121 | 144 | 211 | 102 | 98 | 274 | 38 | 55 | 202 | 232 | 250 | 186 | 107 | 224 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-4 (4 samples using it): (161, 7, 98, 274, 177, 98, 274, 12, 21, 42, 61, 15, 37, 7, 98, 57)
| 161 | 7 | 98 | 274 | 177 | 98 | 274 | 12 | 21 | 42 | 61 | 15 | 37 | 7 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is each | group | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (161, 7, 98, 166, 98, 73, 232, 109, 177, 186, 207, 274, 232, 257, 93, 144, 200, 196)
| 161 | 7 | 98 | 166 | 98 | 73 | 232 | 109 | 177 | 186 | 207 | 274 | 232 | 257 | 93 | 144 | 200 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does each | student | get | ? <eos> | CommonDiv | ilds |

### Top-6 (4 samples using it): (161, 125, 219, 77, 209, 4, 121, 144, 109, 180, 54, 150, 99, 186, 80, 153, 63, 83, 102, 13, 94, 161, 125, 196)
| 161 | 125 | 219 | 77 | 209 | 4 | 121 | 144 | 109 | 180 | 54 | 150 | 99 | 186 | 80 | 153 | 63 | 83 | 102 | 13 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get | there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |

### Top-7 (4 samples using it): (161, 223, 121, 144, 200, 7, 98, 61, 237, 68, 262, 228, 258, 11, 172, 176, 237, 16, 42, 157, 106, 257, 110, 36, 199, 257, 125, 42, 9, 107, 203, 251)
| 161 | 223 | 121 | 144 | 200 | 7 | 98 | 61 | 237 | 68 | 262 | 228 | 258 | 11 | 172 | 176 | 237 | 16 | 42 | 157 | 106 | 257 | 110 | 36 | 199 | 257 | 125 | 42 | 9 | 107 | 203 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with | <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-8 (3 samples using it): (161, 7, 98, 61, 263, 56, 41, 195, 161, 229, 251)
| 161 | 7 | 98 | 61 | 263 | 56 | 41 | 195 | 161 | 229 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled <num> | miles | at <num> | miles | per hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |

### Top-9 (3 samples using it): (161, 7, 98, 61, 263, 20, 257, 76, 54, 251)
| 161 | 7 | 98 | 61 | 263 | 20 | 257 | 76 | 54 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | jogged <num> | kilometers | at <num> | kilometers | per hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-10 (3 samples using it): (161, 7, 98, 218, 261, 98, 163, 43, 109, 177, 9, 161, 125, 196)
| 161 | 7 | 98 | 218 | 261 | 98 | 163 | 43 | 109 | 177 | 9 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | sold <num> | boxes | of <LOC_1> | . How many | cases | of <num> | boxes | , plus extra | boxes | does | <PER_1> | need | ? <eos> | CommonDiv | ilds |


## Multiplication (93 samples)
### Top-1 (3 samples using it): (161, 62, 12, 52, 263, 151, 177, 186, 20, 40, 167)
| 161 | 62 | 12 | 52 | 263 | 151 | 177 | 186 | 20 | 40 | 167 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |

### Top-2 (3 samples using it): (161, 76, 218, 177, 218, 109, 96, 195, 161, 98, 57)
| 161 | 76 | 218 | 177 | 218 | 109 | 96 | 195 | 161 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | wandered | for <num> | hours | at <num> | miles per hour | . How far | did | <PER_1> | go | ? <eos> | Multiplication | ilds |

### Top-3 (3 samples using it): (161, 7, 98, 102, 98, 99, 204, 7, 98, 151, 177, 9, 161, 229, 251)
| 161 | 7 | 98 | 102 | 98 | 99 | 204 | 7 | 98 | 151 | 177 | 9 | 161 | 229 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | boxes | of | crayons | . Each | box | holds <num> | crayons | . How many | crayons | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-4 (3 samples using it): (161, 76, 218, 153, 63, 83, 54, 137, 273, 38, 70, 233, 266, 164, 213, 164, 213, 57)
| 161 | 76 | 218 | 153 | 63 | 83 | 54 | 137 | 273 | 38 | 70 | 233 | 266 | 164 | 213 | 164 | 213 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles per | hour | . How far | is | it between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |

### Top-5 (2 samples using it): (161, 98, 76, 218, 96, 7, 98, 140, 196)
| 161 | 98 | 76 | 218 | 96 | 7 | 98 | 140 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do <num> | bananas | cost | ? <eos> | Multiplication | ilds |

### Top-6 (2 samples using it): (161, 125, 7, 98, 41, 153, 203, 180, 170, 31)
| 161 | 125 | 7 | 98 | 41 | 153 | 203 | 180 | 170 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | has <num> | legs | . How many | legs | do <num> | bees | have | ? <eos> | Multiplication | ilds |

### Top-7 (2 samples using it): (161, 125, 7, 98, 274, 38, 153, 202, 232, 227, 107, 31)
| 161 | 125 | 7 | 98 | 274 | 38 | 153 | 202 | 232 | 227 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | pencils | . If there | are <num> | children | , how many | pencils | are there | in total | ? <eos> | Multiplication | ilds |

### Top-8 (2 samples using it): (161, 125, 7, 98, 242, 164, 117, 232, 257, 98, 177, 186, 107, 243, 251)
| 161 | 125 | 7 | 98 | 242 | 164 | 117 | 232 | 257 | 98 | 177 | 186 | 107 | 243 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | child | has <num> | bottle | caps | . If there | are <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-9 (2 samples using it): (161, 7, 98, 102, 98, 264, 7, 98, 221, 180, 261, 268, 102, 98, 200, 161, 229, 251)
| 161 | 7 | 98 | 102 | 98 | 264 | 7 | 98 | 221 | 180 | 261 | 268 | 102 | 98 | 200 | 161 | 229 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | packages | of | gum | . There | are <num> | pieces | in each | package | . How many | pieces | of | gum | does | <PER_1> | have | ? <eos> | Multiplication | ilds |

### Top-10 (2 samples using it): (161, 7, 98, 102, 98, 99, 204, 7, 98, 61, 7, 98, 240, 43, 206, 132, 5, 216, 26, 31)
| 161 | 7 | 98 | 102 | 98 | 99 | 204 | 7 | 98 | 61 | 7 | 98 | 240 | 43 | 206 | 132 | 5 | 216 | 26 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | boxes | of | blocks | . Each | box | holds <num> | blocks | and there | are <num> | boxes | in a | <unk> | . How many | blocks | does | <PER_1> | have | ? <eos> | Multiplication | ilds |


## TimeVariantUnknownFinal (30 samples)
### Top-1 (1 samples using it): (161, 7, 98, 272, 175, 44, 38, 42, 61, 263, 226, 125, 42, 61, 263, 151, 177, 186, 51, 258, 196)
| 161 | 7 | 98 | 272 | 175 | 44 | 38 | 42 | 61 | 263 | 226 | 125 | 42 | 61 | 263 | 151 | 177 | 186 | 51 | 258 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had <num> | dimes | in her | bank | . Her | dad | gave | her <num> | dimes | and her | mother | gave | her <num> | dimes | . How many | dimes | does | <PER_1> | have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-2 (1 samples using it): (161, 125, 38, 55, 29, 238, 54, 44, 15, 7, 98, 73, 232, 35, 261, 98, 76, 186, 107, 31)
| 161 | 125 | 38 | 55 | 29 | 238 | 54 | 44 | 15 | 7 | 98 | 73 | 232 | 35 | 261 | 98 | 76 | 186 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served <num> | pies during | lunch | and <num> | during dinner today | . The | restaurant | served <num> | pies | and <num> | pizzas | yesterday | . How many | pies | were | served | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-3 (1 samples using it): (161, 7, 98, 166, 98, 73, 177, 111, 77, 209, 7, 98, 166, 34, 151, 177, 186, 80, 162, 251)
| 161 | 7 | 98 | 166 | 98 | 73 | 177 | 111 | 77 | 209 | 7 | 98 | 166 | 34 | 151 | 177 | 186 | 80 | 162 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | pencils | in the | drawer | and <num> | pencils | on the | desk | . <PER_1> | placed <num> | pencils | on the | desk | . How many | pencils | are | now there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-4 (1 samples using it): (161, 7, 98, 61, 263, 107, 224, 209, 125, 42, 61, 263, 226, 125, 42, 61, 263, 151, 177, 186, 51, 258, 196)
| 161 | 7 | 98 | 61 | 263 | 107 | 224 | 209 | 125 | 42 | 61 | 263 | 226 | 125 | 42 | 61 | 263 | 151 | 177 | 186 | 51 | 258 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had <num> | pennies | and <num> | nickels | in her | bank | . Her | dad | gave | her <num> | nickels | and her | mother | gave | her <num> | nickels | . How many | nickels | does | <PER_1> | have now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-5 (1 samples using it): (161, 125, 42, 150, 99, 186, 80, 98, 274, 232, 257, 116, 98, 274, 257, 125, 42, 157, 249, 31)
| 161 | 125 | 42 | 150 | 99 | 186 | 80 | 98 | 274 | 232 | 257 | 116 | 98 | 274 | 257 | 125 | 42 | 157 | 249 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> | <unk> | <unk> | . <PER_1> | paid | $ <num> for | <unk> | , $ <num> for | apples | , and $ | <num> for | peaches | . In total | , how much | money | did | she | spend | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-6 (1 samples using it): (161, 258, 177, 98, 218, 202, 177, 98, 163, 257, 98, 273, 41, 156, 271, 248, 102, 98, 122, 222)
| 161 | 258 | 177 | 98 | 218 | 202 | 177 | 98 | 163 | 257 | 98 | 273 | 41 | 156 | 271 | 248 | 102 | 98 | 122 | 222 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | purchased a | football | game | for $ <num> | , a | <unk> | game | for $ <num> | , and a <MISC_1> | game | for $ <num> | . How much | did | <PER_1> | spend | on | video | games | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-7 (1 samples using it): (161, 7, 98, 166, 98, 73, 177, 111, 77, 209, 7, 98, 73, 177, 111, 77, 151, 177, 186, 80, 162, 251)
| 161 | 7 | 98 | 166 | 98 | 73 | 177 | 111 | 77 | 209 | 7 | 98 | 73 | 177 | 111 | 77 | 151 | 177 | 186 | 80 | 162 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | erasers | in the | drawer | and <num> | erasers | on the | desk | . <PER_1> | placed <num> | erasers | and <num> | rulers | on the | desk | . How many | erasers | are | now there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-8 (1 samples using it): (161, 7, 98, 166, 98, 73, 177, 111, 137, 209, 117, 232, 18, 43, 166, 192, 151, 177, 186, 80, 162, 251)
| 161 | 7 | 98 | 166 | 98 | 73 | 177 | 111 | 137 | 209 | 117 | 232 | 18 | 43 | 166 | 192 | 151 | 177 | 186 | 80 | 162 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | crayons | in the | drawer | and <num> | crayons | on the | desk | . <PER_1> | placed <num> | crayons | and <num> | scissors | on the | desk | . How many | crayons | are | now there | in total | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-9 (1 samples using it): (161, 223, 121, 144, 82, 183, 17, 101, 209, 4, 216, 69, 232, 137, 209, 4, 121, 144, 43, 206, 177, 98, 215, 197, 74, 251)
| 161 | 223 | 121 | 144 | 82 | 183 | 17 | 101 | 209 | 4 | 216 | 69 | 232 | 137 | 209 | 4 | 121 | 144 | 43 | 206 | 177 | 98 | 215 | 197 | 74 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | gave | <PER_1> | <num> new | baseball | cards | . <PER_1> | bought | <num> | baseball | cards | . How many | baseball | cards | does <PER_1> | have | now | ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-10 (1 samples using it): (161, 9, 171, 144, 200, 103, 13, 174, 218, 177, 98, 202, 28, 236, 76, 218, 177, 98, 41, 153, 7, 63, 83, 107, 31)
| 161 | 9 | 171 | 144 | 200 | 103 | 13 | 174 | 218 | 177 | 98 | 202 | 28 | 236 | 76 | 218 | 177 | 98 | 41 | 153 | 7 | 63 | 83 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to <num> | football | games this | month | . He | went | to <num> | games last | month | , and | <unk> | to | go | to <num> | games next | month | . How many | games | will | he | <unk> | in all | ? <eos> | TimeVariantUnknownFinal | ai2 |


## Sum (20 samples)
### Top-1 (2 samples using it): (161, 76, 218, 263, 257, 76, 218, 263, 257, 76, 218, 43, 206, 102, 98, 93, 138, 107, 31)
| 161 | 76 | 218 | 263 | 257 | 76 | 218 | 263 | 257 | 76 | 218 | 43 | 206 | 102 | 98 | 93 | 138 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> blue | balloons | , <PER_2> | has | <num> blue | balloons | , and <PER_3> | has | <num> blue | balloons | . How many | blue | balloons | do they | have | in total | ? <eos> | Sum | ai2 |

### Top-2 (2 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 154, 76, 218, 4, 221, 89, 41, 153, 7, 63, 83, 107, 31)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 154 | 76 | 218 | 4 | 221 | 89 | 41 | 153 | 7 | 63 | 83 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | onions | , <PER_2> | grew <num> | onions | , and <PER_3> | grew <num> | onions | . They | worked | for <num> | days | on the | farm | . How many | onions | did | they | grow | in total | ? <eos> | Sum | ai2 |

### Top-3 (1 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 41, 153, 83, 54, 251)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 41 | 153 | 83 | 54 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | books | , <PER_2> | has <num> | books | , and <PER_3> | has <num> | books | . How many | books | do | they have together | ? <eos> | Sum | ai2 |

### Top-4 (1 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 41, 153, 148, 42, 217, 112)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 41 | 153 | 148 | 42 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | onions | , <PER_2> | grew <num> | onions | , and <PER_3> | grew <num> | onions | . How many | onions | did they | grow | in all | ? <eos> | Sum | ai2 |

### Top-5 (1 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 166, 98, 41, 153, 148, 42, 86)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 166 | 98 | 41 | 153 | 148 | 42 | 86 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found <num> | seashells | , <PER_2> | found <num> | seashells | , and <PER_3> | found <num> | seashells | on the | beach | . How many | seashells | did they | find together | ? <eos> | Sum | ai2 |

### Top-6 (1 samples using it): (161, 7, 98, 202, 7, 98, 202, 7, 98, 166, 48, 158, 41, 153, 193, 186, 107, 31)
| 161 | 7 | 98 | 202 | 7 | 98 | 202 | 7 | 98 | 166 | 48 | 158 | 41 | 153 | 193 | 186 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | plums | , <PER_2> | picked <num> | plums | , and <PER_3> | picked <num> | plums | from the | <unk> | tree | . How many | plums | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-7 (1 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 274, 158, 41, 153, 193, 186, 107, 31)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 274 | 158 | 41 | 153 | 193 | 186 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | pears | , <PER_2> | picked <num> | pears | , and <PER_3> | picked <num> | pears | from the pear | tree | . How many | pears | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-8 (1 samples using it): (161, 7, 98, 257, 7, 98, 257, 7, 98, 183, 98, 274, 34, 151, 177, 9, 186, 107, 31)
| 161 | 7 | 98 | 257 | 7 | 98 | 257 | 7 | 98 | 183 | 98 | 274 | 34 | 151 | 177 | 9 | 186 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | limes | , <PER_2> | picked <num> | limes | , and <PER_3> | picked <num> | limes | and <num> | pears | , at the | farm | . How many | limes | were | picked | in total | ? <eos> | Sum | ai2 |

### Top-9 (1 samples using it): (161, 98, 122, 172, 38, 192, 128, 203, 67, 128, 203, 43, 206, 109, 243, 38, 107, 31)
| 161 | 98 | 122 | 172 | 38 | 192 | 128 | 203 | 67 | 128 | 203 | 43 | 206 | 109 | 243 | 38 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | construction | company | <unk> <num> | ton of | <unk> | , <num> | ton of | <unk> | , and <num> | ton of | <unk> | . How many | tons of material | did the | company <unk> | in all | ? <eos> | Sum | ai2 |

### Top-10 (1 samples using it): (161, 7, 98, 274, 178, 7, 98, 102, 98, 61, 237, 218, 10, 128, 203, 260, 261, 98, 240, 125, 42, 216, 26, 31)
| 161 | 7 | 98 | 274 | 178 | 7 | 98 | 102 | 98 | 61 | 237 | 218 | 10 | 128 | 203 | 260 | 261 | 98 | 240 | 125 | 42 | 216 | 26 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | made trail | mix | for a <unk> trip | . She | used <num> | pound | of | peanuts | , <num> | pound | of chocolate | <unk> | , and <num> | pound of | raisins | . How many | pounds | of trail | mix | did | <PER_1> | make | ? <eos> | Sum | ai2 |


# Dataset - top templates
## ilds (449 samples)
### Top-1 (5 samples using it): (161, 7, 98, 154, 76, 218, 261, 98, 94, 161, 125, 196)
| 161 | 7 | 98 | 154 | 76 | 218 | 261 | 98 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | cards | . <PER_2> | takes | <num> away | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |

### Top-2 (5 samples using it): (161, 7, 98, 274, 38, 42, 219, 261, 98, 94, 161, 76, 2)
| 161 | 7 | 98 | 274 | 38 | 42 | 219 | 261 | 98 | 94 | 161 | 76 | 2 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | collects <num> | blocks | . <PER_1> 's | father | gives | <PER_1> <num> more | . How many | blocks | does | <PER_1> | have | ? <eos> | Addition | ilds |

### Top-3 (5 samples using it): (161, 7, 98, 215, 68, 76, 218, 261, 98, 177, 9, 161, 225, 217, 112)
| 161 | 7 | 98 | 215 | 68 | 76 | 218 | 261 | 98 | 177 | 9 | 161 | 225 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bottle | caps | . He | buys | <num> more | . How many | bottle | caps | does | <PER_1> | have | in all | ? <eos> | Addition | ilds |

### Top-4 (4 samples using it): (161, 7, 98, 61, 263, 20, 257, 94, 161, 125, 196)
| 161 | 7 | 98 | 61 | 263 | 20 | 257 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| If <PER_1> | strolled <num> | miles | at <num> | miles | per hour | , how long | was | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |

### Top-5 (4 samples using it): (161, 76, 218, 177, 178, 117, 171, 261, 98, 94, 161, 98, 118, 251)
| 161 | 76 | 218 | 177 | 178 | 117 | 171 | 261 | 98 | 94 | 161 | 98 | 118 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | starts | with <num> | pencils | . He | gives <num> | to <PER_2> | . How many | pencils | does | <PER_1> | end | with | ? <eos> | Subtraction | ilds |

### Top-6 (4 samples using it): (161, 7, 98, 274, 81, 219, 10, 257, 98, 93, 144, 200, 196)
| 161 | 7 | 98 | 274 | 81 | 219 | 10 | 257 | 98 | 93 | 144 | 200 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | bananas | . If he | shares | them among <num> | friends | , how many | bananas | does each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-7 (4 samples using it): (161, 9, 121, 144, 211, 102, 98, 274, 38, 55, 202, 232, 250, 186, 107, 224, 251)
| 161 | 9 | 121 | 144 | 211 | 102 | 98 | 274 | 38 | 55 | 202 | 232 | 250 | 186 | 107 | 224 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | stored | in | boxes | . If there | are <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |

### Top-8 (4 samples using it): (161, 7, 98, 274, 177, 98, 274, 12, 21, 42, 61, 15, 37, 7, 98, 57)
| 161 | 7 | 98 | 274 | 177 | 98 | 274 | 12 | 21 | 42 | 61 | 15 | 37 | 7 | 98 | 57 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | bananas | in <PER_1> 's | banana | collection | . If the | bananas | are | organized | into <num> | groups | , how big | is each | group | ? <eos> | CommonDiv | ilds |

### Top-9 (4 samples using it): (161, 7, 98, 166, 98, 73, 232, 109, 177, 186, 207, 274, 232, 257, 93, 144, 200, 196)
| 161 | 7 | 98 | 166 | 98 | 73 | 232 | 109 | 177 | 186 | 207 | 274 | 232 | 257 | 93 | 144 | 200 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | students | in the | class | and <num> | tickets | . If the | tickets | are | divided | equally among the | students | , how many | does each | student | get | ? <eos> | CommonDiv | ilds |

### Top-10 (4 samples using it): (161, 125, 219, 77, 209, 4, 121, 144, 109, 180, 54, 150, 99, 186, 80, 153, 63, 83, 102, 13, 94, 161, 125, 196)
| 161 | 125 | 219 | 77 | 209 | 4 | 121 | 144 | 109 | 180 | 54 | 150 | 99 | 186 | 80 | 153 | 63 | 83 | 102 | 13 | 94 | 161 | 125 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | to <PER_2> 's | house | . It | is | <num> | miles | from <PER_1> 's | house | to <PER_2> 's | house | . It | took | <PER_1> <num> | hours | to | get | there | . How fast | did | <PER_1> | go | ? <eos> | CommonDiv | ilds |


## ai2 (316 samples)
### Top-1 (5 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 148, 42, 217, 112)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 148 | 42 | 217 | 112 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | carrots | . <PER_2> | grew <num> | carrots | . How many | carrots | did they | grow | in total | ? <eos> | Addition | ai2 |

### Top-2 (4 samples using it): (161, 7, 98, 264, 7, 98, 41, 153, 83, 54, 251)
| 161 | 7 | 98 | 264 | 7 | 98 | 41 | 153 | 83 | 54 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | books | . <PER_2> | has <num> | books | . How many | books | do | they have together | ? <eos> | Addition | ai2 |

### Top-3 (3 samples using it): (161, 7, 98, 61, 7, 98, 166, 48, 41, 153, 148, 42, 86)
| 161 | 7 | 98 | 61 | 7 | 98 | 166 | 48 | 41 | 153 | 148 | 42 | 86 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . How many | seashells | did they | find together | ? <eos> | Addition | ai2 |

### Top-4 (3 samples using it): (161, 7, 98, 183, 12, 209, 7, 98, 41, 153, 148, 42, 217, 222)
| 161 | 7 | 98 | 183 | 12 | 209 | 7 | 98 | 41 | 153 | 148 | 42 | 217 | 222 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew <num> | carrots | and <num> | watermelons | . <PER_2> | grew <num> | carrots | . How many | carrots | did they | grow | in all | ? <eos> | Addition | ai2 |

### Top-5 (3 samples using it): (161, 7, 98, 61, 7, 98, 264, 7, 98, 151, 22, 193, 186, 107, 31)
| 161 | 7 | 98 | 61 | 7 | 98 | 264 | 7 | 98 | 151 | 22 | 193 | 186 | 107 | 31 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | picked <num> | oranges | and <PER_2> | picked <num> | oranges | . <PER_3> | picked <num> | apples | . How many | oranges | were | picked | in all | ? <eos> | Addition | ai2 |

### Top-6 (3 samples using it): (161, 258, 177, 98, 99, 62, 109, 177, 98, 151, 177, 98, 194, 51, 258, 196)
| 161 | 258 | 177 | 98 | 99 | 62 | 109 | 177 | 98 | 151 | 177 | 98 | 194 | 51 | 258 | 196 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has <num> | baseball | cards | . <PER_2> | bought <num> | of <PER_1> <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have now | ? <eos> | Subtraction | ai2 |

### Top-7 (3 samples using it): (161, 7, 98, 166, 98, 264, 7, 98, 166, 98, 151, 177, 186, 80, 162, 251)
| 161 | 7 | 98 | 166 | 98 | 264 | 7 | 98 | 166 | 98 | 151 | 177 | 186 | 80 | 162 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are <num> | pencils | in the | drawer | . <PER_1> | placed <num> | pencils | in the | drawer | . How many | pencils | are | now there | in total | ? <eos> | Addition | ai2 |

### Top-8 (3 samples using it): (161, 7, 98, 61, 263, 221, 103, 13, 258, 166, 98, 61, 41, 153, 83, 54, 115, 251)
| 161 | 7 | 98 | 61 | 263 | 221 | 103 | 13 | 258 | 166 | 98 | 61 | 41 | 153 | 83 | 54 | 115 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found <num> | seashells | and <num> | <unk> | on the | beach | . She | gave <num> | of the | seashells | to <PER_2> | . How many | seashells | does | <PER_1> now | have | ? <eos> | Subtraction | ai2 |

### Top-9 (3 samples using it): (161, 223, 121, 144, 43, 18, 142, 255, 99, 62, 109, 177, 98, 151, 177, 98, 200, 106, 197, 74, 251)
| 161 | 223 | 121 | 144 | 43 | 18 | 142 | 255 | 99 | 62 | 109 | 177 | 98 | 151 | 177 | 98 | 200 | 106 | 197 | 74 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | had | <num> | baseball | cards | , and <num> | were | torn | . <PER_2> | bought <num> | of <PER_1> 's | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now | ? <eos> | Subtraction | ai2 |

### Top-10 (3 samples using it): (161, 223, 121, 144, 238, 7, 98, 166, 98, 274, 101, 212, 257, 76, 218, 105, 101, 261, 98, 225, 228, 62, 251)
| 161 | 223 | 121 | 144 | 238 | 7 | 98 | 166 | 98 | 274 | 101 | 212 | 257 | 76 | 218 | 105 | 101 | 261 | 98 | 225 | 228 | 62 | 251 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | seashells | and <PER_2> | found <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find together | ? <eos> | Addition | ai2 |


