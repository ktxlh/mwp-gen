Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated', gen_fi='', pure='', tagged_fi='segs/seg-srl-ai2-ilds-300-35-5-far.txt')
# Analysis of segmentation
metadata_path=/home/shangling/Datasets/srl-ai2-ilds-train-valid/ai2-ilds-train-valid-concated/metadata_train.tsv
seg_path=segs/seg-srl-ai2-ilds-300-35-5-far.txt
k=100
n=10
# Overall - top templates
### Top-1 (111 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | grew | <num> | pumpkins | , but | the | <unk> | ate | <num> | pumpkins | . How many | pumpkins | does | <PER_1> | have | ? <eos> | Subtraction | ai2 |
| <PER_1> | baked | <num> | muffins | . How many more | muffins | does | <PER_1> | have | to | bake | to | have | <num> | muffins | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . | <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | cards | . | <num> | are | eaten | by a | hippopotamus | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | dollars | . How many more | dollars | does | she | have | to | <unk> | to | have | <num> | dollars | ? <eos> | Subtraction | ilds |
| <PER_1> | baked | <num> | muffins | . <PER_2> | baked | <num> | times | as | many | . How many | muffins | did | <PER_2> | bake | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | crayons | . | <num> | are | eaten | by a | hippopotamus | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | blocks | . | <num> | are | eaten | by a | hippopotamus | . How many | blocks | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | dogs | . Each | dog | had | <num> | puppies | . How many | puppies | does | <PER_1> | now | have | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | fish | . How many more | fish | does | she | need | to | buy | to | have | <num> | fish | ? <eos> | Subtraction | ilds |

### Top-2 (99 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | strolled | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | fly | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | cards | . She | loses | <num> | . How many | cards | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | strolled | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | stroll | ? <eos> | CommonDiv | ilds |
| <PER_1> | wandered | <num> | kilometers | at <num> | kilometers | per | hour | . How long | did | <PER_1> | <unk> | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | marbles | . She | loses | <num> | . How many | marbles | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | wandered | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | found | <num> | seashells | but <num> | were | <unk> | . How many <unk> | seashells | did | <PER_1> | find | ? <eos> | SubtractionTimeVariantUnknownFinal | ai2 |

### Top-3 (69 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | minutes | to | bake one | <unk> | of cookies | . How long | will | it | take | to | bake | <num> | <unk> | of | cookies | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | balloons | . <num> | balloons | are | red | and the | rest | are | green | . How many | green | balloons | does | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | crayons | . <PER_2> | has | <num> | crayons | . She | shares | <num> | with | <PER_3> | . How many | crayons | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | has | <num> | apples | . He | shares | <num> | with | <PER_3> | . How many | apples | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | guests | <unk> | to his | party | . Each | table | will | hold | <num> | guests | . How many | <unk> | will | he | need | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> | of <PER_1> | <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | baseball | cards | . <PER_2> | bought | <num> | of <PER_1> | <PER_3> | baseball | cards | . How many | baseball | cards | does | <PER_1> | have | now ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | dimes | in his | bank | . His | sister | borrowed | <num> | of | his | dimes | . How many | dimes | does | <PER_1> | have | now ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | books | , <PER_2> | has | <num> | books | , | and <PER_3> | has | <num> | books | . How many | books | do | they | have | together ? <eos> | Sum | ai2 |
| A | restaurant made | <num> | hamburgers | to | serve | during | lunch | . <unk> | <num> | were | <unk> | served | . How many | hamburgers | were | over from | lunch | ? <eos> | Subtraction | ai2 |

### Top-4 (51 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | wants | to | split | a | collection | of | crayons | into | groups | of | <num> | . <PER_1> | has | <num> | crayons | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | <unk> | for the | <unk> | team | and | ran | <num> | laps | per | <unk> | . How many | minutes | did | it | take | <PER_1> | to | run | <num> | laps | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | erasers | into | groups | of | <num> | . <PER_1> | has | <num> | erasers | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | wants | to | split | a | collection | of | peanuts | into | groups | of | <num> | . <PER_1> | has | <num> | peanuts | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | made | cookies | . She | used | <num> | cup | of | flour | and <num> | cup | of | sugar | . How much | more | flour | than | sugar | did | <PER_1> | use | ? <eos> | Subtraction | ai2 |
| <PER_1> | <unk> | <num> | people | to her | birthday | party | . They | each | ate | <num> | pieces | of | pizza | . How many | pieces | of | pizza | did | they | eat | ? <eos> | Multiplication | ilds |
| I | have | a | pet <unk> | <unk> | . Each | year | he | <unk> | <num> | pounds | . He | is | <num> | <unk> | old | . How many | pounds | does | he | weigh | ? <eos> | Multiplication | ilds |
| <PER_1> | wants | to | split | a | collection | of | bottle | caps | into groups | of <num> | . <PER_1> | has | <num> | bottle | caps | . How many | groups | will | be | created | ? <eos> | CommonDiv | ilds |
| <PER_1> | had | <num> | grams | of | <unk> | . Then he | used | <num> | grams | of the | <unk> | to | make | some <unk> | eggs | . How much | <unk> | does | <PER_1> | have | ? <eos> | Subtraction | ai2 |
| <ORG_1> | has | <num> | boxes | of tickets | . Each | box | holds | <num> | tickets | and there | are | <num> | boxes | in a | <unk> | . How many | tickets | does | <ORG_1> | have | ? <eos> | Multiplication | ilds |

### Top-5 (40 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| It | takes | <num> | apples | to make | <num> | pie | . How many | apples | does | it | take | to | make | <num> | pies | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | bottle | caps | . <num> | are | eaten | by a | hippopotamus | . How many | bottle | caps | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <unk> | sticks | . I | have | <num> | <unk> | sticks | . What | is the | <unk> | of <unk> | <unk> | sticks | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | cents | . He | paid | <num> | cents | for a | candy | <unk> | . How much | <unk> | will | he | get | ? <eos> | Subtraction | ilds |
| <PER_1> | ate | <num> | <unk> | sticks | before | dinner | and <num> more | after | dinner | . How many | <unk> | sticks | did | he | eat | ? <eos> | Addition | ilds |
| <PER_1> | bought | <num> | ounces | of | sugar | , and she | <unk> | <num> | ounces | of | it | on the | <unk> | . How much | is | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | seashells | . How many more | seashells | does | she | need | to | find | to have | <num> | seashells | in her | collection | ? <eos> | Subtraction | ilds |
| You | have | <num> | cookies | and <unk> | to | share | them | equally with <num> | people | . How many | cookies | would | each | <unk> | get | ? <eos> | CommonDiv | ilds |
| <PER_1> <PER_2> | car gets | <num> | miles | per | gallon | of | gas | . How far | can | she | drive | on <num> | gallons | of | gas | ? <eos> | Multiplication | ilds |
| <PER_1> | is <unk> | <num> | friends | to a | party | . He | has | <num> | cookies | . How many | cookies | will | each | friend | get | ? <eos> | CommonDiv | ilds |

### Top-6 (34 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | needs | to | read | a | <num> | <unk> | book | for | school | . He | has | already | read | <num> | pages | . How many | pages | does | he | have | left | to | read | ? <eos> | Subtraction | ilds |
| Mrs. <PER_1> | <unk> | <num> | ounces | of <unk> | to | <unk> | a | pound | of | clothes | . How many | ounces | of | <unk> | will | she | use | to | <unk> | <num> | pounds | of | clothes | ? <eos> | Multiplication | ilds |
| <PER_1> | has | <num> | apples | . <PER_2> | gave | her | <num> more | . She | needs | <num> | apples | to | make | a | pie | . <unk> | she | have | <unk> | to | make | a | pie | ? <eos> | Addition | ilds |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |
| The | school | is | <unk> | a | <unk> | trip | . There | are | <num> | students | and <num> | seats | on each | school | bus | . How many | <unk> | are | needed | to | take | the | trip | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | old | , brown | <unk> | of | <unk> | paper | and <num> | old | , yellow | <unk> | of | <unk> | paper | . How many | pieces | of | <unk> | paper | does | she | have | ? <eos> | Addition | ilds |
| <PER_1> | drove | <num> | miles | to | <unk> his | grandmother | . <PER_2> | drove | <num> | miles | to | <unk> | her | grandmother | . What | is | the total | number | of | miles | <PER_1> | and <PER_2> | drove | ? <eos> | Addition | ilds |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | <unk> | long | . Then she | <unk> | <num> | <unk> | off the | end | . How long | is | the | piece | of | wood | now ? <eos> | Subtraction | ai2 |
| A | <unk> | bought | a | piece | of | wood | that | was | <num> | centimeters | long | . Then he | <unk> | <num> | centimeters | off the | end | . How long | is | the | piece | of | wood | now ? <eos> | Subtraction | ai2 |
| I | walked | <num> | miles | in <num> | hour | for <MISC_1> | <MISC_2> | <MISC_3> | . If I | <unk> | this | <unk> | for the | <num> | hours | I | walk | , how many | miles | total | will | I | walk | ? <eos> | Multiplication | ilds |

