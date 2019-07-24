Namespace(A_dim=64, K=55, Kmul=1, L=4, align=False, ar_after_decay=False, beamsz=5, best_loss=None, bsz=16, clip=5, cond_A_dim=32, constr_tr_epochs=100, cuda=True, data='/home/shangling/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/', dropout=0.3, emb_drop=True, emb_size=100, epochs=40, fine_tune=False, gen_from_fi='/home/shangling/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated/src_valid.txt', gen_on_valid=False, gen_wts='1,1', hid_size=100, initrange=0.1, interactive=False, label_train=False, layers=1, load='models/chsmm-ai2-cmds-100–55-5-far-NER.pt.0', log_interval=100, lr=0.5, lr_decay=0.5, lse_obj=False, max_mbs_per_epoch=35000, max_pool=True, max_seqlen=70, min_gen_states=0, min_gen_tokes=0, mlp_sz_mult=2, mlpinp=True, no_ar_epochs=100, no_ar_for_vit=False, ntemplates=100, one_rnn=True, onmt_decay=True, optim='sgd', prev_loss=None, save='', seed=1111, sep_attn=True, smaller_cond_dim=64, tagged_fi='segs/seg-ai2-cmds-100-55-5-far-NER.txt', test=False, thresh=3, unif_lenps=True, verbose=True, wid_workers='', word_ar=False, yes_self_trans=False)
using vocabulary of size: 731
568 gen word types
# gen_from_src():
using vocabulary of size: 731
568 gen word types
assuming we start on line 0 of train
# Top 5 templates consist of
## No frequencies
### Top-1
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . She gets <num> | to <PER_2> | . How many | cards | does <PER_1> end with | ? <eos> |
| There are <num> | marbles | . He buys <num> | away | . How many <MISC_1> | bananas | will <PER_1> have |   |
| <PER_1> starts with <num> | seashells | . <PER_2> takes <num> | another <num> |   | pencils | does <PER_1> have |   |
| <PER_1> had <num> | cards | and <PER_1> puts <num> | gives <PER_1> <num> more |   | bottle | does <PER_1> have now |   |
| <PER_1> picked <num> | boxes | . He gives <num> | from <PER_2> |   | blocks | does she have now |   |

### Top-2
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | at <num> | miles | per | hour | . How long | did <PER_1> | <unk> | ? <eos> |
| There are <num> | marbles | and brings <num> | kilometers | to | share | . How far | was <PER_1> <unk> | walk |   |
| <PER_1> starts with <num> | seashells |   | cookies |   |   | . How much farther | did <PER_1> go | stroll |   |
| <PER_1> had <num> | cards |   |   |   |   |   | was <PER_1> | jogging |   |
| <PER_1> picked <num> | boxes |   |   |   |   |   | is it | group |   |

### Top-3
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_1> placed <num> | seashells | . How many | seashells | were picked | in all | ? <eos> |
| There are <num> | marbles | and <PER_2> picked <num> | pencils |   | balloons | do they have | in total |   |
| <PER_1> starts with <num> | seashells | . <PER_2> weighs <num> | pounds |   | pears | did they grow | together |   |
| <PER_1> had <num> | cards | . <PER_2> has <num> | pears |   | books | did they find | are finished |   |
| <PER_1> picked <num> | boxes | and <PER_2> found <num> | miles |   | turnips | does <PER_1> have | get |   |

### Top-4
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | . <PER_1> 's | hours | to <PER_2> | . How many | cards | does <PER_1> end with | ? <eos> |
| There are <num> | marbles | . She loses <num> | boxes | away | . How many <MISC_1> | bananas | will <PER_1> have |   |
| <PER_1> starts with <num> | seashells | and <PER_2> picked <num> | balloons | another <num> |   | pencils | does <PER_1> have |   |
| <PER_1> had <num> | cards | . There are <num> | mile | gives <PER_1> <num> more |   | bottle | does <PER_1> have now |   |
| <PER_1> picked <num> | boxes | . <PER_3> picked <num> | father | from <PER_2> |   | blocks | does she have now |   |

### Top-5
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> | oranges | and <num> | cards | . <PER_1> 's | hours | . How many | seashells | were picked | in all | ? <eos> |
| There are <num> | marbles | and <num> tall | caps | . She loses <num> | boxes |   | balloons | do they have | in total |   |
| <PER_1> starts with <num> | seashells | <num> | crayons | and <PER_2> picked <num> | balloons |   | pears | did they grow | together |   |
| <PER_1> had <num> | cards | has <num> | trees | . There are <num> | mile |   | books | did they find | are finished |   |
| <PER_1> picked <num> | boxes | every <num> | ride | . <PER_3> picked <num> | father |   | turnips | does <PER_1> have | get |   |

## With frequencies
### Top-1
| 271 | 40 | 68 | 0 | 107 | 45 | 214 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> (0.25) | oranges (0.06) | . She gets <num> (0.14) | to <PER_2> (0.16) | . How many (0.99) | cards (0.08) | does <PER_1> end with (0.22) | ? <eos> (1.00) |
| There are <num> (0.16) | marbles (0.06) | . He buys <num> (0.10) | away (0.14) | . How many <MISC_1> (0.01) | bananas (0.07) | will <PER_1> have (0.13) |   |
| <PER_1> starts with <num> (0.09) | seashells (0.05) | . <PER_2> takes <num> (0.10) | another <num> (0.14) |   | pencils (0.06) | does <PER_1> have (0.11) |   |
| <PER_1> had <num> (0.07) | cards (0.05) | and <PER_1> puts <num> (0.09) | gives <PER_1> <num> more (0.12) |   | bottle (0.05) | does <PER_1> have now (0.10) |   |
| <PER_1> picked <num> (0.05) | boxes (0.05) | . He gives <num> (0.07) | from <PER_2> (0.12) |   | blocks (0.05) | does she have now (0.05) |   |

### Top-2
| 271 | 40 | 148 | 42 | 182 | 53 | 219 | 197 | 39 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> (0.25) | oranges (0.06) | at <num> (0.88) | miles (0.56) | per (0.88) | hour (0.88) | . How long (0.48) | did <PER_1> (0.24) | <unk> (0.22) | ? <eos> (1.00) |
| There are <num> (0.16) | marbles (0.06) | and brings <num> (0.12) | kilometers (0.31) | to (0.12) | share (0.12) | . How far (0.38) | was <PER_1> <unk> (0.18) | walk (0.17) |   |
| <PER_1> starts with <num> (0.09) | seashells (0.05) |   | cookies (0.12) |   |   | . How much farther (0.14) | did <PER_1> go (0.15) | stroll (0.17) |   |
| <PER_1> had <num> (0.07) | cards (0.05) |   |   |   |   |   | was <PER_1> (0.12) | jogging (0.17) |   |
| <PER_1> picked <num> (0.05) | boxes (0.05) |   |   |   |   |   | is it (0.09) | group (0.17) |   |

### Top-3
| 271 | 40 | 178 | 66 | 52 | 227 | 32 | 85 | 84 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> (0.25) | oranges (0.06) | . <PER_1> placed <num> (0.16) | seashells (0.10) | . How many (1.00) | seashells (0.16) | were picked (0.24) | in all (0.38) | ? <eos> (1.00) |
| There are <num> (0.16) | marbles (0.06) | and <PER_2> picked <num> (0.10) | pencils (0.09) |   | balloons (0.12) | do they have (0.24) | in total (0.25) |   |
| <PER_1> starts with <num> (0.09) | seashells (0.05) | . <PER_2> weighs <num> (0.07) | pounds (0.07) |   | pears (0.09) | did they grow (0.24) | together (0.12) |   |
| <PER_1> had <num> (0.07) | cards (0.05) | . <PER_2> has <num> (0.07) | pears (0.07) |   | books (0.07) | did they find (0.12) | are finished (0.05) |   |
| <PER_1> picked <num> (0.05) | boxes (0.05) | and <PER_2> found <num> (0.06) | miles (0.06) |   | turnips (0.05) | does <PER_1> have (0.03) | get (0.04) |   |

### Top-4
| 271 | 40 | 13 | 196 | 0 | 107 | 45 | 214 | 139 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> (0.25) | oranges (0.06) | . <PER_1> 's (0.11) | hours (0.07) | to <PER_2> (0.16) | . How many (0.99) | cards (0.08) | does <PER_1> end with (0.22) | ? <eos> (1.00) |
| There are <num> (0.16) | marbles (0.06) | . She loses <num> (0.09) | boxes (0.07) | away (0.14) | . How many <MISC_1> (0.01) | bananas (0.07) | will <PER_1> have (0.13) |   |
| <PER_1> starts with <num> (0.09) | seashells (0.05) | and <PER_2> picked <num> (0.07) | balloons (0.06) | another <num> (0.14) |   | pencils (0.06) | does <PER_1> have (0.11) |   |
| <PER_1> had <num> (0.07) | cards (0.05) | . There are <num> (0.07) | mile (0.05) | gives <PER_1> <num> more (0.12) |   | bottle (0.05) | does <PER_1> have now (0.10) |   |
| <PER_1> picked <num> (0.05) | boxes (0.05) | . <PER_3> picked <num> (0.07) | father (0.05) | from <PER_2> (0.12) |   | blocks (0.05) | does she have now (0.05) |   |

### Top-5
| 271 | 40 | 93 | 180 | 13 | 196 | 52 | 227 | 32 | 85 | 84 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| <PER_1> has <num> (0.25) | oranges (0.06) | and <num> (0.69) | cards (0.11) | . <PER_1> 's (0.11) | hours (0.07) | . How many (1.00) | seashells (0.16) | were picked (0.24) | in all (0.38) | ? <eos> (1.00) |
| There are <num> (0.16) | marbles (0.06) | and <num> tall (0.08) | caps (0.11) | . She loses <num> (0.09) | boxes (0.07) |   | balloons (0.12) | do they have (0.24) | in total (0.25) |   |
| <PER_1> starts with <num> (0.09) | seashells (0.05) | <num> (0.08) | crayons (0.05) | and <PER_2> picked <num> (0.07) | balloons (0.06) |   | pears (0.09) | did they grow (0.24) | together (0.12) |   |
| <PER_1> had <num> (0.07) | cards (0.05) | has <num> (0.06) | trees (0.04) | . There are <num> (0.07) | mile (0.05) |   | books (0.07) | did they find (0.12) | are finished (0.05) |   |
| <PER_1> picked <num> (0.05) | boxes (0.05) | every <num> (0.03) | ride (0.04) | . <PER_3> picked <num> (0.07) | father (0.05) |   | turnips (0.05) | does <PER_1> have (0.03) | get (0.04) |   |