### Top-7 (32 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | <unk> | . She | wants | to | give | each | <unk> | <num> | pieces | of | gum | . How much | gum | will | she | need | ? <eos> | Multiplication | ilds |
| <PER_1> | bought | <num> | pounds | of | fruit | for a | class | party | . The | class | ate | <num> | pounds | of the | fruit | . How much | fruit | is | ? <eos> | Subtraction | ai2 |
| <num> | ducks | are | <unk> | in a | lake | . <num> | more | ducks | come | to | join | them | . How many | ducks | are | <unk> | in the | lake | ? <eos> | Addition | ilds |
| <PER_1> | has | <num> | marbles | and <num> | blocks | . If he | shares | the | marbles | among | <num> | friends | , how many | marbles | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| If <PER_1> | split | <num> | apples | between <num> | people | in her | class | and | <unk> | the | left | <unk> | , how many | apples | did | each | <unk> | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | bought | <num> | pieces | of | paper | . She | used | <num> | pieces | of the | paper | . How many | pieces | of paper | does | she | have | left | ? <eos> | Subtraction | ilds |
| <LOC_1> | has | <num> | eggs | and <num> | <MISC_1> | . If she | shares | the | eggs | among | <num> | friends | , how many | eggs | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | candies | and <num> | bananas | . If she | shares | the | candies | among | <num> | friends | , how many | candies | does | each | friend | get | ? <eos> | CommonDiv | ilds |
| <num> | birds | were | sitting | on the | fence | . <num> | more | birds | <unk> | to | join | them | . How many | birds | are | sitting | on the | fence | ? <eos> | Addition | ilds |
| <PER_1> | had | <num> | packages | of | <unk> | . There | are | <num> | <unk> | in each | package | . She | ate | <num> | <unk> | . How many | are | left | ? <eos> | Multiplication | ilds |

### Top-8 (28 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | <unk> | . Each | <unk> | has | <num> | fish | . How many | fish | are | there | ? <eos> | Multiplication | ilds |
| <PER_1> | drove | <num> | miles | every | hour | . How many | miles | would | he | drive | in <num> | hours | ? <eos> | Multiplication | ilds |
| There | are | <num> | flowers | and <num> | bees | . How many | <unk> | bees | are | there | than | flowers | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | marbles | . He | gave | <num> | to <PER_2> | . How many | does | he | have | left | ? <eos> | Subtraction | ilds |
| <PER_1> | scored | <num> | points | in each | game | . How many | points | did | she | score | in <num> | games | ? <eos> | Multiplication | ilds |
| Each | bag <unk> | <num> | pounds | of | oranges | . How many | pounds | of | oranges | are | in <num> | bags | ? <eos> | Multiplication | ilds |
| There | are | <num> | eggs | in a | box | . <PER_1> | takes | <num> | eggs | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | oranges | in a | box | . <PER_1> | takes | <num> | oranges | . How many | are | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | pencils | in a | box | . <PER_1> | takes | <num> | pencils | . How many | are | left | ? <eos> | Subtraction | ilds |

### Top-9 (24 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | <unk> | <num> | dollars | for the | pie | , | <PER_1> | has | <num> | dollars | , her | friend | has | <num> | dollars | . How much | money | did | she | have | before | <unk> | the | pie | ? <eos> | Addition | ai2 |
| A | <unk> | <unk> | <unk> | <unk> | the | <unk> | . It | <unk> | <num> | acres | of the | <unk> | in <unk> | , but | leaves | <num> | acres | <unk> | . How many | acres | does | the | <unk> | <unk> | ? <eos> | Subtraction | ai2 |
| While | <unk> | a | video | game | , <PER_1> | scored | <num> | points | . He | and his | <unk> | together | have | a | total | of | <num> | points | . How many | points | does | <PER_1> 's | <unk> | have | ? <eos> | Subtraction | ai2 |
| At a | pie | - | <unk> | <unk> | , <PER_1> | got | <unk> | <num> | pie | before | time | was | called | <unk> <PER_2> | finished | <unk> | <num> | pie | . How much more | pie | did | <PER_1> | eat | than <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | filled | a | bucket | with <num> | gallon | of | water | . A <unk> | minutes | <unk> | , she | <unk> | <unk> | <num> | gallon | of | water | <unk> | . How much | water | had | leaked | out of the | bucket | ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | peaches | at her | <unk> | fruit | dish | . She | went | to the | orchard | and | picked | peaches | to | <unk> | up . There | are | now <num> | peaches | . how many | did | she | pick | ? <eos> | Subtraction | ai2 |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out | of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |
| <PER_1> | collects | baseball | cards | . She | had | <num> | cards | . She | gave | some | of her | cards | to <PER_2> | and now | has | <num> | cards | left | . How many | cards | did | <PER_1> | give | to <PER_2> | ? <eos> | Subtraction | ilds |
| There | are | <num> | candies | in a | box | . <PER_1> | has | <num> | candies | in a | bag | . <PER_2> | takes | <num> | candies | out | of the | box | . How many | candies | are | left | in the | box | ? <eos> | Subtraction | ilds |
| There | are | <num> | erasers | in a | box | . <PER_1> | has | <num> | erasers | in a | bag | . <PER_2> | takes | <num> | erasers | out | of the | box | . How many | erasers | are | left | in the | box | ? <eos> | Subtraction | ilds |

### Top-10 (23 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | scored | <num> | <unk> | <unk> | soccer | last | season | . This | season | he | scored | <num> | <unk> | . What | is | the total | number | of | <unk> | <PER_1> | scored | ? <eos> | Addition | ilds |
| It | takes | <num> | feet | of <unk> | to | make | a | <unk> | - | shirt | . How many | <unk> | - | shirts | can | be | made | with <num> | feet | of | material | ? <eos> | CommonDiv | ilds |
| A | restaurant served | <num> hot | dogs | during | lunch | and <num> | during | dinner | today | . It | served | <num> | of | them | yesterday | . How many | hot | dogs | were | served | today | ? <eos> | Addition | ai2 |
| <unk> | watermelons | have | <num> | seeds | each | . If <unk> | have | <num> | watermelons | , how many | seeds | <unk> | there | be | when all | seeds | are | <unk> | out | of the | watermelons | ? <eos> | Multiplication | ilds |
| <PER_1> | found | <num> | seashells | on the | beach | . she | gave | <PER_2> | some | of her | seashells | . She | has | <num> | seashell | . How many | seashells | did | she | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| <PER_1> | found | <num> | seashells | on the | beach | , he | gave | <PER_2> | some | of his | seashells | . He | has | <num> | seashell | . How many | seashells | did | he | give | to <PER_2> | ? <eos> | Subtraction | ai2 |
| Mrs. <PER_1> | <unk> | <num> | bees | in the | <unk> | . The | next | day | she | <unk> | <num> | times | that | many . How many | bees | did | she | <unk> | on the | second | day | ? <eos> | Multiplication | ilds |
| <unk> | heads | come | in packages | of | <num> | . <PER_1> | ate | <num> <MISC_1> | <MISC_2> | . How many | whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |
| There | are | <num> | people | on the | <LOC_1> <LOC_2> <LOC_3> | <unk> | team | . If a | <unk> | <unk> | is | <num> | <unk> | long , how far | will | each | team | <unk> | have | to | run | ? <eos> | CommonDiv | ilds |
| <unk> | heads | come | in packages | of | <num> | . <PER_1> | ate | <num> <MISC_1> | <MISC_2> | . How many | whole | boxes | did | he | eat | and how many | <MISC_1> <MISC_2> | does | he | have | left | ? <eos> | CommonDiv | ilds |

### Top-11 (19 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| I | have | <num> | cents | to | buy | candy | . If each | <unk> | costs | <num> | cents | , how many | <unk> | can | I | buy | ? <eos> | CommonDiv | ilds |
| <PER_1> | bought | <num> | pounds | of | peanuts | and <num> | pounds | of | raisins | . How many | pounds | of | <unk> | did | she | buy | in all ? <eos> | Addition | ai2 |
| <PER_1> | had | <num> | <unk> | and <PER_2> | had | <num> | <unk> | . If they | put | their | <unk> | together | , how many | would | they | have | ? <eos> | Addition | ilds |
| <PER_1> | sold | <num> | boxes | of <MISC_1> | . How many | cases | of | <num> | boxes | , plus extra | boxes | does | <PER_1> | need | to | <unk> | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | <MISC_1> | games | . How many | does | she | need | to | give | away so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |
| <PER_1> | has | <num> | <MISC_1> | games | . How many | does | she | need | to | give | away so that she | will | have | <num> | games | left | ? <eos> | Subtraction | ilds |
| There | are | <num> | pencils | and <num> rulers | in the | drawer | . <PER_1> | took | <num> | pencils | out of the | drawer | . How many | pencils | are | there | now ? <eos> | Subtraction | ai2 |
| <PER_1> | had | <num> | <unk> | on her birthday | cake | . She | grew | <unk> and | got | <num> more | on her | birthday | cake | . How old | is | <PER_1> | now ? <eos> | Addition | ilds |
| A <unk> | book holds | <num> | DVDs | . There | are | <num> | DVDs | already in the | book | . How many more | DVDs | can | be | put | in the | book | ? <eos> | Subtraction | ilds |
| Mrs. <PER_1> | bought | a | <unk> | for <num> | cents | and a | <unk> | for <num> | cents | . How much | did | she | spend | in all for the | two | toys | ? <eos> | Addition | ilds |

### Top-12 (17 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | class | is | <unk> | a | pizza | party | . You | buy | <num> | pizzas | . Each | pizza | has | <num> | slices | . How many | slices | is | that | altogether ? <eos> | Multiplication | ilds |
| <PER_1> | had | some | marbles | . She | gave | <num> | to | <PER_2> | . Now she | has | <num> | marbles | left | . How many | did | she | have | to | start | with ? <eos> | Addition | ilds |
| <PER_1> | picked | <num> | plums | , <PER_2> | picked | <num> | plums | , | and <PER_3> | picked | <num> | plums | from the | <unk> | tree | . How many | plums | were | picked | in total ? <eos> | Sum | ai2 |
| <PER_1> | went | to <num> | football | games | this | year | . He | went | to <num> | games | last | year | . How many | football | games | did | <PER_1> | go | to | in all ? <eos> | Addition | ai2 |
| <PER_1> | made | an | apple | pie | . She | used | <num> | <unk> | of | <unk> | and <num> | <unk> | of | <unk> | . How much more | <unk> | than <unk> | did | <PER_1> | use ? <eos> | Subtraction | ai2 |
| <PER_1> | made | a | <unk> | with <num> | blocks | . He | added | some more | blocks | and now he | has | <num> | blocks | . How many | did | he | have | to | add | ? <eos> | Subtraction | ilds |
| <PER_1> | had | <num> | flowers | . <PER_2> | gave | her | some more | flowers | . Now , <PER_1> | has | <num> | flowers | . How many | flowers | did | <PER_2> | give | to | <PER_1> | ? <eos> | Subtraction | ilds |
| <PER_1> 's | dog | had | puppies | . She | gave | <num> | to her | friends | . She | now has | <num> | puppies | . How many | puppies | did | she | have | to | start | with ? <eos> | Addition | ai2 |
| There | are | <num> | <unk> | in the | barn | . Some more | come | to | join | them | . Now there | are | <num> | <unk> | . How many | <unk> | <unk> | to | join | them ? <eos> | Subtraction | ilds |
| <PER_1> | had | some | noodles | . He | gave | <num> | noodles | to <PER_2> | . Now <PER_1> <unk> | has | <num> | noodles | . How many | noodles | did | <PER_1> | have | to | <unk> | with ? <eos> | Addition | ilds |

### Top-13 (15 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | found | <num> | <unk> | in the | yard | and measured | them | with a | <unk> | . <num> | <unk> | was | <num> | inch | long | . The <unk> | <unk> | was | <num> | inch | long | . How much | longer | was | the | longer | <unk> | ? <eos> | Subtraction | ai2 |
| Mrs. <PER_1> | wants | to | make | a | <unk> <unk> her | garden | . She | needs | <num> | <unk> | to | <unk> | the | <unk> | . She | has | <num> | <unk> | . How many more | <unk> | does | she | need | to | <unk> | the | <unk> | ? <eos> | Subtraction | ilds |
| You | are | <unk> a | book | with <num> | pages | . If you | <unk> | to | read | the same | number | of | pages | each | night | , how many | would | you | have | to | read | each | night | to | <unk> | in <num> | days | ? <eos> | CommonDiv | ilds |
| <num> | students | are | <unk> | to the | <unk> | . They | have | to | be | divided | into groups | so that | each | <unk> | has | one | group | . There | are | <num> | <unk> | . How many | students | will | be | in each | group | ? <eos> | CommonDiv | ilds |
| <PER_1> | bought | <num> <unk> | <unk> | . She | has | <num> | children | . She | would | <unk> | to | <unk> | the | <unk> | among her | children | so that each | child | gets | the same | <unk> | . How many | <unk> | would | each | child | get | ? <eos> | CommonDiv | ilds |
| <PER_1> and <PER_2> | made | egg | rolls | to share | at the | school | <unk> | . <PER_1> | <unk> | <num> | egg | rolls | . <MISC_1> | <unk> | <num> | egg | rolls | . What | is | the total | number | of | egg | rolls | <PER_1> | and <PER_2> | <unk> | ? <eos> | Addition | ilds |
| There | were | <num> | bales | of hay | in the | barn | . <PER_1> | <unk> | bales | in the | barn | today | . There | are | now <num> | bales | of | hay | in the | barn | . How many | bales | did | he | store | in the | barn | ? <eos> | Subtraction | ai2 |
| While | <unk> | <unk> | at her | <unk> | <unk> | , <PER_1> | <unk> | that she | had | <num> | box | of | baking | <unk> | yesterday | , but the | <unk> | is | now down to <num> | box | . How much more | baking | <unk> | did | <PER_1> | have | yesterday | ? <eos> | Subtraction | ai2 |
| A | company <unk> | some | houses | in <LOC_1> <LOC_2> | white and blue | <unk> | a | total | of <num> | gallons | of | <unk> | . If they | used | <num> | gallons | of white | <unk> | , how many | gallons | of | blue | <unk> | did | the | company | use | ? <eos> | Subtraction | ai2 |
| There | were | <num> red | orchids | and <num> | white | orchids | in the | vase | . <PER_1> | cut | some red | orchids | from her flower | garden | . There | are | now <num> | red | orchids | in the | vase | . How many | red | orchids | did | she | cut | ? <eos> | Subtraction | ai2 |

### Top-14 (14 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | ran | <num> | mile | and | walked | <num> | mile | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | ran | <num> | miles | and | walked | <num> | miles | . How much <unk> | did | <PER_1> | run | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | <unk> | <num> | points | per | game | in basketball | . How many | points | would | he | score | in <num> | games | ? <eos> | Multiplication | ilds |
| Mrs. <PER_1> | <unk> | <num> | <unk> | eat | <num> | flowers | each . How many | flowers | total | did | the | <unk> | eat | ? <eos> | Multiplication | ilds |
| There | are | <num> | leaves | . There | are | <num> | ladybugs | on each | <unk> | . How many | ladybugs | are | there | in all ? <eos> | Multiplication | ilds |
| There | are | <num> | <unk> | . There | are | <num> | apples | in each | <unk> | . How many | apples | are | there | in all ? <eos> | Multiplication | ilds |
| <PER_1> | can | <unk> | at a | <unk> | of <num> | miles | an hour | . How far | can | she | <unk> | in <num> | hours | ? <eos> | Multiplication | ilds |
| There | are | <num> | <unk> | . Each | <unk> | has | <num> | flowers | in it | . How many | flowers | are | there | in all ? <eos> | Multiplication | ilds |
| <PER_1> | drove | <num> | miles | in one | hour | . At that | <unk> | , how far | can | she | drive | in <num> | hours | ? <eos> | Multiplication | ilds |
| There | were | <num> | girls | and <num> | boys | on the | playground | at | recess | . How many | children | were | there | in all ? <eos> | Addition | ilds |

### Top-15 (13 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to | the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| <PER_1> | went | to | the | store | <num> | times | last | month | . She | buys | <num> | peanuts | each | time | she | goes | to the | store | . How many | peanuts | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| There | are | <num> | popular | trees | currently in the | park | . Park | workers | will | plant | <num> | popular | trees | today | . How many | popular | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | . How many | orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | <num> | walnut | trees | today | . How many | walnut | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | were | a | total | of <num> | football | games | this | year | , <num> | are | played | at night | . <PER_1> | missed | <num> | of the | games | . How many | football | games | did | <PER_1> | go | to in | total | ? <eos> | Subtraction | ai2 |
| <PER_1> 's | cat | had | kittens | and <num> | had | spots | . He | gave | <num> | to <PER_2> | and <num> | to | <PER_3> | . He | now | has | <num> | kittens | . How many | kittens | did | he | have | to | start | with ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> | tall | trees | currently | in the | park | . Park | workers | will | plant | <num> short trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> | tall | trees | currently | in the | park | . Park | workers | will | plant | <num> short trees | today | . How many short | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |

### Top-16 (12 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | eggs | in each | box | . How many | eggs | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| There | are | <num> | marbles | in each | box | . How many | marbles | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| <PER_1> | <unk> | <num> | miles | at <num> | miles | per | hour | . How long | did | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| There | are | <num> | crayons | in each | box | . How many | crayons | are | in <num> | boxes | ? <eos> | Multiplication | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per | hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| There | are | <num> | cards | . <num> | cards | more | are | added | . How many | are | there total ? <eos> | Addition | ilds |
| There | are | <num> | marbles | . <num> | marbles | more | are | added | . How many | are | there total ? <eos> | Addition | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per | hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |
| If <PER_1> | jogged | <num> | kilometers | at <num> | kilometers | per | hour | , how long | was | <PER_1> <unk> | ? <eos> | CommonDiv | ilds |

### Top-17 (12 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | oranges | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | oranges | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | has | <num> | bananas | that | must | be | put | away in | boxes | . <PER_2> | comes | to | help | and | brings | <num> | cookies | to | share | with <PER_1> | . If there | are | <num> | boxes | , how many | bananas | must | go | in each | box | ? <eos> | CommonDiv | ilds |
| <PER_1> | went | to <num> | soccer | games | this | year | , but | missed | <num> | . She | went | to <num> | games | last | year | and | <unk> | to | go | to <num> | games | next | year | . How many | soccer | games | will | <PER_1> | go | to | in all ? <eos> | TimeVariantUnknownFinal | ai2 |
| <PER_1> | found | an | orange | caterpillar | and a green | caterpillar | in her | <unk> | . The | green | caterpillar | was | <num> | inches | long | and the | orange | caterpillar | was | <num> | inches | long | . How much longer | was | the | green | caterpillar | than the | orange | caterpillar | ? <eos> | Subtraction | ai2 |
| <unk> <PER_1> | weighed | <num> | pieces | of | <unk> | for an <unk> | . The | piece | of | <unk> | weighed | <num> | pounds | and the | piece | of | <unk> | weighed | <num> | pound | . How much more | did | the | piece | of | <unk> | weigh than the | piece | of | <unk> | ? <eos> | Subtraction | ai2 |
| Mrs. <PER_1> | measured | the | <unk> | from her | desk | to the | water | <unk> | . It | was | <num> | feet | . How many | feet | will | Mrs. <PER_1> | walk | on her | <unk> | to the | <unk> | <unk> | she | goes | to the | water | <unk> | <num> | times | today | ? <eos> | Multiplication | ilds |
| There | were | <num> | bales | of hay | in the | barn | and <num> bales | in the | <unk> | . <PER_1> | <unk> | bales | in the | barn | today | . There | are | now <num> | bales | of | hay | in the | barn | . How many | bales | did | he | store | in the | barn | ? <eos> | Subtraction | ai2 |

### Top-18 (11 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | went | to the | store | <num> | times | last | month | . She | buys | <num> | bottle | caps | each | time | she | goes | to the | store | . How many | bottle | caps | did | <PER_1> | buy | last | month | ? <eos> | Multiplication | ilds |
| <unk> | car | gets | <num> | miles | per | gallon | of | gas | . If <PER_1> | \xe2\x80\x99s | house | is | <num> | miles | away | , how many | gallons | of | gas | would | it | take | to | get | to her | house | ? <eos> | CommonDiv | ilds |
| <PER_1> | had | <num> | peaches | at | his | <unk> | fruit | dish | . He | went | to the | orchard | and | picked | peaches | to | <unk> | up | . There | are | now <num> | peaches | . how many | did | he | pick | ? <eos> | Subtraction | ai2 |
| The <ORG_1> <ORG_2> | sold | a | total | of | <num> | tickets | last | season | . If they | sold | <num> | tickets | in the | first | <unk> | of | the | season | , how many | tickets | did | they | <unk> | in the | second | <unk> | ? <eos> | Subtraction | ai2 |
| <PER_1> | added | <num> | cup | of <unk> | to a | <unk> | of | trail | mix | . Later | , she | added | <num> | cup | of | <unk> | . How many | cups | of | <unk> | did | <PER_1> | put | in the | trail | mix | in all ? <eos> | Addition | ai2 |
| <PER_1> | made | trail | mix | for a <unk> | trip | . She | used | <num> | pound | of | peanuts | , <num> | pound | of chocolate | <unk> | , and <num> | pound | of | raisins | . How many | pounds | of trail | mix | did | <PER_1> | make | ? <eos> | Sum | ai2 |
| <PER_1> | did | a | <unk> | <unk> | to | get | in <unk> | for soccer | season | . <unk> | , <PER_1> | ran | <num> | mile | . Then she | ran | <num> | mile | and | <num> | mile | . How many | miles | did | <PER_1> | run | in total ? <eos> | TimeVariantUnknownFinal | ai2 |
| <PER_1> | found | <num> | seashells | , <PER_2> | found | <num> | seashells | , and <PER_3> | found | <num> | seashells | on the | beach | . When they | cleaned | them | , they | discovered | that <num> | were | cracked | . How many | seashells | did | they | find | together ? <eos> | Sum | ai2 |
| <unk> | class | had | a | pizza | party | . <num> | of a | pizza | was | left | over | , and <num> | of another | pizza | was | left | over . You | put | them | both into one | box | . How much | pizza | do | you | have | altogether ? <eos> | Addition | ilds |
| <PER_1> and <PER_2> | <unk> | their | <unk> | <unk> | . <unk> their | mother | bought | for them a <unk> | <unk> | yesterday | . <PER_2> | <unk> | <num> | times | on the | <unk> | . <PER_1> | <unk> | <num> more | times | than <PER_2> | . How many | times | did | they | <unk> | altogether ? <eos> | Addition | ilds |

### Top-19 (10 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | bought | <num> | watermelons | . The | first | <unk> | was | <num> | pounds | , and the | second | <unk> | was | <num> | pounds | . How many | pounds | of | <unk> | did | <PER_1> | buy | ? <eos> | Addition | ai2 |
| <PER_1> | went | to a | <unk> | sale | to | buy | chairs | . Each | <unk> | cost | <num> | dollars | . How much | money | did | <PER_1> | spend | for the | <num> | chairs | she | bought | ? <eos> | Multiplication | ilds |
| <unk> | fill | an | <unk> | , the | <unk> | <unk> | <num> | <unk> | of | <unk> | green and <num> | <unk> | <unk> | . How many | <unk> | of | <unk> | did | it | <unk> | for that | <unk> | ? <eos> | Addition | ai2 |
| This | afternoon | <PER_1> | left | school | , <unk> | the | bus | <num> | miles | , and then | walked | <num> | mile | to | get | home | . How much <unk> | did | <PER_1> | ride | than | walk | ? <eos> | Subtraction | ai2 |
| <PER_1> | went | to <num> | basketball | games | this | year | , but | missed | <num> | . He | went | to <num> | games | last | year | . How many | basketball | games | did | <PER_1> | go | to | in total ? <eos> | Addition | ai2 |
| <PER_1> 's | cat | had | kittens | . He | gave | <num> | to <PER_2> | and <num> | to | <PER_3> | . He | now | has | <num> | kittens | . How many | kittens | did | he | have | to | start | with ? <eos> | TimeVariantUnknownInitial | ai2 |
| <PER_1> <PER_2> | dog | had | puppies | and <num> | had | spots | . He | gave | <num> | to his | friends | . He | now has | <num> | puppies | . How many | puppies | did | he | have | to | start | with ? <eos> | Addition | ai2 |
| <PER_1> | had | some | balloons | . His | mom | gave | him | <num> more | balloons | for his | birthday | . Then , <PER_1> | had | <num> | balloons | . How many | balloons | did | <PER_1> | have | to | start | with ? <eos> | Subtraction | ilds |
| Mrs. <PER_1> | is | <unk> <MISC_1> | <MISC_2> <MISC_3> <unk> | for her | <num> | dogs | . If she | wants | to | buy | them | <num> | <unk> | <unk> | each | , how many | <unk> | does | she | need | to | buy | ? <eos> | Multiplication | ilds |
| There | are | <num> | books | in <LOC_1> | <LOC_2> 's | <unk> | library | . In <unk> | , there | are | <num> | books | in <unk> | school | <unk> | . How many | books | do | the | <unk> | in <LOC_1> <LOC_2> | have | <unk> ? <eos> | Addition | ai2 |