__start_noun0__ seashells __end_noun0__ __start_noun1__ starfish __end_noun1__ __start_noun2__ beach __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> seashells (c) in the beach (c) . <PER_2> has <num> seashells (c) in the beach (c) . How many seashells (c) are in the beach (c) ? <eos>|||<PER_1> has <num>|271 seashells (c)|40 in the|186 beach (c)|132 . <PER_2> has <num>|178 seashells (c)|66 in the|21 beach (c)|22 . How many|107 seashells (c)|45 are in the|3 beach (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.26

__start_noun0__ seashells __end_noun0__ __start_noun1__ starfish __end_noun1__ __start_noun2__ beach __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> seashells (c) in the beach (c) . <PER_2> has <num> seashells (c) in the beach (c) . How many seashells (c) are in the beach (c) ? <eos>|||<PER_1> has <num>|271 seashells (c)|40 in the|186 beach (c)|132 . <PER_2> has <num>|178 seashells (c)|66 in the|21 beach (c)|22 . How many|107 seashells (c)|45 are in the|3 beach (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.26

__start_noun0__ basketball __end_noun0__ __start_noun1__ game __end_noun1__ __start_noun2__ video __end_noun2__ __start_noun3__ games __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> basketball (c) in the video (c) . <PER_2> has <num> games (c) in the video (c) . How many games (c) are in the games (c) ? <eos>|||<PER_1> has <num>|271 basketball (c)|40 in the|186 video (c)|132 . <PER_2> has <num>|178 games (c)|66 in the|21 video (c)|22 . How many|107 games (c)|45 are in the|3 games (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.34

__start_noun0__ grant __end_noun0__ __start_noun1__ books __end_noun1__ __start_noun2__ library __end_noun2__ __start_noun3__ total __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> grant (c) in the library (c) . <PER_2> has <num> books (c) in the library (c) . How many books (c) are in the library (c) ? <eos>|||<PER_1> has <num>|271 grant (c)|40 in the|186 library (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 library (c)|22 . How many|107 books (c)|45 are in the|3 library (c)|75 ? <eos>|139
a=-0.90 t=-0.62 g=-0.29

__start_noun0__ dimes __end_noun0__ __start_noun1__ bank __end_noun1__ __start_noun2__ dad __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> dimes (c) in the bank (c) . <PER_2> has <num> dimes (c) in the bank (c) . How many dimes (c) are in the dad (c) ? <eos>|||<PER_1> has <num>|271 dimes (c)|40 in the|186 bank (c)|132 . <PER_2> has <num>|178 dimes (c)|66 in the|21 bank (c)|22 . How many|107 dimes (c)|45 are in the|3 dad (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ school __end_noun0__ __start_noun1__ janitor __end_noun1__ __start_noun2__ week __end_noun2__ __start_noun3__ total __end_noun3__ __start_noun4__ pieces __end_noun4__ __start_noun5__ trash __end_noun5__ __start_noun6__ classrooms __end_noun6__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> school (c) in the week (c) . <PER_2> has <num> pieces (c) in the week (c) . How many pieces (c) are in the classrooms (c) ? <eos>|||<PER_1> has <num>|271 school (c)|40 in the|186 week (c)|132 . <PER_2> has <num>|178 pieces (c)|66 in the|21 week (c)|22 . How many|107 pieces (c)|45 are in the|3 classrooms (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ inches __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> inches (c) in the inches (c) . <PER_2> has <num> inches (c) in the inches (c) . How many inches (c) are in the inches (c) ? <eos>|||<PER_1> has <num>|271 inches (c)|40 in the|186 inches (c)|132 . <PER_2> has <num>|178 inches (c)|66 in the|21 inches (c)|22 . How many|107 inches (c)|45 are in the|3 inches (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.24

__start_noun0__ trees __end_noun0__ __start_noun1__ park __end_noun1__ __start_noun2__ workers __end_noun2__ __start_noun3__ plant __end_noun3__ __start_noun4__ walnut __end_noun4__ __start_noun5__ today __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> walnut (c) in the park (c) . <PER_2> has <num> trees (c) in the park (c) . How many walnut (c) are in the today (c) ? <eos>|||<PER_1> has <num>|271 walnut (c)|40 in the|186 park (c)|132 . <PER_2> has <num>|178 trees (c)|66 in the|21 park (c)|22 . How many|107 walnut (c)|45 are in the|3 today (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.32

__start_noun0__ week __end_noun0__ __start_noun1__ dollars __end_noun1__ __start_noun2__ cars __end_noun2__ __start_noun3__ weekend __end_noun3__ __start_noun4__ money __end_noun4__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> week (c) in the cars (c) . <PER_2> has <num> dollars (c) in the cars (c) . How many money (c) are in the cars (c) ? <eos>|||<PER_1> has <num>|271 week (c)|40 in the|186 cars (c)|132 . <PER_2> has <num>|178 dollars (c)|66 in the|21 cars (c)|22 . How many|107 money (c)|45 are in the|3 cars (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.33

__start_noun0__ total __end_noun0__ __start_noun1__ tickets __end_noun1__ __start_noun2__ season __end_noun2__ __start_noun3__ half __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> total (c) in the season (c) . <PER_2> has <num> tickets (c) in the season (c) . How many tickets (c) are in the tickets (c) ? <eos>|||<PER_1> has <num>|271 total (c)|40 in the|186 season (c)|132 . <PER_2> has <num>|178 tickets (c)|66 in the|21 season (c)|22 . How many|107 tickets (c)|45 are in the|3 tickets (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.34

__start_noun0__ pizza __end_noun0__ __start_noun1__ party __end_noun1__ __start_noun2__ friends __end_noun2__ __start_noun3__ bottles __end_noun3__ __start_noun4__ soda __end_noun4__ __start_noun5__ cola __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> pizza (c) in the party (c) . <PER_2> has <num> pizza (c) in the party (c) . How many pizza (c) are in the cola (c) ? <eos>|||<PER_1> has <num>|271 pizza (c)|40 in the|186 party (c)|132 . <PER_2> has <num>|178 pizza (c)|66 in the|21 party (c)|22 . How many|107 pizza (c)|45 are in the|3 cola (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ customers __end_noun0__ __start_noun1__ muffs __end_noun1__ __start_noun2__ mall __end_noun2__ __start_noun3__ none __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> customers (c) in the muffs (c) . <PER_2> has <num> mall (c) in the muffs (c) . How many none (c) are in the mall (c) ? <eos>|||<PER_1> has <num>|271 customers (c)|40 in the|186 muffs (c)|132 . <PER_2> has <num>|178 mall (c)|66 in the|21 muffs (c)|22 . How many|107 none (c)|45 are in the|3 mall (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ year __end_noun0__ __start_noun1__ people __end_noun1__ __start_noun2__ country __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> year (c) in the country (c) . <PER_2> has <num> people (c) in the country (c) . How many people (c) are in the country (c) ? <eos>|||<PER_1> has <num>|271 year (c)|40 in the|186 country (c)|132 . <PER_2> has <num>|178 people (c)|66 in the|21 country (c)|22 . How many|107 people (c)|45 are in the|3 country (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ pencils __end_noun0__ __start_noun1__ drawer __end_noun1__ __start_noun2__ total __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> pencils (c) in the drawer (c) . <PER_2> has <num> pencils (c) in the drawer (c) . How many pencils (c) are in the total (c) ? <eos>|||<PER_1> has <num>|271 pencils (c)|40 in the|186 drawer (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 drawer (c)|22 . How many|107 pencils (c)|45 are in the|3 total (c)|75 ? <eos>|139
a=-0.87 t=-0.61 g=-0.26

__start_noun0__ cards __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> cards (c) in the cards (c) . <PER_2> has <num> cards (c) in the cards (c) . How many cards (c) are the cards (c) ? <eos>|||<PER_1> has <num>|271 cards (c)|40 in the|186 cards (c)|132 . <PER_2> has <num>|178 cards (c)|66 in the|21 cards (c)|22 . How many|107 cards (c)|45 are the|3 cards (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.23

__start_noun0__ restaurant __end_noun0__ __start_noun1__ cakes __end_noun1__ __start_noun2__ lunch __end_noun2__ __start_noun3__ dinner __end_noun3__ __start_noun4__ today __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> restaurant (c) in the lunch (c) . <PER_2> has <num> cakes (c) in the lunch (c) . How many cakes (c) are in the today (c) ? <eos>|||<PER_1> has <num>|271 restaurant (c)|40 in the|186 lunch (c)|132 . <PER_2> has <num>|178 cakes (c)|66 in the|21 lunch (c)|22 . How many|107 cakes (c)|45 are in the|3 today (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ corporation __end_noun0__ __start_noun1__ employees __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> corporation (c) in the employees (c) . <PER_2> has <num> corporation (c) in the employees (c) . How many corporation (c) are in the employees (c) ? <eos>|||<PER_1> has <num>|271 corporation (c)|40 in the|186 employees (c)|132 . <PER_2> has <num>|178 corporation (c)|66 in the|21 employees (c)|22 . How many|107 corporation (c)|45 are in the|3 employees (c)|75 ? <eos>|139
a=-0.88 t=-0.62 g=-0.27

__start_noun0__ peaches __end_noun0__ __start_noun1__ roadside __end_noun1__ __start_noun2__ fruit __end_noun2__ __start_noun3__ dish __end_noun3__ __start_noun4__ orchard __end_noun4__ __start_noun5__ stock __end_noun5__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> peaches (c) in the fruit (c) . <PER_2> has <num> peaches (c) in the fruit (c) . How many stock (c) are in the stock (c) ? <eos>|||<PER_1> has <num>|271 peaches (c)|40 in the|186 fruit (c)|132 . <PER_2> has <num>|178 peaches (c)|66 in the|21 fruit (c)|22 . How many|107 stock (c)|45 are in the|3 stock (c)|75 ? <eos>|139
a=-0.99 t=-0.62 g=-0.38

__start_noun0__ classmates __end_noun0__ __start_noun1__ blocks __end_noun1__ __start_noun2__ scale __end_noun2__ __start_noun3__ science __end_noun3__ __start_noun4__ lab __end_noun4__ __start_noun5__ block __end_noun5__ __start_noun6__ pounds __end_noun6__ __start_noun7__ yellow __end_noun7__ __start_noun8__ weigh __end_noun8__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> classmates (c) in the scale (c) . <PER_2> has <num> pounds (c) in the scale (c) . How many pounds (c) are in the yellow (c) ? <eos>|||<PER_1> has <num>|271 classmates (c)|40 in the|186 scale (c)|132 . <PER_2> has <num>|178 pounds (c)|66 in the|21 scale (c)|22 . How many|107 pounds (c)|45 are in the|3 yellow (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ dogwood __end_noun0__ __start_noun1__ trees __end_noun1__ __start_noun2__ park __end_noun2__ __start_noun3__ workers __end_noun3__ __start_noun4__ plant __end_noun4__ __start_noun5__ today __end_noun5__ __start_noun6__ tomorrow __end_noun6__ __start_solution_type__ TimeVariantUnknownFinal __end_solution_type__

<PER_1> has <num> dogwood (c) in the park (c) . <PER_2> has <num> trees (c) in the park (c) . How many tomorrow (c) are in the today (c) ? <eos>|||<PER_1> has <num>|271 dogwood (c)|40 in the|186 park (c)|132 . <PER_2> has <num>|178 trees (c)|66 in the|21 park (c)|22 . How many|107 tomorrow (c)|45 are in the|3 today (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.35

__start_noun0__ pennies __end_noun0__ __start_noun1__ nickels __end_noun1__ __start_noun2__ bank __end_noun2__ __start_noun3__ dad __end_noun3__ __start_noun4__ mother __end_noun4__ __start_solution_type__ TimeVariantUnknownFinal __end_solution_type__

<PER_1> has <num> pennies (c) in the bank (c) . <PER_2> has <num> nickels (c) in the bank (c) . How many nickels (c) are in the nickels (c) ? <eos>|||<PER_1> has <num>|271 pennies (c)|40 in the|186 bank (c)|132 . <PER_2> has <num>|178 nickels (c)|66 in the|21 bank (c)|22 . How many|107 nickels (c)|45 are in the|3 nickels (c)|75 ? <eos>|139
a=-0.91 t=-0.62 g=-0.30

__start_noun0__ chemistry __end_noun0__ __start_noun1__ pounds __end_noun1__ __start_noun2__ geometry __end_noun2__ __start_noun3__ textbook __end_noun3__ __start_noun4__ pound __end_noun4__ __start_noun5__ weigh __end_noun5__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> chemistry (c) in the geometry (c) . <PER_2> has <num> pounds (c) in the geometry (c) . How many pounds (c) are in the pound (c) ? <eos>|||<PER_1> has <num>|271 chemistry (c)|40 in the|186 geometry (c)|132 . <PER_2> has <num>|178 pounds (c)|66 in the|21 geometry (c)|22 . How many|107 pounds (c)|45 are in the|3 pound (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ orange __end_noun0__ __start_noun1__ caterpillar __end_noun1__ __start_noun2__ backyard __end_noun2__ __start_noun3__ inches __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> orange (c) in the backyard (c) . <PER_2> has <num> inches (c) in the backyard (c) . How many orange (c) are in the backyard (c) ? <eos>|||<PER_1> has <num>|271 orange (c)|40 in the|186 backyard (c)|132 . <PER_2> has <num>|178 inches (c)|66 in the|21 backyard (c)|22 . How many|107 orange (c)|45 are in the|3 backyard (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.33

__start_noun0__ chef __end_noun0__ __start_noun1__ kilograms __end_noun1__ __start_noun2__ almonds __end_noun2__ __start_noun3__ pecans __end_noun3__ __start_noun4__ nuts __end_noun4__ __start_noun5__ buy __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> chef (c) in the almonds (c) . <PER_2> has <num> nuts (c) in the almonds (c) . How many buy (c) are in the nuts (c) ? <eos>|||<PER_1> has <num>|271 chef (c)|40 in the|186 almonds (c)|132 . <PER_2> has <num>|178 nuts (c)|66 in the|21 almonds (c)|22 . How many|107 buy (c)|45 are in the|3 nuts (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.39

__start_noun0__ pencils __end_noun0__ __start_noun1__ crayons __end_noun1__ __start_noun2__ drawer __end_noun2__ __start_noun3__ total __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> pencils (c) in the drawer (c) . <PER_2> has <num> pencils (c) in the drawer (c) . How many pencils (c) are in the drawer (c) ? <eos>|||<PER_1> has <num>|271 pencils (c)|40 in the|186 drawer (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 drawer (c)|22 . How many|107 pencils (c)|45 are in the|3 drawer (c)|75 ? <eos>|139
a=-0.90 t=-0.62 g=-0.29

__start_noun0__ school __end_noun0__ __start_noun1__ basketball __end_noun1__ __start_noun2__ games __end_noun2__ __start_noun3__ year __end_noun3__ __start_noun4__ team __end_noun4__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> school (c) in the year (c) . <PER_2> has <num> games (c) in the year (c) . How many school (c) are in the games (c) ? <eos>|||<PER_1> has <num>|271 school (c)|40 in the|186 year (c)|132 . <PER_2> has <num>|178 games (c)|66 in the|21 year (c)|22 . How many|107 school (c)|45 are in the|3 games (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ seashells __end_noun0__ __start_noun1__ beach __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> seashells (c) in the beach (c) . <PER_2> has <num> seashells (c) in the beach (c) . How many seashells (c) are in the beach (c) ? <eos>|||<PER_1> has <num>|271 seashells (c)|40 in the|186 beach (c)|132 . <PER_2> has <num>|178 seashells (c)|66 in the|21 beach (c)|22 . How many|107 seashells (c)|45 are in the|3 beach (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.24

__start_noun0__ turnips __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> turnips (c) in the turnips (c) . <PER_2> has <num> turnips (c) in the turnips (c) . How many turnips (c) are in the turnips (c) ? <eos>|||<PER_1> has <num>|271 turnips (c)|40 in the|186 turnips (c)|132 . <PER_2> has <num>|178 turnips (c)|66 in the|21 turnips (c)|22 . How many|107 turnips (c)|45 are in the|3 turnips (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ cup __end_noun0__ __start_noun1__ raisins __end_noun1__ __start_noun2__ batch __end_noun2__ __start_noun3__ mix __end_noun3__ __start_noun4__ cups __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> cup (c) in the batch (c) . <PER_2> has <num> cups (c) in the batch (c) . How many cups (c) are in the cups (c) ? <eos>|||<PER_1> has <num>|271 cup (c)|40 in the|186 batch (c)|132 . <PER_2> has <num>|178 cups (c)|66 in the|21 batch (c)|22 . How many|107 cups (c)|45 are in the|3 cups (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.35

__start_noun0__ watermelons __end_noun0__ __start_noun1__ turnips __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> watermelons (c) in the turnips (c) . <PER_2> has <num> watermelons (c) in the turnips (c) . How many watermelons (c) are in the turnips (c) ? <eos>|||<PER_1> has <num>|271 watermelons (c)|40 in the|186 turnips (c)|132 . <PER_2> has <num>|178 watermelons (c)|66 in the|21 turnips (c)|22 . How many|107 watermelons (c)|45 are in the|3 turnips (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.25

__start_noun0__ treasure __end_noun0__ __start_noun1__ hunter __end_noun1__ __start_noun2__ chest __end_noun2__ __start_noun3__ total __end_noun3__ __start_noun4__ gems __end_noun4__ __start_noun5__ diamonds __end_noun5__ __start_noun6__ rest __end_noun6__ __start_noun7__ rubies __end_noun7__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> treasure (c) in the chest (c) . <PER_2> has <num> total (c) in the chest (c) . How many rest (c) are in the rubies (c) ? <eos>|||<PER_1> has <num>|271 treasure (c)|40 in the|186 chest (c)|132 . <PER_2> has <num>|178 total (c)|66 in the|21 chest (c)|22 . How many|107 rest (c)|45 are in the|3 rubies (c)|75 ? <eos>|139
a=-1.02 t=-0.62 g=-0.40

__start_noun0__ crayons __end_noun0__ __start_noun1__ pencils __end_noun1__ __start_noun2__ drawer __end_noun2__ __start_noun3__ total __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> crayons (c) in the drawer (c) . <PER_2> has <num> crayons (c) in the drawer (c) . How many pencils (c) are in the drawer (c) ? <eos>|||<PER_1> has <num>|271 crayons (c)|40 in the|186 drawer (c)|132 . <PER_2> has <num>|178 crayons (c)|66 in the|21 drawer (c)|22 . How many|107 pencils (c)|45 are in the|3 drawer (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.30

__start_noun0__ cat __end_noun0__ __start_noun1__ toy __end_noun1__ __start_noun2__ cage __end_noun2__ __start_noun3__ cost __end_noun3__ __start_noun4__ purchases __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> cat (c) in the cage (c) . <PER_2> has <num> cost (c) in the cage (c) . How many cost (c) are in the purchases (c) ? <eos>|||<PER_1> has <num>|271 cat (c)|40 in the|186 cage (c)|132 . <PER_2> has <num>|178 cost (c)|66 in the|21 cage (c)|22 . How many|107 cost (c)|45 are in the|3 purchases (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ seashells __end_noun0__ __start_noun1__ beach __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> seashells (c) in the beach (c) . <PER_2> has <num> seashells (c) in the beach (c) . How many seashells (c) are in the beach (c) ? <eos>|||<PER_1> has <num>|271 seashells (c)|40 in the|186 beach (c)|132 . <PER_2> has <num>|178 seashells (c)|66 in the|21 beach (c)|22 . How many|107 seashells (c)|45 are in the|3 beach (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.24

__start_noun0__ vacation __end_noun0__ __start_noun1__ summer __end_noun1__ __start_noun2__ souvenirs __end_noun2__ __start_noun3__ mile __end_noun3__ __start_noun4__ hotel __end_noun4__ __start_noun5__ postcard __end_noun5__ __start_noun6__ shop __end_noun6__ __start_noun7__ miles __end_noun7__ __start_noun8__ walk __end_noun8__ __start_solution_type__ TimeVariantUnknownFinal __end_solution_type__

<PER_1> has <num> vacation (c) in the souvenirs (c) . <PER_2> has <num> mile (c) in the souvenirs (c) . How many miles (c) are in the walk (c) ? <eos>|||<PER_1> has <num>|271 vacation (c)|40 in the|186 souvenirs (c)|132 . <PER_2> has <num>|178 mile (c)|66 in the|21 souvenirs (c)|22 . How many|107 miles (c)|45 are in the|3 walk (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ trees __end_noun0__ __start_noun1__ park __end_noun1__ __start_noun2__ workers __end_noun2__ __start_noun3__ plant __end_noun3__ __start_noun4__ walnut __end_noun4__ __start_noun5__ today __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> walnut (c) in the park (c) . <PER_2> has <num> trees (c) in the park (c) . How many walnut (c) are in the today (c) ? <eos>|||<PER_1> has <num>|271 walnut (c)|40 in the|186 park (c)|132 . <PER_2> has <num>|178 trees (c)|66 in the|21 park (c)|22 . How many|107 walnut (c)|45 are in the|3 today (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.32

__start_noun0__ truck __end_noun0__ __start_noun1__ pounds __end_noun1__ __start_noun2__ sand __end_noun2__ __start_noun3__ travels __end_noun3__ __start_noun4__ construction __end_noun4__ __start_noun5__ yard __end_noun5__ __start_noun6__ way __end_noun6__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> truck (c) in the sand (c) . <PER_2> has <num> pounds (c) in the sand (c) . How many pounds (c) are in the way (c) ? <eos>|||<PER_1> has <num>|271 truck (c)|40 in the|186 sand (c)|132 . <PER_2> has <num>|178 pounds (c)|66 in the|21 sand (c)|22 . How many|107 pounds (c)|45 are in the|3 way (c)|75 ? <eos>|139
a=-0.99 t=-0.62 g=-0.38

__start_noun0__ balloons __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> balloons (c) in the balloons (c) . <PER_2> has <num> balloons (c) in the balloons (c) . How many balloons (c) are in the balloons (c) ? <eos>|||<PER_1> has <num>|271 balloons (c)|40 in the|186 balloons (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 balloons (c)|22 . How many|107 balloons (c)|45 are in the|3 balloons (c)|75 ? <eos>|139
a=-0.90 t=-0.67 g=-0.23

__start_noun0__ pencils __end_noun0__ __start_noun1__ rulers __end_noun1__ __start_noun2__ drawer __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> pencils (c) in the drawer (c) . <PER_2> has <num> pencils (c) in the drawer (c) . How many pencils (c) are in the drawer (c) ? <eos>|||<PER_1> has <num>|271 pencils (c)|40 in the|186 drawer (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 drawer (c)|22 . How many|107 pencils (c)|45 are in the|3 drawer (c)|75 ? <eos>|139
a=-0.87 t=-0.61 g=-0.26

__start_noun0__ seashells __end_noun0__ __start_noun1__ beach __end_noun1__ __start_noun2__ seashell __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> seashells (c) in the beach (c) . <PER_2> has <num> seashells (c) in the beach (c) . How many seashells (c) are in the seashell (c) ? <eos>|||<PER_1> has <num>|271 seashells (c)|40 in the|186 beach (c)|132 . <PER_2> has <num>|178 seashells (c)|66 in the|21 beach (c)|22 . How many|107 seashells (c)|45 are in the|3 seashell (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ basketball __end_noun0__ __start_noun1__ games __end_noun1__ __start_noun2__ year __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> basketball (c) in the year (c) . <PER_2> has <num> games (c) in the year (c) . How many basketball (c) are in the year (c) ? <eos>|||<PER_1> has <num>|271 basketball (c)|40 in the|186 year (c)|132 . <PER_2> has <num>|178 games (c)|66 in the|21 year (c)|22 . How many|107 basketball (c)|45 are in the|3 year (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ dimes __end_noun0__ __start_noun1__ bank __end_noun1__ __start_noun2__ dad __end_noun2__ __start_noun3__ mother __end_noun3__ __start_solution_type__ TimeVariantUnknownFinal __end_solution_type__

<PER_1> has <num> dimes (c) in the bank (c) . <PER_2> has <num> dimes (c) in the bank (c) . How many dimes (c) are in the dad (c) ? <eos>|||<PER_1> has <num>|271 dimes (c)|40 in the|186 bank (c)|132 . <PER_2> has <num>|178 dimes (c)|66 in the|21 bank (c)|22 . How many|107 dimes (c)|45 are in the|3 dad (c)|75 ? <eos>|139
a=-0.90 t=-0.62 g=-0.28

__start_noun0__ fruit __end_noun0__ __start_noun1__ salad __end_noun1__ __start_noun2__ pound __end_noun2__ __start_noun3__ melon __end_noun3__ __start_noun4__ berries __end_noun4__ __start_noun5__ pounds __end_noun5__ __start_noun6__ use __end_noun6__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> fruit (c) in the pound (c) . <PER_2> has <num> pounds (c) in the pound (c) . How many pounds (c) are in the use (c) ? <eos>|||<PER_1> has <num>|271 fruit (c)|40 in the|186 pound (c)|132 . <PER_2> has <num>|178 pounds (c)|66 in the|21 pound (c)|22 . How many|107 pounds (c)|45 are in the|3 use (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ salon __end_noun0__ __start_noun1__ inch __end_noun1__ __start_noun2__ hair __end_noun2__ __start_noun3__ day __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> salon (c) in the hair (c) . <PER_2> has <num> inch (c) in the hair (c) . How many hair (c) are in the hair (c) ? <eos>|||<PER_1> has <num>|271 salon (c)|40 in the|186 hair (c)|132 . <PER_2> has <num>|178 inch (c)|66 in the|21 hair (c)|22 . How many|107 hair (c)|45 are in the|3 hair (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.34

__start_noun0__ biologist __end_noun0__ __start_noun1__ fish __end_noun1__ __start_noun2__ foot __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> biologist (c) in the foot (c) . <PER_2> has <num> fish (c) in the foot (c) . How many fish (c) are in the fish (c) ? <eos>|||<PER_1> has <num>|271 biologist (c)|40 in the|186 foot (c)|132 . <PER_2> has <num>|178 fish (c)|66 in the|21 foot (c)|22 . How many|107 fish (c)|45 are in the|3 fish (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ cell __end_noun0__ __start_noun1__ phone __end_noun1__ __start_noun2__ company __end_noun2__ __start_noun3__ total __end_noun3__ __start_noun4__ customers __end_noun4__ __start_noun5__ world __end_noun5__ __start_noun6__ countries __end_noun6__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> cell (c) in the phone (c) . <PER_2> has <num> company (c) in the phone (c) . How many countries (c) are in the countries (c) ? <eos>|||<PER_1> has <num>|271 cell (c)|40 in the|186 phone (c)|132 . <PER_2> has <num>|178 company (c)|66 in the|21 phone (c)|22 . How many|107 countries (c)|45 are in the|3 countries (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.39

__start_noun0__ plums __end_noun0__ __start_noun1__ oranges __end_noun1__ __start_noun2__ orchard __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> plums (c) in the orchard (c) . <PER_2> has <num> oranges (c) in the orchard (c) . How many oranges (c) are in the orchard (c) ? <eos>|||<PER_1> has <num>|271 plums (c)|40 in the|186 orchard (c)|132 . <PER_2> has <num>|178 oranges (c)|66 in the|21 orchard (c)|22 . How many|107 oranges (c)|45 are in the|3 orchard (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.28

__start_noun0__ violet __end_noun0__ __start_noun1__ balloons __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> violet (c) in the balloons (c) . <PER_2> has <num> balloons (c) in the balloons (c) . How many violet (c) are in the balloons (c) ? <eos>|||<PER_1> has <num>|271 violet (c)|40 in the|186 balloons (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 balloons (c)|22 . How many|107 violet (c)|45 are in the|3 balloons (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.25

__start_noun0__ balloons __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> balloons (c) in the balloons (c) . <PER_2> has <num> balloons (c) in the balloons (c) . How many balloons (c) are the balloons (c) ? <eos>|||<PER_1> has <num>|271 balloons (c)|40 in the|186 balloons (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 balloons (c)|22 . How many|107 balloons (c)|45 are the|3 balloons (c)|75 ? <eos>|139
a=-0.90 t=-0.67 g=-0.23

__start_noun0__ beach __end_noun0__ __start_noun1__ sister __end_noun1__ __start_noun2__ sandcastles __end_noun2__ __start_noun3__ heights __end_noun3__ __start_noun4__ sandcastle __end_noun4__ __start_noun5__ foot __end_noun5__ __start_noun6__ tall __end_noun6__ __start_noun7__ taller __end_noun7__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> beach (c) in the sandcastles (c) . <PER_2> has <num> sister (c) in the sandcastles (c) . How many tall (c) are in the tall (c) ? <eos>|||<PER_1> has <num>|271 beach (c)|40 in the|186 sandcastles (c)|132 . <PER_2> has <num>|178 sister (c)|66 in the|21 sandcastles (c)|22 . How many|107 tall (c)|45 are in the|3 tall (c)|75 ? <eos>|139
a=-0.99 t=-0.62 g=-0.38

__start_noun0__ potatoes __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> potatoes (c) in the potatoes (c) . <PER_2> has <num> potatoes (c) in the potatoes (c) . How many potatoes (c) are in the potatoes (c) ? <eos>|||<PER_1> has <num>|271 potatoes (c)|40 in the|186 potatoes (c)|132 . <PER_2> has <num>|178 potatoes (c)|66 in the|21 potatoes (c)|22 . How many|107 potatoes (c)|45 are in the|3 potatoes (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.23

__start_noun0__ cup __end_noun0__ __start_noun1__ oil __end_noun1__ __start_noun2__ measuring __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> cup (c) in the oil (c) . <PER_2> has <num> oil (c) in the oil (c) . How many oil (c) are in the oil (c) ? <eos>|||<PER_1> has <num>|271 cup (c)|40 in the|186 oil (c)|132 . <PER_2> has <num>|178 oil (c)|66 in the|21 oil (c)|22 . How many|107 oil (c)|45 are in the|3 oil (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.31

__start_noun0__ houses __end_noun0__ __start_noun1__ housing __end_noun1__ __start_noun2__ boom __end_noun2__ __start_noun3__ developers __end_noun3__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> houses (c) in the boom (c) . <PER_2> has <num> houses (c) in the boom (c) . How many houses (c) are in the boom (c) ? <eos>|||<PER_1> has <num>|271 houses (c)|40 in the|186 boom (c)|132 . <PER_2> has <num>|178 houses (c)|66 in the|21 boom (c)|22 . How many|107 houses (c)|45 are in the|3 boom (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.33

__start_noun0__ books __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> books (c) in the books (c) . <PER_2> has <num> books (c) in the books (c) . How many books (c) are in the books (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 books (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 books (c)|22 . How many|107 books (c)|45 are in the|3 books (c)|75 ? <eos>|139
a=-0.93 t=-0.67 g=-0.25

__start_noun0__ books __end_noun0__ __start_noun1__ sale __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> books (c) in the sale (c) . <PER_2> has <num> books (c) in the sale (c) . How many books (c) are in the sale (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 sale (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 sale (c)|22 . How many|107 books (c)|45 are in the|3 sale (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ inch __end_noun0__ __start_noun1__ morning __end_noun1__ __start_noun2__ afternoon __end_noun2__ __start_noun3__ amount __end_noun3__ __start_noun4__ snowfall __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> inch (c) in the afternoon (c) . <PER_2> has <num> inch (c) in the afternoon (c) . How many inch (c) are in the snowfall (c) ? <eos>|||<PER_1> has <num>|271 inch (c)|40 in the|186 afternoon (c)|132 . <PER_2> has <num>|178 inch (c)|66 in the|21 afternoon (c)|22 . How many|107 inch (c)|45 are in the|3 snowfall (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ mile __end_noun0__ __start_noun1__ run __end_noun1__ __start_noun2__ walk __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> mile (c) in the walk (c) . <PER_2> has <num> mile (c) in the walk (c) . How many mile (c) are in the walk (c) ? <eos>|||<PER_1> has <num>|271 mile (c)|40 in the|186 walk (c)|132 . <PER_2> has <num>|178 mile (c)|66 in the|21 walk (c)|22 . How many|107 mile (c)|45 are in the|3 walk (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ laps __end_noun0__ __start_noun1__ class __end_noun1__ __start_noun2__ track __end_noun2__ __start_noun3__ practice __end_noun3__ __start_noun4__ jog __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> laps (c) in the track (c) . <PER_2> has <num> class (c) in the track (c) . How many practice (c) are in the jog (c) ? <eos>|||<PER_1> has <num>|271 laps (c)|40 in the|186 track (c)|132 . <PER_2> has <num>|178 class (c)|66 in the|21 track (c)|22 . How many|107 practice (c)|45 are in the|3 jog (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ ounces __end_noun0__ __start_noun1__ sugar __end_noun1__ __start_noun2__ floor __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> ounces (c) in the floor (c) . <PER_2> has <num> sugar (c) in the floor (c) . How many sugar (c) are in the floor (c) ? <eos>|||<PER_1> has <num>|271 ounces (c)|40 in the|186 floor (c)|132 . <PER_2> has <num>|178 sugar (c)|66 in the|21 floor (c)|22 . How many|107 sugar (c)|45 are in the|3 floor (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ farmer __end_noun0__ __start_noun1__ lambs __end_noun1__ __start_noun2__ ones __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> farmer (c) in the ones (c) . <PER_2> has <num> farmer (c) in the ones (c) . How many farmer (c) are in the ones (c) ? <eos>|||<PER_1> has <num>|271 farmer (c)|40 in the|186 ones (c)|132 . <PER_2> has <num>|178 farmer (c)|66 in the|21 ones (c)|22 . How many|107 farmer (c)|45 are in the|3 ones (c)|75 ? <eos>|139
a=-0.93 t=-0.61 g=-0.32

__start_noun0__ pears __end_noun0__ __start_noun1__ tree __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> pears (c) in the tree (c) . <PER_2> has <num> pears (c) in the tree (c) . How many pears (c) are in the tree (c) ? <eos>|||<PER_1> has <num>|271 pears (c)|40 in the|186 tree (c)|132 . <PER_2> has <num>|178 pears (c)|66 in the|21 tree (c)|22 . How many|107 pears (c)|45 are in the|3 tree (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ trees __end_noun0__ __start_noun1__ park __end_noun1__ __start_noun2__ workers __end_noun2__ __start_noun3__ plant __end_noun3__ __start_noun4__ maple __end_noun4__ __start_noun5__ today __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> maple (c) in the park (c) . <PER_2> has <num> maple (c) in the park (c) . How many maple (c) are in the today (c) ? <eos>|||<PER_1> has <num>|271 maple (c)|40 in the|186 park (c)|132 . <PER_2> has <num>|178 maple (c)|66 in the|21 park (c)|22 . How many|107 maple (c)|45 are in the|3 today (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.31

__start_noun0__ total __end_noun0__ __start_noun1__ peaches __end_noun1__ __start_noun2__ dollar __end_noun2__ __start_noun3__ coupon __end_noun3__ __start_noun4__ cherries __end_noun4__ __start_noun5__ money __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> total (c) in the dollar (c) . <PER_2> has <num> peaches (c) in the dollar (c) . How many money (c) are in the cherries (c) ? <eos>|||<PER_1> has <num>|271 total (c)|40 in the|186 dollar (c)|132 . <PER_2> has <num>|178 peaches (c)|66 in the|21 dollar (c)|22 . How many|107 money (c)|45 are in the|3 cherries (c)|75 ? <eos>|139
a=-0.99 t=-0.62 g=-0.37

__start_noun0__ trees __end_noun0__ __start_noun1__ park __end_noun1__ __start_noun2__ workers __end_noun2__ __start_noun3__ oak __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> trees (c) in the park (c) . <PER_2> has <num> oak (c) in the park (c) . How many oak (c) are in the park (c) ? <eos>|||<PER_1> has <num>|271 trees (c)|40 in the|186 park (c)|132 . <PER_2> has <num>|178 oak (c)|66 in the|21 park (c)|22 . How many|107 oak (c)|45 are in the|3 park (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.30

__start_noun0__ oranges __end_noun0__ __start_noun1__ apples __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> oranges (c) in the apples (c) . <PER_2> has <num> apples (c) in the apples (c) . How many oranges (c) are in the apples (c) ? <eos>|||<PER_1> has <num>|271 oranges (c)|40 in the|186 apples (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 apples (c)|22 . How many|107 oranges (c)|45 are in the|3 apples (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.25

__start_noun0__ mall __end_noun0__ __start_noun1__ shirt __end_noun1__ __start_noun2__ jacket __end_noun2__ __start_noun3__ shops __end_noun3__ __start_noun4__ money __end_noun4__ __start_noun5__ spend __end_noun5__ __start_noun6__ clothing __end_noun6__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> mall (c) in the shirt (c) . <PER_2> has <num> money (c) in the shirt (c) . How many money (c) are in the clothing (c) ? <eos>|||<PER_1> has <num>|271 mall (c)|40 in the|186 shirt (c)|132 . <PER_2> has <num>|178 money (c)|66 in the|21 shirt (c)|22 . How many|107 money (c)|45 are in the|3 clothing (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ dish __end_noun0__ __start_noun1__ bacteria __end_noun1__ __start_noun2__ scientist __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> dish (c) in the scientist (c) . <PER_2> has <num> dish (c) in the scientist (c) . How many dish (c) are in the scientist (c) ? <eos>|||<PER_1> has <num>|271 dish (c)|40 in the|186 scientist (c)|132 . <PER_2> has <num>|178 dish (c)|66 in the|21 scientist (c)|22 . How many|107 dish (c)|45 are in the|3 scientist (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ quarters __end_noun0__ __start_noun1__ dimes __end_noun1__ __start_noun2__ bank __end_noun2__ __start_noun3__ sister __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> quarters (c) in the bank (c) . <PER_2> has <num> dimes (c) in the bank (c) . How many dimes (c) are in the dimes (c) ? <eos>|||<PER_1> has <num>|271 quarters (c)|40 in the|186 bank (c)|132 . <PER_2> has <num>|178 dimes (c)|66 in the|21 bank (c)|22 . How many|107 dimes (c)|45 are in the|3 dimes (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.30

__start_noun0__ carrots __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> carrots (c) in the carrots (c) . <PER_2> has <num> carrots (c) in the carrots (c) . How many carrots (c) are in the carrots (c) ? <eos>|||<PER_1> has <num>|271 carrots (c)|40 in the|186 carrots (c)|132 . <PER_2> has <num>|178 carrots (c)|66 in the|21 carrots (c)|22 . How many|107 carrots (c)|45 are in the|3 carrots (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.24

__start_noun0__ dog __end_noun0__ __start_noun1__ puppies __end_noun1__ __start_noun2__ spots __end_noun2__ __start_noun3__ friends __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> dog (c) in the spots (c) . <PER_2> has <num> puppies (c) in the spots (c) . How many puppies (c) are in the puppies (c) ? <eos>|||<PER_1> has <num>|271 dog (c)|40 in the|186 spots (c)|132 . <PER_2> has <num>|178 puppies (c)|66 in the|21 spots (c)|22 . How many|107 puppies (c)|45 are in the|3 puppies (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ football __end_noun0__ __start_noun1__ games __end_noun1__ __start_noun2__ year __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> football (c) in the year (c) . <PER_2> has <num> games (c) in the year (c) . How many football (c) are in the year (c) ? <eos>|||<PER_1> has <num>|271 football (c)|40 in the|186 year (c)|132 . <PER_2> has <num>|178 games (c)|66 in the|21 year (c)|22 . How many|107 football (c)|45 are in the|3 year (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ books __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> books (c) in the books (c) . <PER_2> has <num> books (c) in the books (c) . How many books (c) are in the books (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 books (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 books (c)|22 . How many|107 books (c)|45 are in the|3 books (c)|75 ? <eos>|139
a=-0.93 t=-0.67 g=-0.25

__start_noun0__ dust __end_noun0__ __start_noun1__ storm __end_noun1__ __start_noun2__ prairie __end_noun2__ __start_noun3__ acres __end_noun3__ __start_noun4__ cover __end_noun4__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> dust (c) in the prairie (c) . <PER_2> has <num> acres (c) in the prairie (c) . How many acres (c) are in the cover (c) ? <eos>|||<PER_1> has <num>|271 dust (c)|40 in the|186 prairie (c)|132 . <PER_2> has <num>|178 acres (c)|66 in the|21 prairie (c)|22 . How many|107 acres (c)|45 are in the|3 cover (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.39

__start_noun0__ inventory __end_noun0__ __start_noun1__ pastry __end_noun1__ __start_noun2__ shop __end_noun2__ __start_noun3__ box __end_noun3__ __start_noun4__ powder __end_noun4__ __start_noun5__ yesterday __end_noun5__ __start_noun6__ supply __end_noun6__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> inventory (c) in the shop (c) . <PER_2> has <num> yesterday (c) in the shop (c) . How many supply (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 inventory (c)|40 in the|186 shop (c)|132 . <PER_2> has <num>|178 yesterday (c)|66 in the|21 shop (c)|22 . How many|107 supply (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-1.02 t=-0.62 g=-0.40

__start_noun0__ watermelons __end_noun0__ __start_noun1__ rabbits __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> watermelons (c) in the rabbits (c) . <PER_2> has <num> watermelons (c) in the rabbits (c) . How many watermelons (c) are in the rabbits (c) ? <eos>|||<PER_1> has <num>|271 watermelons (c)|40 in the|186 rabbits (c)|132 . <PER_2> has <num>|178 watermelons (c)|66 in the|21 rabbits (c)|22 . How many|107 watermelons (c)|45 are in the|3 rabbits (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ farmer __end_noun0__ __start_noun1__ bushels __end_noun1__ __start_noun2__ wheat __end_noun2__ __start_noun3__ weather __end_noun3__ __start_noun4__ season __end_noun4__ __start_noun5__ harvest __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> farmer (c) in the bushels (c) . <PER_2> has <num> harvest (c) in the bushels (c) . How many harvest (c) are in the harvest (c) ? <eos>|||<PER_1> has <num>|271 farmer (c)|40 in the|186 bushels (c)|132 . <PER_2> has <num>|178 harvest (c)|66 in the|21 bushels (c)|22 . How many|107 harvest (c)|45 are in the|3 harvest (c)|75 ? <eos>|139
a=-1.00 t=-0.62 g=-0.38

__start_noun0__ shorts __end_noun0__ __start_noun1__ jacket __end_noun1__ __start_noun2__ shirt __end_noun2__ __start_noun3__ shops __end_noun3__ __start_noun4__ money __end_noun4__ __start_noun5__ clothing __end_noun5__ __start_solution_type__ TimeVariantUnknownFinal __end_solution_type__

<PER_1> has <num> shorts (c) in the shirt (c) . <PER_2> has <num> shorts (c) in the shirt (c) . How many money (c) are in the clothing (c) ? <eos>|||<PER_1> has <num>|271 shorts (c)|40 in the|186 shirt (c)|132 . <PER_2> has <num>|178 shorts (c)|66 in the|21 shirt (c)|22 . How many|107 money (c)|45 are in the|3 clothing (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.35

__start_noun0__ family __end_noun0__ __start_noun1__ budget __end_noun1__ __start_noun2__ groceries __end_noun2__ __start_noun3__ fraction __end_noun3__ __start_noun4__ spend __end_noun4__ __start_noun5__ food __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> family (c) in the groceries (c) . <PER_2> has <num> spend (c) in the groceries (c) . How many food (c) are in the spend (c) ? <eos>|||<PER_1> has <num>|271 family (c)|40 in the|186 groceries (c)|132 . <PER_2> has <num>|178 spend (c)|66 in the|21 groceries (c)|22 . How many|107 food (c)|45 are in the|3 spend (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ punch __end_noun0__ __start_noun1__ friend __end_noun1__ __start_noun2__ birthday __end_noun2__ __start_noun3__ party __end_noun3__ __start_noun4__ gallon __end_noun4__ __start_noun5__ grape __end_noun5__ __start_noun6__ juice __end_noun6__ __start_noun7__ cranberry __end_noun7__ __start_noun8__ club __end_noun8__ __start_noun9__ soda __end_noun9__ __start_noun10__ gallons __end_noun10__ __start_solution_type__ Sum __end_solution_type__

<PER_1> has <num> punch (c) in the friend (c) . <PER_2> has <num> gallon (c) in the friend (c) . How many juice (c) are in the cranberry (c) ? <eos>|||<PER_1> has <num>|271 punch (c)|40 in the|186 friend (c)|132 . <PER_2> has <num>|178 gallon (c)|66 in the|21 friend (c)|22 . How many|107 juice (c)|45 are in the|3 cranberry (c)|75 ? <eos>|139
a=-1.03 t=-0.62 g=-0.41

__start_noun0__ apples __end_noun0__ __start_noun1__ tickets __end_noun1__ __start_noun2__ store __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> apples (c) in the store (c) . <PER_2> has <num> apples (c) in the store (c) . How many apples (c) are in the store (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 store (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 store (c)|22 . How many|107 apples (c)|45 are in the|3 store (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ eggs __end_noun0__ __start_noun1__ hen __end_noun1__ __start_noun2__ baskets __end_noun2__ __start_noun3__ basket __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> eggs (c) in the baskets (c) . <PER_2> has <num> eggs (c) in the baskets (c) . How many eggs (c) are in the baskets (c) ? <eos>|||<PER_1> has <num>|271 eggs (c)|40 in the|186 baskets (c)|132 . <PER_2> has <num>|178 eggs (c)|66 in the|21 baskets (c)|22 . How many|107 eggs (c)|45 are in the|3 baskets (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.31

__start_noun0__ cards __end_noun0__ __start_noun1__ father __end_noun1__ __start_noun2__ apples __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> cards (c) in the father (c) . <PER_2> has <num> apples (c) in the father (c) . How many cards (c) are in the father (c) ? <eos>|||<PER_1> has <num>|271 cards (c)|40 in the|186 father (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 father (c)|22 . How many|107 cards (c)|45 are in the|3 father (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ toucans __end_noun0__ __start_noun1__ limb __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> toucans (c) in the limb (c) . <PER_2> has <num> toucans (c) in the limb (c) . How many toucans (c) are in the limb (c) ? <eos>|||<PER_1> has <num>|271 toucans (c)|40 in the|186 limb (c)|132 . <PER_2> has <num>|178 toucans (c)|66 in the|21 limb (c)|22 . How many|107 toucans (c)|45 are in the|3 limb (c)|75 ? <eos>|139
a=-0.88 t=-0.62 g=-0.27

__start_noun0__ carrot __end_noun0__ __start_noun1__ sticks __end_noun1__ __start_noun2__ dinner __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> carrot (c) in the dinner (c) . <PER_2> has <num> sticks (c) in the dinner (c) . How many sticks (c) are in the sticks (c) ? <eos>|||<PER_1> has <num>|271 carrot (c)|40 in the|186 dinner (c)|132 . <PER_2> has <num>|178 sticks (c)|66 in the|21 dinner (c)|22 . How many|107 sticks (c)|45 are in the|3 sticks (c)|75 ? <eos>|139
a=-0.93 t=-0.61 g=-0.32

__start_noun0__ track __end_noun0__ __start_noun1__ team __end_noun1__ __start_noun2__ laps __end_noun2__ __start_noun3__ minute __end_noun3__ __start_noun4__ minutes __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> track (c) in the laps (c) . <PER_2> has <num> minutes (c) in the laps (c) . How many minutes (c) are in the minutes (c) ? <eos>|||<PER_1> has <num>|271 track (c)|40 in the|186 laps (c)|132 . <PER_2> has <num>|178 minutes (c)|66 in the|21 laps (c)|22 . How many|107 minutes (c)|45 are in the|3 minutes (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ students __end_noun0__ __start_noun1__ table __end_noun1__ __start_noun2__ lunchroom __end_noun2__ __start_noun3__ tables __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> students (c) in the lunchroom (c) . <PER_2> has <num> students (c) in the lunchroom (c) . How many students (c) are in the lunchroom (c) ? <eos>|||<PER_1> has <num>|271 students (c)|40 in the|186 lunchroom (c)|132 . <PER_2> has <num>|178 students (c)|66 in the|21 lunchroom (c)|22 . How many|107 students (c)|45 are in the|3 lunchroom (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ Nicholas __end_noun0__ __start_noun1__ bottle __end_noun1__ __start_noun2__ caps __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> bottle (c) in the caps (c) . <PER_2> has <num> bottle (c) in the caps (c) . How many bottle (c) are in the caps (c) ? <eos>|||<PER_1> has <num>|271 bottle (c)|40 in the|186 caps (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 caps (c)|22 . How many|107 bottle (c)|45 are in the|3 caps (c)|75 ? <eos>|139
a=-0.87 t=-0.61 g=-0.26

__start_noun0__ bottle __end_noun0__ __start_noun1__ caps __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> bottle (c) in the caps (c) . <PER_2> has <num> bottle (c) in the caps (c) . How many bottle (c) are in the caps (c) ? <eos>|||<PER_1> has <num>|271 bottle (c)|40 in the|186 caps (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 caps (c)|22 . How many|107 bottle (c)|45 are in the|3 caps (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ pencils __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> pencils (c) in the pencils (c) . <PER_2> has <num> pencils (c) in the pencils (c) . How many pencils (c) are the pencils (c) ? <eos>|||<PER_1> has <num>|271 pencils (c)|40 in the|186 pencils (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 pencils (c)|22 . How many|107 pencils (c)|45 are the|3 pencils (c)|75 ? <eos>|139
a=-0.94 t=-0.67 g=-0.26

__start_noun0__ grocery __end_noun0__ __start_noun1__ store __end_noun1__ __start_noun2__ packs __end_noun2__ __start_noun3__ cookies __end_noun3__ __start_noun4__ noodles __end_noun4__ __start_noun5__ groceries __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> grocery (c) in the store (c) . <PER_2> has <num> cookies (c) in the store (c) . How many cookies (c) are in the groceries (c) ? <eos>|||<PER_1> has <num>|271 grocery (c)|40 in the|186 store (c)|132 . <PER_2> has <num>|178 cookies (c)|66 in the|21 store (c)|22 . How many|107 cookies (c)|45 are in the|3 groceries (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ miles __end_noun0__ __start_noun1__ hour __end_noun1__ __start_noun2__ sprint __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> miles (c) in the hour (c) . <PER_2> has <num> miles (c) in the hour (c) . How many miles (c) are in the sprint (c) ? <eos>|||<PER_1> has <num>|271 miles (c)|40 in the|186 hour (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hour (c)|22 . How many|107 miles (c)|45 are in the|3 sprint (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.28

__start_noun0__ birds __end_noun0__ __start_noun1__ tree __end_noun1__ __start_noun2__ fly __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> birds (c) in the tree (c) . <PER_2> has <num> birds (c) in the tree (c) . How many birds (c) are in the fly (c) ? <eos>|||<PER_1> has <num>|271 birds (c)|40 in the|186 tree (c)|132 . <PER_2> has <num>|178 birds (c)|66 in the|21 tree (c)|22 . How many|107 birds (c)|45 are in the|3 fly (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ family __end_noun0__ __start_noun1__ vacation __end_noun1__ __start_noun2__ mom __end_noun2__ __start_noun3__ car __end_noun3__ __start_noun4__ mph __end_noun4__ __start_noun5__ campground __end_noun5__ __start_noun6__ hours __end_noun6__ __start_noun7__ home __end_noun7__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> family (c) in the vacation (c) . <PER_2> has <num> hours (c) in the vacation (c) . How many hours (c) are in the home (c) ? <eos>|||<PER_1> has <num>|271 family (c)|40 in the|186 vacation (c)|132 . <PER_2> has <num>|178 hours (c)|66 in the|21 vacation (c)|22 . How many|107 hours (c)|45 are in the|3 home (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.37

__start_noun0__ touchdowns __end_noun0__ __start_noun1__ points __end_noun1__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> touchdowns (c) in the points (c) . <PER_2> has <num> points (c) in the points (c) . How many points (c) are in the points (c) ? <eos>|||<PER_1> has <num>|271 touchdowns (c)|40 in the|186 points (c)|132 . <PER_2> has <num>|178 points (c)|66 in the|21 points (c)|22 . How many|107 points (c)|45 are in the|3 points (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.24

__start_noun0__ boxes __end_noun0__ __start_noun1__ cases __end_noun1__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> boxes (c) in the cases (c) . <PER_2> has <num> boxes (c) in the cases (c) . How many boxes (c) are in the cases (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 cases (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 cases (c)|22 . How many|107 boxes (c)|45 are in the|3 cases (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.25

__start_noun0__ cards __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> cards (c) in the cards (c) . <PER_2> has <num> cards (c) in the cards (c) . How many cards (c) are the cards (c) ? <eos>|||<PER_1> has <num>|271 cards (c)|40 in the|186 cards (c)|132 . <PER_2> has <num>|178 cards (c)|66 in the|21 cards (c)|22 . How many|107 cards (c)|45 are the|3 cards (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.23

__start_noun0__ tower __end_noun0__ __start_noun1__ blocks __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> tower (c) in the blocks (c) . <PER_2> has <num> blocks (c) in the blocks (c) . How many blocks (c) are in the blocks (c) ? <eos>|||<PER_1> has <num>|271 tower (c)|40 in the|186 blocks (c)|132 . <PER_2> has <num>|178 blocks (c)|66 in the|21 blocks (c)|22 . How many|107 blocks (c)|45 are in the|3 blocks (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.25

__start_noun0__ stickers __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> stickers (c) in the stickers (c) . <PER_2> has <num> stickers (c) in the stickers (c) . How many stickers (c) are the stickers (c) ? <eos>|||<PER_1> has <num>|271 stickers (c)|40 in the|186 stickers (c)|132 . <PER_2> has <num>|178 stickers (c)|66 in the|21 stickers (c)|22 . How many|107 stickers (c)|45 are the|3 stickers (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ starts __end_noun0__ __start_noun1__ eggs __end_noun1__ __start_noun2__ end __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> starts (c) in the eggs (c) . <PER_2> has <num> eggs (c) in the eggs (c) . How many eggs (c) are in the end (c) ? <eos>|||<PER_1> has <num>|271 starts (c)|40 in the|186 eggs (c)|132 . <PER_2> has <num>|178 eggs (c)|66 in the|21 eggs (c)|22 . How many|107 eggs (c)|45 are in the|3 end (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.31

__start_noun0__ snowballs __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> snowballs (c) in the snowballs (c) . <PER_2> has <num> snowballs (c) in the snowballs (c) . How many snowballs (c) are the snowballs (c) ? <eos>|||<PER_1> has <num>|271 snowballs (c)|40 in the|186 snowballs (c)|132 . <PER_2> has <num>|178 snowballs (c)|66 in the|21 snowballs (c)|22 . How many|107 snowballs (c)|45 are the|3 snowballs (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ school __end_noun0__ __start_noun1__ field __end_noun1__ __start_noun2__ trip __end_noun2__ __start_noun3__ students __end_noun3__ __start_noun4__ seats __end_noun4__ __start_noun5__ bus __end_noun5__ __start_noun6__ buses __end_noun6__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> school (c) in the trip (c) . <PER_2> has <num> students (c) in the trip (c) . How many buses (c) are in the trip (c) ? <eos>|||<PER_1> has <num>|271 school (c)|40 in the|186 trip (c)|132 . <PER_2> has <num>|178 students (c)|66 in the|21 trip (c)|22 . How many|107 buses (c)|45 are in the|3 trip (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.33

__start_noun0__ blocks __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> blocks (c) in the blocks (c) . <PER_2> has <num> blocks (c) in the blocks (c) . How many blocks (c) are in the blocks (c) ? <eos>|||<PER_1> has <num>|271 blocks (c)|40 in the|186 blocks (c)|132 . <PER_2> has <num>|178 blocks (c)|66 in the|21 blocks (c)|22 . How many|107 blocks (c)|45 are in the|3 blocks (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.25

__start_noun0__ money __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> money (c) in the money (c) . <PER_2> has <num> money (c) in the money (c) . How many money (c) are the money (c) ? <eos>|||<PER_1> has <num>|271 money (c)|40 in the|186 money (c)|132 . <PER_2> has <num>|178 money (c)|66 in the|21 money (c)|22 . How many|107 money (c)|45 are the|3 money (c)|75 ? <eos>|139
a=-0.94 t=-0.67 g=-0.26

__start_noun0__ cup __end_noun0__ __start_noun1__ ounces __end_noun1__ __start_noun2__ cups __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> cup (c) in the ounces (c) . <PER_2> has <num> cups (c) in the ounces (c) . How many cup (c) are in the cups (c) ? <eos>|||<PER_1> has <num>|271 cup (c)|40 in the|186 ounces (c)|132 . <PER_2> has <num>|178 cups (c)|66 in the|21 ounces (c)|22 . How many|107 cup (c)|45 are in the|3 cups (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.31

__start_noun0__ apples __end_noun0__ __start_noun1__ people __end_noun1__ __start_noun2__ class __end_noun2__ __start_noun3__ left __end_noun3__ __start_noun4__ overs __end_noun4__ __start_noun5__ classmate __end_noun5__ __start_noun6__ get __end_noun6__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> apples (c) in the class (c) . <PER_2> has <num> apples (c) in the class (c) . How many apples (c) are in the get (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 class (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 class (c)|22 . How many|107 apples (c)|45 are in the|3 get (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ erasers __end_noun0__ __start_noun1__ box __end_noun1__ __start_noun2__ bag __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> erasers (c) in the box (c) . <PER_2> has <num> erasers (c) in the box (c) . How many erasers (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 erasers (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 erasers (c)|66 in the|21 box (c)|22 . How many|107 erasers (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ apples __end_noun0__ __start_noun1__ pie __end_noun1__ __start_noun2__ pies __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> apples (c) in the pies (c) . <PER_2> has <num> apples (c) in the pies (c) . How many apples (c) are in the pies (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 pies (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 pies (c)|22 . How many|107 apples (c)|45 are in the|3 pies (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ tickets __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> tickets (c) in the tickets (c) . <PER_2> has <num> tickets (c) in the tickets (c) . How many tickets (c) are in the tickets (c) ? <eos>|||<PER_1> has <num>|271 tickets (c)|40 in the|186 tickets (c)|132 . <PER_2> has <num>|178 tickets (c)|66 in the|21 tickets (c)|22 . How many|107 tickets (c)|45 are in the|3 tickets (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ beavers __end_noun0__ __start_noun1__ home __end_noun1__ __start_noun2__ swim __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> beavers (c) in the swim (c) . <PER_2> has <num> home (c) in the swim (c) . How many beavers (c) are in the swim (c) ? <eos>|||<PER_1> has <num>|271 beavers (c)|40 in the|186 swim (c)|132 . <PER_2> has <num>|178 home (c)|66 in the|21 swim (c)|22 . How many|107 beavers (c)|45 are in the|3 swim (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.31

__start_noun0__ child __end_noun0__ __start_noun1__ pencils __end_noun1__ __start_noun2__ children __end_noun2__ __start_noun3__ total __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> child (c) in the children (c) . <PER_2> has <num> pencils (c) in the children (c) . How many pencils (c) are in the total (c) ? <eos>|||<PER_1> has <num>|271 child (c)|40 in the|186 children (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 children (c)|22 . How many|107 pencils (c)|45 are in the|3 total (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.33

__start_noun0__ markers __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> markers (c) in the markers (c) . <PER_2> has <num> markers (c) in the markers (c) . How many markers (c) are in the markers (c) ? <eos>|||<PER_1> has <num>|271 markers (c)|40 in the|186 markers (c)|132 . <PER_2> has <num>|178 markers (c)|66 in the|21 markers (c)|22 . How many|107 markers (c)|45 are in the|3 markers (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.23

__start_noun0__ flowers __end_noun0__ __start_noun1__ bees __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> flowers (c) in the bees (c) . <PER_2> has <num> flowers (c) in the bees (c) . How many flowers (c) are in the bees (c) ? <eos>|||<PER_1> has <num>|271 flowers (c)|40 in the|186 bees (c)|132 . <PER_2> has <num>|178 flowers (c)|66 in the|21 bees (c)|22 . How many|107 flowers (c)|45 are in the|3 bees (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.24

__start_noun0__ birds __end_noun0__ __start_noun1__ tree __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> birds (c) in the tree (c) . <PER_2> has <num> birds (c) in the tree (c) . How many birds (c) are in the tree (c) ? <eos>|||<PER_1> has <num>|271 birds (c)|40 in the|186 tree (c)|132 . <PER_2> has <num>|178 birds (c)|66 in the|21 tree (c)|22 . How many|107 birds (c)|45 are in the|3 tree (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ oranges __end_noun0__ __start_noun1__ store __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> oranges (c) in the store (c) . <PER_2> has <num> oranges (c) in the store (c) . How many oranges (c) are in the store (c) ? <eos>|||<PER_1> has <num>|271 oranges (c)|40 in the|186 store (c)|132 . <PER_2> has <num>|178 oranges (c)|66 in the|21 store (c)|22 . How many|107 oranges (c)|45 are in the|3 store (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ miles __end_noun0__ __start_noun1__ hour __end_noun1__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> miles (c) in the hour (c) . <PER_2> has <num> miles (c) in the hour (c) . How many miles (c) are in the hour (c) ? <eos>|||<PER_1> has <num>|271 miles (c)|40 in the|186 hour (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hour (c)|22 . How many|107 miles (c)|45 are in the|3 hour (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ apples __end_noun0__ __start_noun1__ box __end_noun1__ __start_noun2__ bag __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> apples (c) in the box (c) . <PER_2> has <num> apples (c) in the box (c) . How many apples (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 box (c)|22 . How many|107 apples (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ packages __end_noun0__ __start_noun1__ gum __end_noun1__ __start_noun2__ pieces __end_noun2__ __start_noun3__ package __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> packages (c) in the gum (c) . <PER_2> has <num> pieces (c) in the gum (c) . How many pieces (c) are in the gum (c) ? <eos>|||<PER_1> has <num>|271 packages (c)|40 in the|186 gum (c)|132 . <PER_2> has <num>|178 pieces (c)|66 in the|21 gum (c)|22 . How many|107 pieces (c)|45 are in the|3 gum (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.34

__start_noun0__ balloons __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> balloons (c) in the balloons (c) . <PER_2> has <num> balloons (c) in the balloons (c) . How many balloons (c) are the balloons (c) ? <eos>|||<PER_1> has <num>|271 balloons (c)|40 in the|186 balloons (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 balloons (c)|22 . How many|107 balloons (c)|45 are the|3 balloons (c)|75 ? <eos>|139
a=-0.90 t=-0.67 g=-0.23

__start_noun0__ boxes __end_noun0__ __start_noun1__ blocks __end_noun1__ __start_noun2__ box __end_noun2__ __start_noun3__ case __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> boxes (c) in the box (c) . <PER_2> has <num> boxes (c) in the box (c) . How many boxes (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 box (c)|22 . How many|107 boxes (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.31

__start_noun0__ points __end_noun0__ __start_noun1__ game __end_noun1__ __start_noun2__ score __end_noun2__ __start_noun3__ games __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> points (c) in the game (c) . <PER_2> has <num> points (c) in the game (c) . How many points (c) are in the games (c) ? <eos>|||<PER_1> has <num>|271 points (c)|40 in the|186 game (c)|132 . <PER_2> has <num>|178 points (c)|66 in the|21 game (c)|22 . How many|107 points (c)|45 are in the|3 games (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.33

__start_noun0__ bananas __end_noun0__ __start_noun1__ boxes __end_noun1__ __start_noun2__ cookies __end_noun2__ __start_noun3__ share __end_noun3__ __start_noun4__ box __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> bananas (c) in the boxes (c) . <PER_2> has <num> cookies (c) in the boxes (c) . How many cookies (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 bananas (c)|40 in the|186 boxes (c)|132 . <PER_2> has <num>|178 cookies (c)|66 in the|21 boxes (c)|22 . How many|107 cookies (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.32

__start_noun0__ books __end_noun0__ __start_noun1__ book __end_noun1__ __start_noun2__ chapters __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> books (c) in the chapters (c) . <PER_2> has <num> books (c) in the chapters (c) . How many books (c) are in the chapters (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 chapters (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 chapters (c)|22 . How many|107 books (c)|45 are in the|3 chapters (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ miles __end_noun0__ __start_noun1__ hour __end_noun1__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> miles (c) in the hour (c) . <PER_2> has <num> miles (c) in the hour (c) . How many miles (c) are in the hour (c) ? <eos>|||<PER_1> has <num>|271 miles (c)|40 in the|186 hour (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hour (c)|22 . How many|107 miles (c)|45 are in the|3 hour (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ apples __end_noun0__ __start_noun1__ jar __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> apples (c) in the jar (c) . <PER_2> has <num> apples (c) in the jar (c) . How many apples (c) are in the jar (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 jar (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 jar (c)|22 . How many|107 apples (c)|45 are in the|3 jar (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ books __end_noun0__ __start_noun1__ school __end_noun1__ __start_noun2__ rest __end_noun2__ __start_noun3__ sports __end_noun3__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> books (c) in the sports (c) . <PER_2> has <num> books (c) in the sports (c) . How many books (c) are in the sports (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 sports (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 sports (c)|22 . How many|107 books (c)|45 are in the|3 sports (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ house __end_noun0__ __start_noun1__ miles __end_noun1__ __start_noun2__ hours __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> house (c) in the hours (c) . <PER_2> has <num> miles (c) in the hours (c) . How many miles (c) are in the house (c) ? <eos>|||<PER_1> has <num>|271 house (c)|40 in the|186 hours (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hours (c)|22 . How many|107 miles (c)|45 are in the|3 house (c)|75 ? <eos>|139
a=-0.94 t=-0.61 g=-0.33

__start_noun0__ box __end_noun0__ __start_noun1__ crayons __end_noun1__ __start_noun2__ birthday __end_noun2__ __start_noun3__ end __end_noun3__ __start_noun4__ school __end_noun4__ __start_noun5__ year __end_noun5__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> school (c) in the birthday (c) . <PER_2> has <num> crayons (c) in the birthday (c) . How many crayons (c) are in the year (c) ? <eos>|||<PER_1> has <num>|271 school (c)|40 in the|186 birthday (c)|132 . <PER_2> has <num>|178 crayons (c)|66 in the|21 birthday (c)|22 . How many|107 crayons (c)|45 are in the|3 year (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.33

__start_noun0__ heads __end_noun0__ __start_noun1__ packages __end_noun1__ __start_noun2__ boxes __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> heads (c) in the boxes (c) . <PER_2> has <num> boxes (c) in the boxes (c) . How many boxes (c) are in the boxes (c) ? <eos>|||<PER_1> has <num>|271 heads (c)|40 in the|186 boxes (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 boxes (c)|22 . How many|107 boxes (c)|45 are in the|3 boxes (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.29

__start_noun0__ Jennifer __end_noun0__ __start_noun1__ apples __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> Jennifer (c) in the apples (c) . <PER_2> has <num> apples (c) in the apples (c) . How many apples (c) are in the apples (c) ? <eos>|||<PER_1> has <num>|271 Jennifer (c)|40 in the|186 apples (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 apples (c)|22 . How many|107 apples (c)|45 are in the|3 apples (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.26

__start_noun0__ bananas __end_noun0__ __start_noun1__ banana __end_noun1__ __start_noun2__ collection __end_noun2__ __start_noun3__ groups __end_noun3__ __start_noun4__ group __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> bananas (c) in the collection (c) . <PER_2> has <num> groups (c) in the collection (c) . How many groups (c) are in the group (c) ? <eos>|||<PER_1> has <num>|271 bananas (c)|40 in the|186 collection (c)|132 . <PER_2> has <num>|178 groups (c)|66 in the|21 collection (c)|22 . How many|107 groups (c)|45 are in the|3 group (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.32

__start_noun0__ fish __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> fish (c) in the fish (c) . <PER_2> has <num> fish (c) in the fish (c) . How many fish (c) are the fish (c) ? <eos>|||<PER_1> has <num>|271 fish (c)|40 in the|186 fish (c)|132 . <PER_2> has <num>|178 fish (c)|66 in the|21 fish (c)|22 . How many|107 fish (c)|45 are the|3 fish (c)|75 ? <eos>|139
a=-0.90 t=-0.67 g=-0.23

__start_noun0__ candies __end_noun0__ __start_noun1__ bananas __end_noun1__ __start_noun2__ shares __end_noun2__ __start_noun3__ friends __end_noun3__ __start_noun4__ friend __end_noun4__ __start_noun5__ get __end_noun5__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> candies (c) in the shares (c) . <PER_2> has <num> candies (c) in the shares (c) . How many candies (c) are in the friend (c) ? <eos>|||<PER_1> has <num>|271 candies (c)|40 in the|186 shares (c)|132 . <PER_2> has <num>|178 candies (c)|66 in the|21 shares (c)|22 . How many|107 candies (c)|45 are in the|3 friend (c)|75 ? <eos>|139
a=-0.98 t=-0.62 g=-0.36

__start_noun0__ trees __end_noun0__ __start_noun1__ backyard __end_noun1__ __start_noun2__ plants __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> trees (c) in the plants (c) . <PER_2> has <num> trees (c) in the plants (c) . How many trees (c) are in the plants (c) ? <eos>|||<PER_1> has <num>|271 trees (c)|40 in the|186 plants (c)|132 . <PER_2> has <num>|178 trees (c)|66 in the|21 plants (c)|22 . How many|107 trees (c)|45 are in the|3 plants (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.31

__start_noun0__ bananas __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> bananas (c) in the bananas (c) . <PER_2> has <num> bananas (c) in the bananas (c) . How many bananas (c) are the bananas (c) ? <eos>|||<PER_1> has <num>|271 bananas (c)|40 in the|186 bananas (c)|132 . <PER_2> has <num>|178 bananas (c)|66 in the|21 bananas (c)|22 . How many|107 bananas (c)|45 are the|3 bananas (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.24

__start_noun0__ blocks __end_noun0__ __start_noun1__ father __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> blocks (c) in the father (c) . <PER_2> has <num> blocks (c) in the father (c) . How many blocks (c) are in the father (c) ? <eos>|||<PER_1> has <num>|271 blocks (c)|40 in the|186 father (c)|132 . <PER_2> has <num>|178 blocks (c)|66 in the|21 father (c)|22 . How many|107 blocks (c)|45 are in the|3 father (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.25

__start_noun0__ peanuts __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> peanuts (c) in the peanuts (c) . <PER_2> has <num> peanuts (c) in the peanuts (c) . How many peanuts (c) are the peanuts (c) ? <eos>|||<PER_1> has <num>|271 peanuts (c)|40 in the|186 peanuts (c)|132 . <PER_2> has <num>|178 peanuts (c)|66 in the|21 peanuts (c)|22 . How many|107 peanuts (c)|45 are the|3 peanuts (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.24

__start_noun0__ presents __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> presents (c) in the presents (c) . <PER_2> has <num> presents (c) in the presents (c) . How many presents (c) are the presents (c) ? <eos>|||<PER_1> has <num>|271 presents (c)|40 in the|186 presents (c)|132 . <PER_2> has <num>|178 presents (c)|66 in the|21 presents (c)|22 . How many|107 presents (c)|45 are the|3 presents (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ cards __end_noun0__ __start_noun1__ hippopotamus __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> cards (c) in the hippopotamus (c) . <PER_2> has <num> cards (c) in the hippopotamus (c) . How many cards (c) are in the hippopotamus (c) ? <eos>|||<PER_1> has <num>|271 cards (c)|40 in the|186 hippopotamus (c)|132 . <PER_2> has <num>|178 cards (c)|66 in the|21 hippopotamus (c)|22 . How many|107 cards (c)|45 are in the|3 hippopotamus (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ house __end_noun0__ __start_noun1__ miles __end_noun1__ __start_noun2__ hours __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> house (c) in the hours (c) . <PER_2> has <num> miles (c) in the hours (c) . How many miles (c) are in the house (c) ? <eos>|||<PER_1> has <num>|271 house (c)|40 in the|186 hours (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hours (c)|22 . How many|107 miles (c)|45 are in the|3 house (c)|75 ? <eos>|139
a=-0.94 t=-0.61 g=-0.33

__start_noun0__ pizzas __end_noun0__ __start_noun1__ pizza __end_noun1__ __start_noun2__ slices __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> pizzas (c) in the pizza (c) . <PER_2> has <num> slices (c) in the pizza (c) . How many slices (c) are in the pizza (c) ? <eos>|||<PER_1> has <num>|271 pizzas (c)|40 in the|186 pizza (c)|132 . <PER_2> has <num>|178 slices (c)|66 in the|21 pizza (c)|22 . How many|107 slices (c)|45 are in the|3 pizza (c)|75 ? <eos>|139
a=-0.93 t=-0.61 g=-0.32

__start_noun0__ fish __end_noun0__ __start_noun1__ sister __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> fish (c) in the sister (c) . <PER_2> has <num> fish (c) in the sister (c) . How many fish (c) are in the sister (c) ? <eos>|||<PER_1> has <num>|271 fish (c)|40 in the|186 sister (c)|132 . <PER_2> has <num>|178 fish (c)|66 in the|21 sister (c)|22 . How many|107 fish (c)|45 are in the|3 sister (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.25

__start_noun0__ birds __end_noun0__ __start_noun1__ fence __end_noun1__ __start_noun2__ land __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> birds (c) in the land (c) . <PER_2> has <num> birds (c) in the land (c) . How many birds (c) are in the land (c) ? <eos>|||<PER_1> has <num>|271 birds (c)|40 in the|186 land (c)|132 . <PER_2> has <num>|178 birds (c)|66 in the|21 land (c)|22 . How many|107 birds (c)|45 are in the|3 land (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ miles __end_noun0__ __start_noun1__ hour __end_noun1__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> miles (c) in the hour (c) . <PER_2> has <num> miles (c) in the hour (c) . How many miles (c) are in the hour (c) ? <eos>|||<PER_1> has <num>|271 miles (c)|40 in the|186 hour (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 hour (c)|22 . How many|107 miles (c)|45 are in the|3 hour (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ CD __end_noun0__ __start_noun1__ rack __end_noun1__ __start_noun2__ CDs __end_noun2__ __start_noun3__ shelf __end_noun3__ __start_noun4__ racks __end_noun4__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> CD (c) in the CDs (c) . <PER_2> has <num> CD (c) in the CDs (c) . How many CD (c) are in the racks (c) ? <eos>|||<PER_1> has <num>|271 CD (c)|40 in the|186 CDs (c)|132 . <PER_2> has <num>|178 CD (c)|66 in the|21 CDs (c)|22 . How many|107 CD (c)|45 are in the|3 racks (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ eggs __end_noun0__ __start_noun1__ shares __end_noun1__ __start_noun2__ friends __end_noun2__ __start_noun3__ friend __end_noun3__ __start_noun4__ get __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> eggs (c) in the friends (c) . <PER_2> has <num> eggs (c) in the friends (c) . How many eggs (c) are in the get (c) ? <eos>|||<PER_1> has <num>|271 eggs (c)|40 in the|186 friends (c)|132 . <PER_2> has <num>|178 eggs (c)|66 in the|21 friends (c)|22 . How many|107 eggs (c)|45 are in the|3 get (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.33

__start_noun0__ bottle __end_noun0__ __start_noun1__ cap __end_noun1__ __start_noun2__ caps __end_noun2__ __start_noun3__ cost __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> bottle (c) in the caps (c) . <PER_2> has <num> bottle (c) in the caps (c) . How many bottle (c) are in the caps (c) ? <eos>|||<PER_1> has <num>|271 bottle (c)|40 in the|186 caps (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 caps (c)|22 . How many|107 bottle (c)|45 are in the|3 caps (c)|75 ? <eos>|139
a=-0.89 t=-0.62 g=-0.28

__start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> <MISC_1> in the _noun0 . <PER_2> has <num> _noun0 in the _noun0 . How many _noun0 are <num> _noun0 ? <eos>|||<PER_1> has <num>|271 <MISC_1>|40 in the|186 _noun0|132 . <PER_2> has <num>|178 _noun0|66 in the|21 _noun0|22 . How many|107 _noun0|45 are <num>|3 _noun0|75 ? <eos>|139
a=-1.03 t=-0.69 g=-0.34

__start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> <MISC_1> in the _noun0 . <PER_2> has <num> _noun0 in the _noun0 . How many _noun0 are the _noun0 ? <eos>|||<PER_1> has <num>|271 <MISC_1>|40 in the|186 _noun0|132 . <PER_2> has <num>|178 _noun0|66 in the|21 _noun0|22 . How many|107 _noun0|45 are the|3 _noun0|75 ? <eos>|139
a=-1.04 t=-0.69 g=-0.35

__start_noun0__ eggs __end_noun0__ __start_noun1__ box __end_noun1__ __start_noun2__ boxes __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> eggs (c) in the boxes (c) . <PER_2> has <num> eggs (c) in the boxes (c) . How many eggs (c) are in the boxes (c) ? <eos>|||<PER_1> has <num>|271 eggs (c)|40 in the|186 boxes (c)|132 . <PER_2> has <num>|178 eggs (c)|66 in the|21 boxes (c)|22 . How many|107 eggs (c)|45 are in the|3 boxes (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ cents __end_noun0__ __start_noun1__ candy __end_noun1__ __start_noun2__ gumdrop __end_noun2__ __start_noun3__ gumdrops __end_noun3__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> cents (c) in the gumdrop (c) . <PER_2> has <num> cents (c) in the gumdrop (c) . How many cents (c) are in the gumdrop (c) ? <eos>|||<PER_1> has <num>|271 cents (c)|40 in the|186 gumdrop (c)|132 . <PER_2> has <num>|178 cents (c)|66 in the|21 gumdrop (c)|22 . How many|107 cents (c)|45 are in the|3 gumdrop (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ candies __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> candies (c) in the candies (c) . <PER_2> has <num> candies (c) in the candies (c) . How many candies (c) are in the candies (c) ? <eos>|||<PER_1> has <num>|271 candies (c)|40 in the|186 candies (c)|132 . <PER_2> has <num>|178 candies (c)|66 in the|21 candies (c)|22 . How many|107 candies (c)|45 are in the|3 candies (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.24

__start_noun0__ dollars __end_noun0__ __start_noun1__ snake __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> dollars (c) in the snake (c) . <PER_2> has <num> dollars (c) in the snake (c) . How many dollars (c) are in the snake (c) ? <eos>|||<PER_1> has <num>|271 dollars (c)|40 in the|186 snake (c)|132 . <PER_2> has <num>|178 dollars (c)|66 in the|21 snake (c)|22 . How many|107 dollars (c)|45 are in the|3 snake (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ sister __end_noun0__ __start_noun1__ drove __end_noun1__ __start_noun2__ concert __end_noun2__ __start_noun3__ miles __end_noun3__ __start_noun4__ gas __end_noun4__ __start_noun5__ gallons __end_noun5__ __start_noun6__ car __end_noun6__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> sister (c) in the concert (c) . <PER_2> has <num> miles (c) in the concert (c) . How many miles (c) are in the concert (c) ? <eos>|||<PER_1> has <num>|271 sister (c)|40 in the|186 concert (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 concert (c)|22 . How many|107 miles (c)|45 are in the|3 concert (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.34

__start_noun0__ balloons __end_noun0__ __start_noun1__ mom __end_noun1__ __start_noun2__ birthday __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> balloons (c) in the birthday (c) . <PER_2> has <num> balloons (c) in the birthday (c) . How many balloons (c) are in the birthday (c) ? <eos>|||<PER_1> has <num>|271 balloons (c)|40 in the|186 birthday (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 birthday (c)|22 . How many|107 balloons (c)|45 are in the|3 birthday (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ cents __end_noun0__ __start_noun1__ candy __end_noun1__ __start_noun2__ piece __end_noun2__ __start_noun3__ costs __end_noun3__ __start_noun4__ gumdrops __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> cents (c) in the piece (c) . <PER_2> has <num> piece (c) in the piece (c) . How many piece (c) are in the piece (c) ? <eos>|||<PER_1> has <num>|271 cents (c)|40 in the|186 piece (c)|132 . <PER_2> has <num>|178 piece (c)|66 in the|21 piece (c)|22 . How many|107 piece (c)|45 are in the|3 piece (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ sheets __end_noun0__ __start_noun1__ paper __end_noun1__ __start_noun2__ pieces __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> sheets (c) in the paper (c) . <PER_2> has <num> pieces (c) in the paper (c) . How many pieces (c) are in the paper (c) ? <eos>|||<PER_1> has <num>|271 sheets (c)|40 in the|186 paper (c)|132 . <PER_2> has <num>|178 pieces (c)|66 in the|21 paper (c)|22 . How many|107 pieces (c)|45 are in the|3 paper (c)|75 ? <eos>|139
a=-0.92 t=-0.61 g=-0.30

__start_noun0__ mom __end_noun0__ __start_noun1__ cookies __end_noun1__ __start_noun2__ dad __end_noun2__ __start_noun3__ school __end_noun3__ __start_noun4__ party __end_noun4__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> mom (c) in the party (c) . <PER_2> has <num> cookies (c) in the party (c) . How many cookies (c) are in the party (c) ? <eos>|||<PER_1> has <num>|271 mom (c)|40 in the|186 party (c)|132 . <PER_2> has <num>|178 cookies (c)|66 in the|21 party (c)|22 . How many|107 cookies (c)|45 are in the|3 party (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.33

__start_noun0__ eggs __end_noun0__ __start_noun1__ jar __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> eggs (c) in the jar (c) . <PER_2> has <num> eggs (c) in the jar (c) . How many eggs (c) are in the jar (c) ? <eos>|||<PER_1> has <num>|271 eggs (c)|40 in the|186 jar (c)|132 . <PER_2> has <num>|178 eggs (c)|66 in the|21 jar (c)|22 . How many|107 eggs (c)|45 are in the|3 jar (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.23

__start_noun0__ baskets __end_noun0__ __start_noun1__ apples __end_noun1__ __start_noun2__ basket __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> baskets (c) in the basket (c) . <PER_2> has <num> apples (c) in the basket (c) . How many apples (c) are in the basket (c) ? <eos>|||<PER_1> has <num>|271 baskets (c)|40 in the|186 basket (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 basket (c)|22 . How many|107 apples (c)|45 are in the|3 basket (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ cupcakes __end_noun0__ __start_noun1__ children __end_noun1__ __start_noun2__ share __end_noun2__ __start_noun3__ person __end_noun3__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> cupcakes (c) in the share (c) . <PER_2> has <num> children (c) in the share (c) . How many cupcakes (c) are in the share (c) ? <eos>|||<PER_1> has <num>|271 cupcakes (c)|40 in the|186 share (c)|132 . <PER_2> has <num>|178 children (c)|66 in the|21 share (c)|22 . How many|107 cupcakes (c)|45 are in the|3 share (c)|75 ? <eos>|139
a=-0.96 t=-0.62 g=-0.34

__start_noun0__ boxes __end_noun0__ __start_noun1__ cases __end_noun1__ __start_noun2__ pickup __end_noun2__ __start_noun3__ cookie __end_noun3__ __start_noun4__ mom __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> boxes (c) in the pickup (c) . <PER_2> has <num> boxes (c) in the pickup (c) . How many boxes (c) are in the mom (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 pickup (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 pickup (c)|22 . How many|107 boxes (c)|45 are in the|3 mom (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ whistles __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> whistles (c) in the whistles (c) . <PER_2> has <num> whistles (c) in the whistles (c) . How many whistles (c) are the whistles (c) ? <eos>|||<PER_1> has <num>|271 whistles (c)|40 in the|186 whistles (c)|132 . <PER_2> has <num>|178 whistles (c)|66 in the|21 whistles (c)|22 . How many|107 whistles (c)|45 are the|3 whistles (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ s __end_noun0__ __start_noun1__ mom __end_noun1__ __start_noun2__ party __end_noun2__ __start_noun3__ balloons __end_noun3__ __start_noun4__ morning __end_noun4__ __start_noun5__ afternoon __end_noun5__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> mom (c) in the party (c) . <PER_2> has <num> balloons (c) in the party (c) . How many balloons (c) are in the balloons (c) ? <eos>|||<PER_1> has <num>|271 mom (c)|40 in the|186 party (c)|132 . <PER_2> has <num>|178 balloons (c)|66 in the|21 party (c)|22 . How many|107 balloons (c)|45 are in the|3 balloons (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ butterflies __end_noun0__ __start_noun1__ butterfly __end_noun1__ __start_noun2__ dots __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> butterflies (c) in the dots (c) . <PER_2> has <num> butterflies (c) in the dots (c) . How many butterflies (c) are in the dots (c) ? <eos>|||<PER_1> has <num>|271 butterflies (c)|40 in the|186 dots (c)|132 . <PER_2> has <num>|178 butterflies (c)|66 in the|21 dots (c)|22 . How many|107 butterflies (c)|45 are in the|3 dots (c)|75 ? <eos>|139
a=-0.94 t=-0.61 g=-0.33

__start_noun0__ feet __end_noun0__ __start_noun1__ cotton __end_noun1__ __start_noun2__ tee-shirt __end_noun2__ __start_noun3__ tee-shirts __end_noun3__ __start_noun4__ material __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> feet (c) in the tee-shirt (c) . <PER_2> has <num> feet (c) in the tee-shirt (c) . How many material (c) are in the material (c) ? <eos>|||<PER_1> has <num>|271 feet (c)|40 in the|186 tee-shirt (c)|132 . <PER_2> has <num>|178 feet (c)|66 in the|21 tee-shirt (c)|22 . How many|107 material (c)|45 are in the|3 material (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.36

__start_noun0__ bottle __end_noun0__ __start_noun1__ caps __end_noun1__ __start_noun2__ jar __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> bottle (c) in the caps (c) . <PER_2> has <num> bottle (c) in the caps (c) . How many bottle (c) are in the caps (c) ? <eos>|||<PER_1> has <num>|271 bottle (c)|40 in the|186 caps (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 caps (c)|22 . How many|107 bottle (c)|45 are in the|3 caps (c)|75 ? <eos>|139
a=-0.88 t=-0.61 g=-0.27

__start_noun0__ hair __end_noun0__ __start_noun1__ inches __end_noun1__ __start_noun2__ haircut __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> hair (c) in the haircut (c) . <PER_2> has <num> hair (c) in the haircut (c) . How many hair (c) are in the haircut (c) ? <eos>|||<PER_1> has <num>|271 hair (c)|40 in the|186 haircut (c)|132 . <PER_2> has <num>|178 hair (c)|66 in the|21 haircut (c)|22 . How many|107 hair (c)|45 are in the|3 haircut (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ bee __end_noun0__ __start_noun1__ legs __end_noun1__ __start_noun2__ bees __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> bee (c) in the legs (c) . <PER_2> has <num> legs (c) in the legs (c) . How many legs (c) are in the legs (c) ? <eos>|||<PER_1> has <num>|271 bee (c)|40 in the|186 legs (c)|132 . <PER_2> has <num>|178 legs (c)|66 in the|21 legs (c)|22 . How many|107 legs (c)|45 are in the|3 legs (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ store __end_noun0__ __start_noun1__ times __end_noun1__ __start_noun2__ month __end_noun2__ __start_noun3__ peanuts __end_noun3__ __start_noun4__ time __end_noun4__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> store (c) in the month (c) . <PER_2> has <num> peanuts (c) in the month (c) . How many peanuts (c) are in the month (c) ? <eos>|||<PER_1> has <num>|271 store (c)|40 in the|186 month (c)|132 . <PER_2> has <num>|178 peanuts (c)|66 in the|21 month (c)|22 . How many|107 peanuts (c)|45 are in the|3 month (c)|75 ? <eos>|139
a=-0.89 t=-0.62 g=-0.27

__start_noun0__ bananas __end_noun0__ __start_noun1__ cards __end_noun1__ __start_noun2__ store __end_noun2__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> bananas (c) in the store (c) . <PER_2> has <num> bananas (c) in the store (c) . How many bananas (c) are in the store (c) ? <eos>|||<PER_1> has <num>|271 bananas (c)|40 in the|186 store (c)|132 . <PER_2> has <num>|178 bananas (c)|66 in the|21 store (c)|22 . How many|107 bananas (c)|45 are in the|3 store (c)|75 ? <eos>|139
a=-0.91 t=-0.61 g=-0.30

__start_noun0__ blocks __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> blocks (c) in the blocks (c) . <PER_2> has <num> blocks (c) in the blocks (c) . How many blocks (c) are in the blocks (c) ? <eos>|||<PER_1> has <num>|271 blocks (c)|40 in the|186 blocks (c)|132 . <PER_2> has <num>|178 blocks (c)|66 in the|21 blocks (c)|22 . How many|107 blocks (c)|45 are in the|3 blocks (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.25

__start_noun0__ hours __end_noun0__ __start_noun1__ house __end_noun1__ __start_noun2__ miles __end_noun2__ __start_noun3__ hour __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> hours (c) in the house (c) . <PER_2> has <num> miles (c) in the house (c) . How many miles (c) are in the house (c) ? <eos>|||<PER_1> has <num>|271 hours (c)|40 in the|186 house (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 house (c)|22 . How many|107 miles (c)|45 are in the|3 house (c)|75 ? <eos>|139
a=-0.91 t=-0.62 g=-0.30

__start_noun0__ boxes __end_noun0__ __start_noun1__ cases __end_noun1__ __start_noun2__ pickup __end_noun2__ __start_noun3__ cookie __end_noun3__ __start_noun4__ mom __end_noun4__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> boxes (c) in the pickup (c) . <PER_2> has <num> boxes (c) in the pickup (c) . How many boxes (c) are in the mom (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 pickup (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 pickup (c)|22 . How many|107 boxes (c)|45 are in the|3 mom (c)|75 ? <eos>|139
a=-0.97 t=-0.62 g=-0.35

__start_noun0__ pencils __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> pencils (c) in the pencils (c) . <PER_2> has <num> pencils (c) in the pencils (c) . How many pencils (c) are in the pencils (c) ? <eos>|||<PER_1> has <num>|271 pencils (c)|40 in the|186 pencils (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 pencils (c)|22 . How many|107 pencils (c)|45 are in the|3 pencils (c)|75 ? <eos>|139
a=-0.94 t=-0.67 g=-0.27

__start_noun0__ books __end_noun0__ __start_noun1__ shelf __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> books (c) in the shelf (c) . <PER_2> has <num> books (c) in the shelf (c) . How many books (c) are in the shelf (c) ? <eos>|||<PER_1> has <num>|271 books (c)|40 in the|186 shelf (c)|132 . <PER_2> has <num>|178 books (c)|66 in the|21 shelf (c)|22 . How many|107 books (c)|45 are in the|3 shelf (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ boxes __end_noun0__ __start_noun1__ apples __end_noun1__ __start_noun2__ box __end_noun2__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> boxes (c) in the box (c) . <PER_2> has <num> apples (c) in the box (c) . How many apples (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 box (c)|22 . How many|107 apples (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ miles __end_noun0__ __start_noun1__ hour __end_noun1__ __start_noun2__ wander __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> miles (c) in the wander (c) . <PER_2> has <num> miles (c) in the wander (c) . How many miles (c) are in the wander (c) ? <eos>|||<PER_1> has <num>|271 miles (c)|40 in the|186 wander (c)|132 . <PER_2> has <num>|178 miles (c)|66 in the|21 wander (c)|22 . How many|107 miles (c)|45 are in the|3 wander (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.28

__start_noun0__ pounds __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> pounds (c) in the pounds (c) . <PER_2> has <num> pounds (c) in the pounds (c) . How many pounds (c) are the pounds (c) ? <eos>|||<PER_1> has <num>|271 pounds (c)|40 in the|186 pounds (c)|132 . <PER_2> has <num>|178 pounds (c)|66 in the|21 pounds (c)|22 . How many|107 pounds (c)|45 are the|3 pounds (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.25

__start_noun0__ boxes __end_noun0__ __start_noun1__ cases __end_noun1__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> boxes (c) in the cases (c) . <PER_2> has <num> boxes (c) in the cases (c) . How many boxes (c) are in the cases (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 cases (c)|132 . <PER_2> has <num>|178 boxes (c)|66 in the|21 cases (c)|22 . How many|107 boxes (c)|45 are in the|3 cases (c)|75 ? <eos>|139
a=-0.87 t=-0.62 g=-0.25

__start_noun0__ cost __end_noun0__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> cost (c) in the cost (c) . <PER_2> has <num> cost (c) in the cost (c) . How many cost (c) are in the cost (c) ? <eos>|||<PER_1> has <num>|271 cost (c)|40 in the|186 cost (c)|132 . <PER_2> has <num>|178 cost (c)|66 in the|21 cost (c)|22 . How many|107 cost (c)|45 are in the|3 cost (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.23

__start_noun0__ candies __end_noun0__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> candies (c) in the candies (c) . <PER_2> has <num> candies (c) in the candies (c) . How many candies (c) are the candies (c) ? <eos>|||<PER_1> has <num>|271 candies (c)|40 in the|186 candies (c)|132 . <PER_2> has <num>|178 candies (c)|66 in the|21 candies (c)|22 . How many|107 candies (c)|45 are the|3 candies (c)|75 ? <eos>|139
a=-0.91 t=-0.67 g=-0.24

__start_noun0__ garden __end_noun0__ __start_noun1__ rows __end_noun1__ __start_noun2__ columns __end_noun2__ __start_noun3__ plans __end_noun3__ __start_noun4__ plants __end_noun4__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> garden (c) in the columns (c) . <PER_2> has <num> plants (c) in the columns (c) . How many plants (c) are in the plants (c) ? <eos>|||<PER_1> has <num>|271 garden (c)|40 in the|186 columns (c)|132 . <PER_2> has <num>|178 plants (c)|66 in the|21 columns (c)|22 . How many|107 plants (c)|45 are in the|3 plants (c)|75 ? <eos>|139
a=-0.95 t=-0.62 g=-0.34

__start_noun0__ students __end_noun0__ __start_noun1__ class __end_noun1__ __start_noun2__ pencils __end_noun2__ __start_noun3__ student __end_noun3__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> students (c) in the class (c) . <PER_2> has <num> pencils (c) in the class (c) . How many pencils (c) are in the pencils (c) ? <eos>|||<PER_1> has <num>|271 students (c)|40 in the|186 class (c)|132 . <PER_2> has <num>|178 pencils (c)|66 in the|21 class (c)|22 . How many|107 pencils (c)|45 are in the|3 pencils (c)|75 ? <eos>|139
a=-0.92 t=-0.62 g=-0.31

__start_noun0__ peanuts __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> peanuts (c) in the peanuts (c) . <PER_2> has <num> peanuts (c) in the peanuts (c) . How many peanuts (c) are in the peanuts (c) ? <eos>|||<PER_1> has <num>|271 peanuts (c)|40 in the|186 peanuts (c)|132 . <PER_2> has <num>|178 peanuts (c)|66 in the|21 peanuts (c)|22 . How many|107 peanuts (c)|45 are in the|3 peanuts (c)|75 ? <eos>|139
a=-0.92 t=-0.67 g=-0.25

__start_noun0__ marbles __end_noun0__ __start_noun1__ oranges __end_noun1__ __start_noun2__ shares __end_noun2__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> marbles (c) in the shares (c) . <PER_2> has <num> oranges (c) in the shares (c) . How many oranges (c) are in the shares (c) ? <eos>|||<PER_1> has <num>|271 marbles (c)|40 in the|186 shares (c)|132 . <PER_2> has <num>|178 oranges (c)|66 in the|21 shares (c)|22 . How many|107 oranges (c)|45 are in the|3 shares (c)|75 ? <eos>|139
a=-0.89 t=-0.61 g=-0.28

__start_noun0__ boxes __end_noun0__ __start_noun1__ erasers __end_noun1__ __start_noun2__ box __end_noun2__ __start_noun3__ case __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> boxes (c) in the box (c) . <PER_2> has <num> erasers (c) in the box (c) . How many boxes (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 boxes (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 erasers (c)|66 in the|21 box (c)|22 . How many|107 boxes (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.94 t=-0.62 g=-0.32

__start_noun0__ Clarence __end_noun0__ __start_noun1__ tickets __end_noun1__ __start_solution_type__ Subtraction __end_solution_type__

<PER_1> has <num> Clarence (c) in the tickets (c) . <PER_2> has <num> tickets (c) in the tickets (c) . How many tickets (c) are in the tickets (c) ? <eos>|||<PER_1> has <num>|271 Clarence (c)|40 in the|186 tickets (c)|132 . <PER_2> has <num>|178 tickets (c)|66 in the|21 tickets (c)|22 . How many|107 tickets (c)|45 are in the|3 tickets (c)|75 ? <eos>|139
a=-0.86 t=-0.62 g=-0.24

__start_noun0__ bottle __end_noun0__ __start_noun1__ caps __end_noun1__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> bottle (c) in the caps (c) . <PER_2> has <num> bottle (c) in the caps (c) . How many bottle (c) are in the caps (c) ? <eos>|||<PER_1> has <num>|271 bottle (c)|40 in the|186 caps (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 caps (c)|22 . How many|107 bottle (c)|45 are in the|3 caps (c)|75 ? <eos>|139
a=-0.85 t=-0.62 g=-0.24

__start_noun0__ oranges __end_noun0__ __start_noun1__ boxes __end_noun1__ __start_noun2__ box __end_noun2__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> oranges (c) in the box (c) . <PER_2> has <num> oranges (c) in the box (c) . How many oranges (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 oranges (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 oranges (c)|66 in the|21 box (c)|22 . How many|107 oranges (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.90 t=-0.61 g=-0.29

__start_noun0__ caps __end_noun0__ __start_noun1__ box __end_noun1__ __start_noun2__ bottle __end_noun2__ __start_noun3__ boxes __end_noun3__ __start_solution_type__ Multiplication __end_solution_type__

<PER_1> has <num> caps (c) in the box (c) . <PER_2> has <num> bottle (c) in the box (c) . How many bottle (c) are in the box (c) ? <eos>|||<PER_1> has <num>|271 caps (c)|40 in the|186 box (c)|132 . <PER_2> has <num>|178 bottle (c)|66 in the|21 box (c)|22 . How many|107 bottle (c)|45 are in the|3 box (c)|75 ? <eos>|139
a=-0.93 t=-0.62 g=-0.32

__start_noun0__ friends __end_noun0__ __start_noun1__ party __end_noun1__ __start_noun2__ cookies __end_noun2__ __start_noun3__ get __end_noun3__ __start_solution_type__ CommonDiv __end_solution_type__

<PER_1> has <num> friends (c) in the party (c) . <PER_2> has <num> cookies (c) in the party (c) . How many cookies (c) are in the cookies (c) ? <eos>|||<PER_1> has <num>|271 friends (c)|40 in the|186 party (c)|132 . <PER_2> has <num>|178 cookies (c)|66 in the|21 party (c)|22 . How many|107 cookies (c)|45 are in the|3 cookies (c)|75 ? <eos>|139
a=-0.90 t=-0.62 g=-0.29

__start_noun0__ apples __end_noun0__ __start_solution_type__ Addition __end_solution_type__

<PER_1> has <num> apples (c) in the apples (c) . <PER_2> has <num> apples (c) in the apples (c) . How many apples (c) are in the apples (c) ? <eos>|||<PER_1> has <num>|271 apples (c)|40 in the|186 apples (c)|132 . <PER_2> has <num>|178 apples (c)|66 in the|21 apples (c)|22 . How many|107 apples (c)|45 are in the|3 apples (c)|75 ? <eos>|139
a=-0.94 t=-0.67 g=-0.27