### Top-20 (7 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | owns | <num> | dogs | . Each | day | , <num> | dog | <unk> | <num> | scoop | of | dog | food | and the <unk> | dog | <unk> | <num> | scoop | . <unk> | , how much | dog | food | do | the | <num> | dogs | eat | each | day | ? <eos> | Addition | ai2 |
| A | <unk> | <unk> | <unk> | <num> | truck | - | load | of | sand | , <num> | truck | - | load | of | <unk> | , and <num> | truck | - | load | of | cement | . How many | truck | - | <unk> | of | material | were | needed | in all ? <eos> | Sum | ai2 |
| <PER_1> | has | <num> | books | in his | library | . He | bought | <unk> | books | at a | yard | sale | over the | weekend | . He | now | has | <num> | books | in his | library | . How many | books | did | he | buy | at the | yard | sale | ? <eos> | Subtraction | ai2 |
| <PER_1> | received | <num> | dollars | for his | birthday | . He | went | to a | <unk> | <unk> | store | and bought | a | baseball | <unk> | , baseball | , and <unk> | . He | had | <num> | dollars | over | , how much | did | he | spent | on the | baseball | <unk> | ? <eos> | Subtraction | ai2 |
| <PER_1> 's | family | <unk> | from the | <LOC_1> | to <LOC_2> | , so they | had | <unk> | their | money | into <MISC_1> | yen | . <unk> | <unk> | <unk> | now has | <num> | yen | and their | <unk> | <unk> | now has | <num> | yen | . How many | yen | do | they | have | ? <eos> | Addition | ai2 |
| <PER_1> | went | to <num> | football | games | this | month | . She | went | to <num> | games | last | month | , and <unk> | to go | to <num> | games | next | month | . She | paid | <num> | dollars | for the | tickets | . How many | games | will | she | <unk> | in all ? <eos> | TimeVariantUnknownFinal | ai2 |
| Last Saturday , <PER_1> | walked | all over | <unk> | <unk> <unk> | . <unk> | , he | walked | <num> | mile | from his | house to the | library | and <num> | mile | from the | library | to the <unk> <unk> | . Then he | walked | <num> | mile | from the | <unk> <unk> <unk> | home | . How many | miles | did | <PER_1> | walk | in all ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-21 (6 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <PER_2> | <unk> | is | <num> | feet | long | and <num> | feet | <unk> | . How much | <unk> | does | she | need | to | <unk> | the whole | <unk> | ? <eos> | Multiplication | ilds |
| A | <unk> | - <unk> | <unk> | has | <num> | <unk> | - | time | employees | and <num> <unk> | - | time | employees | . How many | employees | work | for the | <unk> | ? <eos> | Addition | ai2 |
| A | construction company | bought | <num> | tons | of | <unk> | and <num> | tons | of | sand | . How many | tons | of | material | did | the | company | buy | in all ? <eos> | Addition | ai2 |
| <PER_1> | got fast | food | for lunch | . <PER_1> | spent | $ <num> | on a | <unk> | and $ <num> | on a | <unk> | . What | was | the | total | of the | lunch | bill | ? <eos> | Addition | ai2 |
| <PER_1> and <PER_2> | <unk> | <unk> | <unk> | . <PER_1> | <unk> | <num> | <unk> | of <unk> | on Monday and <PER_2> | <unk> | <num> | <unk> | . How many more | acres | did | <PER_1> | harvest | than <PER_2> | ? <eos> | Subtraction | ai2 |
| Last | year | at <LOC_1> 's | <unk> | , <num> | <unk> | <unk> | on time | . <unk> | , <num> | <unk> | <unk> | <unk> | . In all | , how many | <unk> | <unk> | in <LOC_1> last | year | ? <eos> | Addition | ai2 |

### Top-22 (6 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | fruit | farm | packs | oranges | in boxes | that | hold | <num> | each | . <unk> | day | it | packs | <num> | oranges | . How many | boxes | did | they | use | ? <eos> | CommonDiv | ilds |
| <PER_1> | went | to the <unk> | store | . She | bought | <num> | packs | of | cookies | and <num> | packs | of | noodles | . How many | packs | of | <unk> | did | she | buy | in all ? <eos> | Addition | ilds |
| A | construction | company | <unk> | <num> | ton | of | <unk> | , <num> | ton | of | <unk> | , and <num> | ton | of | <unk> | . How many | tons of material | did | the | company <unk> | in all ? <eos> | Sum | ai2 |
| At a | pizza | party | , <PER_1> | and his | friends | <unk> | <num> | <unk> | of <unk> | - | <unk> | <unk> | and <num> | <unk> | of | <unk> | . How much <unk> | did | they | <unk> | in all ? <eos> | Addition | ai2 |
| Last | year , egg <unk> | in <LOC_1> <LOC_2> | produced | <num> | eggs | . This | year | , <unk> same | <unk> | produced | <num> | eggs | . How many more | eggs | did | the | <unk> | <unk> | this | year | ? <eos> | Subtraction | ai2 |
| <LOC_1> <LOC_2> | was | originally blue <unk> | it <unk> | had | <num> <unk> | plants | . Now there | are | <num> <unk> | plants | , and the | lake | has | <unk> | green | . How many | more <unk> | plants | are | in <LOC_1> <LOC_2> | now ? <eos> | Subtraction | ai2 |

### Top-23 (6 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <PER_2> | pencil | is | <num> | cubes | long | . If she | gets | another | pencil | that | is | <num> | cubes | long | , how many | cubes | long | are | both | pencils | ? <eos> | Addition | ilds |
| A <unk> | <unk> | measured | <num> | fish | that | was | <num> | <unk> | long | and a | second | fish | that | was | <num> | <unk> | long . How much | longer | was | the first | fish | ? <eos> | Subtraction | ai2 |
| The <LOC_1> | <unk> | in <LOC_2> | <LOC_3> | has | <num> | seats | . Each | <unk> | can | hold | <num> | people | . How many | people | can | ride | the <LOC_1> | <unk> | at the | same | time | ? <eos> | Multiplication | ilds |
| A pet | <unk> | store | has | <num> | bags | of | dog | food | and <num> | bags | of | cat | food | . How many more | bags | of | dog | food | are | there than cat | food | ? <eos> | Subtraction | ilds |
| <num> | birds | were | sitting | in a | tree | . Some more | fly | up to the | tree | . Then there | were | <num> | birds | in the | tree | . How many | more | fly | up | to the | tree | ? <eos> | Subtraction | ilds |
| At <PER_1> <PER_2> 's | house | , there | was | <num> | inches | of | snow | , and <LOC_1> <LOC_2> | <LOC_3> | received | <num> | inches | of | snow | . How much | more | snow | did | Mrs. <PER_2> 's | house | have | ? <eos> | Subtraction | ilds |

### Top-24 (6 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | walnut | trees | currently in the | park | . Park | workers | will | plant | walnut | trees | today | . When the workers | are | finished | there | will | be | <num> | walnut | trees | in the | park | . How many | walnut | trees | did | the | workers | plant | today | ? <eos> | Subtraction | ai2 |
| <PER_1> | has | <num> | books | and | <num> | <unk> | in her | library | . She | bought | <unk> | books | at a | yard | sale | over the | weekend | . She | now | has | <num> | books | in her | library | . How many | books | did | she | buy | at the | yard | sale | ? <eos> | Subtraction | ai2 |
| There | are | <num> | maple | trees | currently in the | park | . Park | workers | will | plant | maple | trees | today | . When the workers | are | finished | there | will | be | <num> | maple | trees | in the | park | . How many | maple | trees | did | the | workers | plant | today | ? <eos> | Subtraction | ai2 |
| <unk> a | <unk> | food | drive | , | <unk> | were | <unk> | into | <unk> | . The | drive | <unk> | in <num> | <unk> | of | <unk> | , <num> | <unk> | of | <unk> | , and <num> | <unk> | of | <unk> | . <unk> | , how many | <unk> | would | the | <unk> | food | take | up ? <eos> | Sum | ai2 |
| Mrs. <PER_1> | and her | sister | drove | to a | concert | <num> | miles | away . They | drove | <num> | miles | and then | <unk> | for | gas | . Her | sister | put | <num> | gallons | of | gas | in the | car | . How many | miles | did | they | have | left | to | drive | ? <eos> | Subtraction | ilds |
| <PER_1> | is | a | school | <unk> | . Last | week | , she | picked | up a | total | of <num> | pieces | of | <unk> | . If she | picked | up <num> | pieces | of | <unk> | in the | <unk> | , how many | pieces | of | <unk> | did | <PER_1> | pick | up <unk> | the | <unk> | ? <eos> | Subtraction | ai2 |

### Top-25 (5 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | pencil | weighs | <num> | grams | . How much | do | <num> | pencils | weigh | ? <eos> | Multiplication | ilds |
| A | <unk> has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |
| A | <unk> has | <num> | legs | . How many | legs | do | <num> | bees | have | ? <eos> | Multiplication | ilds |
| If each | <unk> | costs | $ <num> | , how much | must | <PER_1> | <unk> | for <num> | <unk> | ? <eos> | Multiplication | ilds |
| <PER_1> | <unk> | <num> | DVDs | for $ <num> | . How much | did | each <unk> | cost to | <unk> | ? <eos> | CommonDiv | ilds |

### Top-26 (5 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| In <num> | week | , <PER_1> 's | family | <unk> | <num> | carton | of | <unk> | <unk> | and <num> | carton | of <unk> | <unk> | . How much | <unk> | did | they | <unk> | in all ? <eos> | Addition | ai2 |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | stroll | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | run | to <PER_2> 's | house | at <num> | miles | per | hour | . How far | is | it | between <PER_1> 's | house | and <PER_2> 's | house | ? <eos> | Multiplication | ilds |
| It | took | <PER_1> <num> | hours | to | ride | to <LOC_1> <LOC_2> | house | at <num> | miles | per | hour | . How far | is | it | between <PER_1> <PER_2> | house | and <PER_3> 's | house | ? <eos> | Multiplication | ilds |

### Top-27 (5 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | maple | trees | and <num> popular | trees | currently | in the | park | . Park | workers | will | plant | <num> | maple | trees | today | . How many | maple | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Addition | ai2 |
| There | are | <num> | <unk> | trees | currently in the | park | . Park | workers | had | to | cut | down <num> | <unk> | trees | that | were | <unk> | . How many | <unk> | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | Subtraction | ai2 |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . How many | dogwood | trees | will the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |
| There | are | <num> short | bushes | and <num> | tall | trees | currently in the | park | . Park | workers | had | to | cut | down <num> short | bushes | that | were | <unk> | . How many short | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | Subtraction | ai2 |
| <PER_1> | went | to the | <unk> | and had | <num> | inch | of | hair | cut | off . The | next | day | she | went | <unk> | and <unk> | for another <num> | inch | to | be | cut | off . How much | hair | did | she | have | cut | off | in all ? <eos> | Addition | ai2 |

### Top-28 (4 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | has two | <unk> | . The | garden | snake | is | <num> | inches | long | . The | <unk> | <unk> | is | <num> | times | longer | than the | garden | snake | . How long | is | the | <unk> | <unk> | ? <eos> | Multiplication | ilds |
| A | farmer <unk> the | day | with <num> | buckets | of | seeds | . <unk> | <unk> | the | morning | <unk> | seeds | , she | now has | <num> | buckets | . How many | buckets | of | seeds | did | the | farmer | <unk> | ? <eos> | Subtraction | ai2 |
| <PER_1> | got fast | food | for lunch | . <PER_1> | spent | $ <num> | on | <unk> | and $ <num> | on a | <unk> | . <PER_1> | paid | with a | <num> | dollar | bill | . What | was | the | total | of the | lunch | bill | ? <eos> | Addition | ai2 |
| <PER_1> | made <unk> | in the | <unk> | . She | used | <num> | cup | of | strawberries | , <num> | cup | of | <unk> | , and <num> | cup | of | orange | <unk> | . How many | cups of <unk> | did | <PER_1> use | for the | <unk> | ? <eos> | Sum | ai2 |

### Top-29 (4 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | discovered | a | <unk> | <unk> | <unk> | filled | with a | total | of <num> | <unk> | . <num> | of the | <unk> | were | <unk> | , and the | rest | were | <unk> | . How many | of the | <unk> | were | <unk> | ? <eos> | Subtraction | ai2 |
| <PER_1> | \xe2\x80\x99s | <unk> | gives | out | gold | stars | for <unk> | <unk> | work | . <unk> | , <PER_1> | earned | <num> | gold | stars | . | Today | , he | earned | <num> more | . How many | gold | stars | did | <PER_1> | <unk> | in all ? <eos> | Addition | ilds |
| <PER_1> | \xe2\x80\x99s | <unk> | gives | out | gold | stars | for <unk> | <unk> | work | . <unk> | , <PER_1> | earned | <num> | gold | stars | . | Today | , she | earned | <num> more | . How many | gold | stars | did | <PER_1> | <unk> | in all ? <eos> | Addition | ilds |
| <PER_1> | was | in the | <unk> | and she | got | <num> | get | <unk> | cards | from <unk> the | <unk> | . When she | got | home she | got | <num> more | cards | from friends | and family | . How many | get | <unk> | cards | did | <PER_1> | get | ? <eos> | Addition | ilds |

### Top-30 (3 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Each | banana | costs | $ <num> | . How much | do | <num> | bananas | cost | ? <eos> | Multiplication | ilds |
| Each | <unk> | costs | $ <num> | . How much | do | <num> | tickets | cost | ? <eos> | Multiplication | ilds |
| Each | cup <unk> | <num> | ounces | . How many | ounces | are | in <num> | cups | ? <eos> | Multiplication | ilds |

### Top-31 (3 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| The | <unk> | of <LOC_1> | has | <num> | <unk> | - | <unk> | and <num> | children | . How many | people | <unk> | in <PER_1> | ? <eos> | Addition | ilds |
| <unk> | car | gets | <num> | miles | per | gallon | . How many | miles | can | I | drive | on <num> | gallons | of gas ? <eos> | Multiplication | ilds |
| A | car | company | produced | <num> | cars | in <LOC_1> <LOC_2> | and <num> | cars | in <LOC_3> | . How many | cars | is | that | in all ? <eos> | Addition | ai2 |

### Top-32 (3 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | <unk> | produced | <num> | pounds | of | honey | , but <unk> | ate | <num> | pounds | of it | . How much | honey | <unk> | ? <eos> | skip | ai2 |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |
| Each | child | has | <num> | bottle | caps | . If there | are | <num> | children | , how many | bottle | caps | are | there in | total | ? <eos> | Multiplication | ilds |

### Top-33 (3 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | at a <unk> | <unk> | is | <unk> | blood | <unk> | . <num> | <unk> | <unk> | a | total | of <num> | blood | <unk> | . The first | <unk> | <unk> | <num> | blood | <unk> | . How many | blood | <unk> | were | in the second | <unk> | ? <eos> | Subtraction | ai2 |
| <PER_1> <unk> | bought | a new | lamp | for her | <unk> | table | . The old | lamp | was | <num> | <unk> | tall | and the new | lamp | is | <num> | feet | tall | . How much | <unk> | is | the | new | lamp | than the | old | lamp | ? <eos> | Subtraction | ai2 |
| Mrs. <PER_1> | <unk> | at her | car 's | <unk> | before a | trip | . The | <unk> | <unk> | that she | had | traveled | <num> | miles | . When she | <unk> | for | lunch | , the | <unk> | read | <num> | . How many | miles | had | she | traveled | ? <eos> | Subtraction | ilds |

### Top-34 (3 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | baking | a | cake | . The | recipe | <unk> | for <num> | cups | of | flour | and <num> | cups | of | sugar | . She | already | put | in <num> | cups | of | flour | . How many | cups | of | flour | does | she | need | to | add | ? <eos> | Subtraction | ai2 |
| <PER_1> | is | baking | a | cake | . The | recipe | <unk> | for <num> | cups | of | flour | and <num> | cups | of | sugar | . She | already | put | in <num> | cups | of | flour | . How many | cups | of | flour | does | she | need | to | add | ? <eos> | Subtraction | ai2 |
| <PER_1> | owns | the | <ORG_1> | <ORG_2> <ORG_3> | . This | morning | , her | employees | used | <num> | eggs | to | bake | <unk> | pies | . If her | employees | used | a | total | of | <num> | eggs | today | , how many | eggs | did | they | use | in the | afternoon | ? <eos> | Subtraction | ai2 |

### Top-35 (3 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | are | <num> | dogwood | trees | currently in the | park | . Park | workers | will | plant | <num> | dogwood | trees | today | and <num> | dogwood | trees | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | dogwood | trees | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |
| There | are | <num> | orchid | bushes | currently in the | park | . Park | workers | will | plant | <num> | orchid | bushes | today | and <num> | orchid | bushes | <unk> | . It | took | <num> | workers | to | <unk> | the | work | . How many | orchid | bushes | will | the | park | have | when the | workers | are | finished | ? <eos> | TimeVariantUnknownFinal | ai2 |
| A | ship <unk> | of | grain | <unk> | into a <unk> | <unk> | . <unk> | the | time | the | ship | is | <unk> | , <num> | tons | of | grain | have | <unk> | into the | water | . <unk> | <num> | tons | of | grain | <unk> | <unk> | . How many | tons | of | grain | did | the | ship | originally | <unk> | ? <eos> | Addition | ai2 |

### Top-36 (2 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> <PER_2> | <num> | oranges | . He | shares | <num> | with <PER_3> | . How many | oranges | will | <PER_1> | have | ? <eos> | Subtraction | ilds |
| There | were | <num> <unk> | and <num> | ducks | in the | <unk> | . How many | birds | were | in the | <unk> | ? <eos> | Addition | ilds |

### Top-37 (2 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | pizzas | during | lunch | and <num> | during dinner | today | . How many | pizzas | were | served | today | ? <eos> | Addition | ai2 |
| The <ORG_1> <ORG_2> | picked | up <num> <unk> | <unk> | and <num> | <unk> | <unk> | on Saturday | . How many | pieces | of | <unk> | did | they | pick | up altogether ? <eos> | Addition | ilds |

### Top-38 (2 samples using it): (85, 14, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 85 | 14 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | boys | went | down the <unk> | . <num> | more | boys | went | down the <unk> | . How many | boys | went | down the <unk> | ? <eos> | Addition | ilds |
| In <LOC_1> it | <unk> | <num> | inch in the | morning | and <num> | inch in the afternoon | . What | was | the total | <unk> | of | <unk> | ? <eos> | Addition | ai2 |

### Top-39 (2 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | restaurant | served | <num> | slices | of | pie | during | lunch | and <num> | during | dinner | today | . It | served | <num> | of | them | yesterday | . How many | slices | of | pie | were | served | today | ? <eos> | Addition | ai2 |
| Some | <unk> | called | <unk> | <unk> | a <unk> | farm | . In <unk> | , the | farmer | <unk> | ladybugs | <unk> the | <unk> | . There | are | <num> | ladybugs | with spots | and <num> | ladybugs <unk> | spots | . How many | ladybugs | are | there | in all ? <eos> | Addition | ai2 |

### Top-40 (2 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | bathing | <unk> | <unk> | has | a | <unk> | of <num> | bathing | <unk> | for <unk> | . In <unk> | , it | has | <num> | bathing | <unk> | for | <unk> | . How many | bathing | <unk> | are | <unk> <unk> | ? <eos> | Addition | ai2 |
| A | <unk> | <unk> | company | has | a | total | of | <num> | customers | <unk> the | <unk> | . If <num> | of <unk> | customers | <unk> | in the | <LOC_1> <LOC_2> | , how many | of <unk> | customers | <unk> | in <unk> | <unk> | ? <eos> | Subtraction | ai2 |

### Top-41 (2 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | made | <unk> | for her | friend 's | birthday party | . She | used | <num> | gallon | of | <unk> | <unk> | , <num> | gallon | of | <unk> | <unk> | , and <num> | gallon | of | <unk> | <unk> | . How many | gallons | of | <unk> | did | <PER_1> | make | ? <eos> | Sum | ai2 |
| <PER_1> 's | <unk> | class | recorded | the <unk> | each | day | . They | recorded | <num> | centimeter | of | rain | on Monday , <num> | centimeter | of | rain | on Tuesday | , and <num> | centimeter | of | rain | on <unk> | . How many | centimeters | of | rain | did | the | class <unk> | in all ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-42 (2 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | farmer | <unk> | that | he | will | harvest | <num> | <unk> | of | wheat | . The | <unk> | is | <unk> | during the | <unk> | season | , so he | <unk> | <num> | <unk> | of | wheat | than | <unk> | . How many | <unk> | of | wheat | does | the | farmer | harvest | ? <eos> | Addition | ai2 |
| <PER_1> | weighed | <num> | <unk> | <unk> | <unk> | during | a | <unk> | class | . The | blue | <unk> | weighed | <num> | pounds | and the brown | <unk> | weighed | <num> | pounds | . If <PER_1> | <unk> | both | <unk> | on the | <unk> | at the same | time | , <unk> | will | the | <unk> | read | ? <eos> | Addition | ai2 |

### Top-43 (2 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | is | a | <unk> | . Last | year | , she | <unk> | <num> | pounds | of | honey | . This | year | , she | bought | some | new | <unk> | and | <unk> | her | honey | harvest | by <num> | pounds | . How many | pounds | of | honey | did | <PER_1> | harvest | this | year | ? <eos> | Addition | ai2 |
| There | are | <num> short | trees | and <num> | tall | trees | currently | in the | park | . Park | workers | will | plant short | trees | today | . When the | workers | are | finished | there | will | be | <num> short | trees | in the | park | . How many | short | trees | did | the | workers | plant | today | ? <eos> | Subtraction | ai2 |

### Top-44 (2 samples using it): (130, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 130 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | children | were | <unk> | on the | bus | . At the | bus | stop | , some more | children | got | on the | bus | . Then there | were | <num> | children | altogether | on the | bus | . How many | children | got | on the | bus | at the | bus | stop | ? <eos> | Subtraction | ilds |
| <num> | children | were | <unk> | on the | bus | . At the | bus | stop | , some more | children | got | on the | bus | . Then there | were | <num> | children | altogether | on the | bus | . How many | children | got | on the | bus | at the | bus | stop | ? <eos> | Subtraction | ilds |

### Top-45 (2 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | construction | company | is | <unk> | a | <unk> | road | . <unk> | far | , they | have | <unk> | a | total | of <num> | inches | of the | road | . | Today | , they | <unk> | <num> | inches | of the | road | . How many | inches | of the | road | had | they | <unk> | before | today | ? <eos> | Subtraction | ai2 |
| <unk> | to be | <unk> | <MISC_1> | <MISC_2> <MISC_3> <unk> | , <PER_1> | called | the | <unk> | from <num> | pages | of the | <unk> | book | last | week | . This | week | , she | called | the | people | <unk> | on another <num> | pages | of the same | <unk> | book | . How many | pages | <unk> | of | people | did | <PER_1> | <unk> | in all ? <eos> | Addition | ai2 |

### Top-46 (1 samples using it): (135, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134)
| 135 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| How much | would | <num> | pieces | of <unk> | gum cost <unk> each | piece | costs | <num> | cents | ? <eos> | Multiplication | ilds |

### Top-47 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | was | <num> | feet | tall | . Then she | grew | <num> | feet | <unk> . How tall | is | <PER_1> | now ? <eos> | Addition | ai2 |

### Top-48 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| There | were | <num> <unk> | and <num> | ducks | in the | <unk> | . How many | birds | were | there | in all ? <eos> | Addition | ilds |

### Top-49 (1 samples using it): (100, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 100 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| How many | cookies | would | you | have <unk> | you | had | <num> | bags | of | cookies | with <num> | cookies | in each | bag | ? <eos> | Multiplication | ilds |

### Top-50 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| In a | school | , there | are | <num> | girls | and <num> | boys | . How many | <unk> | are | there in that | school | ? <eos> | Addition | ilds |

### Top-51 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | box | of | books | weighs | <num> | pounds | . Each | book | weighs | <num> | pounds | . How many | books | are | there in the | box | ? <eos> | CommonDiv | ilds |

### Top-52 (1 samples using it): (130, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 130 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | <unk> | are | in the | lake | . Each | <unk> | has | <num> | people | . How many | people | are | on | <unk> | in the | lake | ? <eos> | Multiplication | ilds |

### Top-53 (1 samples using it): (130, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 130 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | students | were | sitting | at each | table | in the | <unk> | . There | are | <num> | <unk> | . How many | students | were | sitting | in the | <unk> | ? <eos> | Multiplication | ilds |

### Top-54 (1 samples using it): (110, 81, 14, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 110 | 81 | 14 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> - | <unk> | students | went | to a | concert | in <num> <unk> | . Each | bus | took | <num> | students | . How many | students | went | to the | concert | ? <eos> | Multiplication | ilds |

### Top-55 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | <unk> textbook | weighs | <num> | pounds | and her | <unk> | textbook | weighs | <num> | pound | . How much more | does | the | <unk> | textbook | weigh | than the | <unk> | textbook | ? <eos> | Subtraction | ai2 |

### Top-56 (1 samples using it): (8, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 8 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each of | farmer | <PER_1> 's | <num> | <unk> | is | either <unk> or white | . There | are | <num> | white | <unk> | . How many | of <PER_2> | <PER_1> 's | <unk> | are | <unk> | ? <eos> | Subtraction | ai2 |

### Top-57 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | , the | <unk> | of | <PER_1> 's | <unk> | <unk> | <unk> | by $ <num> | . If her | <unk> | was <unk> | $ <num> | before | , how much | is | it <unk> | now ? <eos> | Subtraction | ai2 |

### Top-58 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | bus | ride | to | school | is | <num> | mile | and <PER_2> 's | bus | ride | is | <num> | mile | . How much | longer | is | <PER_1> 's | bus | ride | than <PER_2> | <PER_3> ? <eos> | Subtraction | ai2 |

### Top-59 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| While | <unk> | <unk> | , a | <unk> | used | <num> | bag | of | wheat | flour | and <num> | bag | of white | flour | . How many | bags | of | flour | did | the | <unk> | use | in all ? <eos> | Addition | ai2 |

### Top-60 (1 samples using it): (91, 129, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 91 | 129 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| At the <unk> store | , <num> the | <unk> | are | <unk> | <unk> | and <num> | the | <unk> | are | <unk> <unk> | . What | fraction | of the | <unk> | are | either | <unk> | <unk> | or <unk> | ? <eos> | Addition | ai2 |

### Top-61 (1 samples using it): (8, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 8 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Before the <unk> | <unk> | <unk> | , there | were | <num> | houses | in <LOC_1> <LOC_2> | . Now , there | are | <num> | houses | . How many | houses | did | <unk> | <unk> | during the | <unk> | <unk> | ? <eos> | Subtraction | ai2 |

### Top-62 (1 samples using it): (153, 129, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 153 | 129 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| In <unk> | <PER_1> 's <unk> class | , <num> | the | students | received | A 's | and <num> | received | <unk> 's | . What | fraction | of the | students | received | either A 's | or <unk> 's | ? <eos> | Addition | ai2 |

### Top-63 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each | day | , the <unk> | <unk> | at <LOC_1> 's | <unk> | <unk> | <num> | bucket | of | <unk> | and <num> | bucket | of salmon | . How many | buckets | of | fish | does | the <unk> | <unk> | eat | <unk> | ? <eos> | Addition | ai2 |

### Top-64 (1 samples using it): (16, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 16 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| On the first | day | of the | week | <PER_1> | had | <num> | stickers | . <PER_1> | earned | <num> more | during the | week | . How many | stickers | did | <PER_1> | have | at the | end | of the | week | ? <eos> | Addition | ilds |

### Top-65 (1 samples using it): (110, 81, 14, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 110 | 81 | 14 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Before <unk> , | customers | buy | <num> <unk> | <unk> | from the | mall | . <unk> <unk> | , they | buy | <num> | , and there | are | <unk> | . In all | , how many <unk> | <unk> | do | the | customers | buy | ? <eos> | Addition | ai2 |

### Top-66 (1 samples using it): (8, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 8 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| On a hot | day | , <PER_1> | <unk> | <num> | bucket | of | water | into a <unk> | <unk> | <unk> | . A <unk> | minutes <unk> | he | added | another <num> | buckets | . How much | water | did | <PER_1> <unk> | into the | <unk> | ? <eos> | Addition | ai2 |

### Top-67 (1 samples using it): (41, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 41 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> <ORG_2> <ORG_3> <ORG_4> | used | <num> | tons | of | cement | to | <unk> | <LOC_1> 's | <unk> | and <num> | tons | of | cement | to | <unk> | <PER_1> | 's | <unk> | . How much | cement | did | <ORG_1> 's | <ORG_3> <ORG_4> use | in all ? <eos> | Addition | ai2 |

### Top-68 (1 samples using it): (35, 129, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 35 | 129 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| In <LOC_1> 's <unk> | <unk> , <num> the | apartments | are | one - | <unk> | apartments | and <num> | are | two | - | <unk> | apartments | . What | fraction | of the | apartments | are | either <num> | - | or two | - | <unk> | apartments | ? <eos> | Addition | ai2 |

### Top-69 (1 samples using it): (86, 126, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 86 | 126 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Each year , | salmon <unk> <unk> , | <unk> | from the | <unk> | to the | <unk> | <unk> | they | were | <unk> | . This | year , <num> | <unk> | and <num> | <unk> | salmon | <unk> | to their | <unk> | . How many | salmon | made | the | trip | ? <eos> | Addition | ai2 |

### Top-70 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | chocolate <unk> | cookie | recipe | <unk> | for <num> | cups | of | chocolate | <unk> | . You | <unk> | to | make | <num> | <unk> | for a | bake | sale | . How many | cups | of | chocolate | <unk> | will | be | needed | to | make | all the | cookie | <unk> | ? <eos> | Multiplication | ilds |

### Top-71 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> his | car | , <PER_1> | spent | $ <num> | on | <unk> | and $ <num> | on new | <unk> | . <PER_1> | <unk> | <num> <MISC_1> 's | for $ <num> | but | <unk> | <unk> | to | . In total | , how much | did | <PER_1> | spend | on | car | <unk> | ? <eos> | Addition | ai2 |

### Top-72 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | and his | <unk> | placed | <unk> | blocks | on a | <unk> | during a | <unk> | <unk> | . The yellow | block | weighed | <num> | pounds | and the | green | block | weighed | <num> | pounds | . How much more | did | the yellow | block | weigh | than the green | block | ? <eos> | Subtraction | ai2 |

### Top-73 (1 samples using it): (129, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 129 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> the | students | in the | band | are | in the | trumpet | section | . <num> | the | students | in the | band | are | in the <unk> | section | . What | fraction | of the | students | in the | band | are | in either the | trumpet | section | or the | <unk> | section | ? <eos> | Addition | ai2 |

### Top-74 (1 samples using it): (45, 14, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 45 | 14 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <ORG_1> <ORG_2> <ORG_3> <ORG_4> | purchased | pieces | of | <unk> | from a | <unk> | . The | <unk> | of the | pieces | they | purchased | were | <num> | ton | , <num> | ton | , and <num> | ton | . How many | tons of <unk> | did | <ORG_1> | <ORG_2> <ORG_3> <ORG_4> <unk> | in all ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-75 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| At the | beach | , <PER_1> | and her | sister | both | <unk> | <unk> | and then | measured their | <unk> | . <PER_1> 's | <unk> | was | <num> | feet | tall | and her | sister 's | was | <num> | feet | tall | . How much | <unk> | was | <PER_1> 's | <unk> | than her | sister | 's | ? <eos> | Subtraction | ai2 |

### Top-76 (1 samples using it): (14, 82, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 14 | 82 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | at <LOC_1> schools | are | <unk> | in a | <unk> | drive | . <num> | <unk> | have | <unk> | collected | so far | . <num> | <unk> | were | collected | from the <unk> | schools | , and the | rest from the elementary | schools | . How many | <unk> | were | collected | at the elementary | schools | ? <eos> | Subtraction | ai2 |

### Top-77 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | put | <unk> | <unk> | into the | <unk> | on <unk> | night | . She | <unk> | that the | restaurant | had | <num> | <unk> | filled | with <unk> | , <num> | <unk> | filled | with | <unk> | , and <num> | <unk> | filled | with | peaches | . How many <unk> | <unk> | did | the | restaurant | have | in all ? <eos> | Sum | ai2 |

### Top-78 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A | <unk> | traveled | <num> | light | - | year | from <unk> | to <MISC_1> <MISC_2> | and <num> | light | - | year | from <MISC_1> | <MISC_2> to <MISC_1> <MISC_3> | Then it | traveled | <num> | light | - | year | from <LOC_1> <LOC_2> <unk> | to <unk> | . How many | light | - | <unk> | did | the | <unk> | <unk> | in all ? <eos> | TimeVariantUnknownFinal | ai2 |

### Top-79 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> | <unk> the | <unk> | ice | cream | after a <unk> | party | . She | had | <num> | carton | of <unk> | road | ice | cream | , <num> | carton | of | cookie | <unk> | ice | cream | , and <num> | carton | of <unk> | <unk> | ice | cream | . How many | <unk> | of | ice | cream | did | <PER_1> | have | in all ? <eos> | Sum | ai2 |

### Top-80 (1 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| When <PER_1> | had | <num> | cat | , he | needed | to | serve | <num> | can | of | cat | food | each | day | . Now that | <PER_1> | has | <unk> | a | second | cat | , he | needs | to | serve | a | total | of | <num> | can | each | day | . How much | extra | food | is | needed | to | <unk> | the | second | cat | ? <eos> | Subtraction | ai2 |

### Top-81 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | oil | pipe | in the | <unk> | <unk> | . Before | engineers | <unk> | to | <unk> | the | pipe | , <num> | <unk> | of | oil | leaked | into the | water | . While the | engineers | worked | , the | pipe | leaked | <num> | <unk> | of | oil | . In all | , how many | <unk> | of | oil | leaked | into the | water | ? <eos> | Addition | ai2 |

### Top-82 (1 samples using it): (162, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134)
| 162 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <unk> | oil | pipe | in the | <unk> | <unk> | . Before | engineers | <unk> | to | <unk> | the | pipe | , <num> | gallons | of | oil | leaked | into the water | . A | total | of <num> | gallons | of | oil | leaked | before the | pipe | was | <unk> | . How many | gallons | of | oil | leaked | <unk> the | engineers | were | <unk> | the | pipe | ? <eos> | Subtraction | ai2 |

### Top-83 (1 samples using it): (127, 151, 165, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 127 | 151 | 165 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> and her | family | use | up a | <unk> | of | <unk> | and | <unk> | jelly , <unk> | they | eat <unk> | every | morning | . At the | <unk> | , they | have | a | <unk> | total | of <num> | grams | of jelly | . If they | have | <num> | grams | of | <unk> | jelly | , how many | grams | of | <unk> | jelly | do | they | have | ? <eos> | Subtraction | ai2 |

### Top-84 (1 samples using it): (92, 67, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133, 134, 174, 133)
| 92 | 67 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | 134 | 174 | 133 | solution type | source |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <PER_1> 's | family | went | on a | <unk> | trip | in the | <unk> | . On the first | day | , they | <unk> | from their | car | to the | <unk> | . <unk> | , they | <unk> | <num> | mile | from the | car | to a | <unk> | , and <num> | mile | from the | <unk> | to a | <unk> | . Then they | <unk> | <num> | mile | from the | <unk> | to | the | <unk> | . How many | miles | did | <PER_1> 's | family <unk> | in all ? <eos> | TimeVariantUnknownFinal | ai2 |


