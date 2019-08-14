Namespace(a_gen=False, a_seg=True, data='/home/shangling/Datasets/3k-mathqa-train-valid', gen_fi='', pure='', tagged_fi='segs/seg-3k-mathqa-300-45-3-100-far.txt')
# Analysis of segmentation
metadata_path=/home/shangling/Datasets/3k-mathqa-train-valid/metadata_train.tsv
seg_path=segs/seg-3k-mathqa-300-45-3-100-far.txt
k=100
n=10
# Overall - top templates
### Top-1 (9 samples using it): (55, 10, 41)
| 55 | 10 | 41 |
| - | - | - |
| ( <num> | x <num> ) = | ? <eos> |
| <num> - ? | = <num> - <num> | <eos> |
| ? x <num> = | <num> x <num> | <eos> |
| <num> * <num> | * <num> = | ? <eos> |
| <num> - <num> | - <num> = | ? <eos> |
| ( <num> ) - | ? = <num> | <eos> |
| <num> * <num> | * <num> = | ? <eos> |
| - <num> x <num> | + <num> = | ? <eos> |
| <unk> , <unk> , | <unk> , <unk> , | <eos> |

### Top-2 (6 samples using it): (115, 83, 35, 124, 44, 2, 72, 124, 44, 2, 123, 40, 102, 31, 119, 74, 36)
| 115 | 83 | 35 | 124 | 44 | 2 | 72 | 124 | 44 | 2 | 123 | 40 | 102 | 31 | 119 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| an | article | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | loss | percent | ? <eos> |
| a | cycle | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | gain | percent | ? <eos> |
| a | cycle | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | gain | percent | ? <eos> |
| an | article | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | gain | percent | ? <eos> |
| an | article | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | loss | percent | ? <eos> |
| an | article | is | bought | for | rs | . <num> and | sold | for | rs | . <num> | , | find | the | gain | percent | ? <eos> |

### Top-3 (5 samples using it): (115, 38, 125, 120, 114, 91, 0, 44, 94, 71, 23, 40, 102, 31, 119, 11, 2, 126)
| 115 | 38 | 125 | 120 | 114 | 91 | 0 | 44 | 94 | 71 | 23 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | train | running | at the speed | of <num> km / | hr | crosses | a | pole | in <num> | seconds | . | find | the | length | of the | train | ? <eos> |
| a | train | running | at the speed | of <num> km / | hr | crosses | a | post | in <num> | seconds | . what | is | the | length | of the | train | ? <eos> |
| a | train | running | at the speed | of <num> km / | hr | crosses | a | pole | in <num> | sec | . what | is | the | length | of the | train | ? <eos> |
| a | train | running | at the speed | of <num> km / | hr | crosses | a | pole | in <num> | seconds | . what | is | the | length | of the | train | ? <eos> |
| a | train | running | at the speed | of <num> km / | hr | crosses | a | pole | in <num> | sec | . what | is | the | length | of the | train | ? <eos> |

### Top-4 (5 samples using it): (115, 83, 84, 64, 91, 0, 44, 49, 17, 2, 69, 112, 120, 54, 38, 125, 34, 71, 23, 63, 29, 101, 38, 125, 41)
| 115 | 83 | 84 | 64 | 91 | 0 | 44 | 49 | 17 | 2 | 69 | 112 | 120 | 54 | 38 | 125 | 34 | 71 | 23 | 63 | 29 | 101 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | train | <num> | m | long | passes | a | man | , | running | at <num> km | / hr | in the same direction | in which the | train | is | going | , in <num> | seconds | . the | speed | of the | train | is | ? <eos> |
| a | train | <num> | m | long | passes | a | man | , | running | at <num> km | / hr | in the same direction | in which the | train | is | going | , in <num> | seconds | . the | speed | of the | train | is | : <eos> |
| a | train | <num> | m | long | passes | a | man | , | running | at <num> km | / hr | in the same direction | in which the | train | is | going | , in <num> | seconds | . the | speed | of the | train | is | : <eos> |
| a | train | <num> | m | long | passes | a | man | , | running | at <num> km | / hr | in the same direction | in which the | train | is | going | , in <num> | seconds | . the | speed | of the | train | is | ? <eos> |
| a | train | <num> | m | long | passes | a | man | , | running | at <num> km | / hr | in the same direction | in which the | train | is | going | , in <num> | seconds | . the | speed | of the | train | is | : <eos> |

### Top-5 (5 samples using it): (115, 38, 125, 134, 94, 71, 23, 64, 22, 64, 91, 0, 46, 71, 23, 64, 22, 64, 91, 0, 46, 63, 29, 101, 38, 125, 91, 0, 30, 48, 36)
| 115 | 38 | 125 | 134 | 94 | 71 | 23 | 64 | 22 | 64 | 91 | 0 | 46 | 71 | 23 | 64 | 22 | 64 | 91 | 0 | 46 | 63 | 29 | 101 | 38 | 125 | 91 | 0 | 30 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | trader | bought | a | car | at <num> | % | discount | on its original | price | . he | sold | it | at a <num> | % | increase | on the | price | he | bought | it | . what | percent | of | profit | did | he | make | on the original | price | ? <eos> |
| a | trader | bought | a | car | at <num> | % | discount | on its original | price | . he | sold | it | at a <num> | % | increase | on the | price | he | bought | it | . what | percent | of | profit | did | he | make | on the original | price | ? <eos> |
| a | trader | bought | a | car | at <num> | % | discount | on its original | price | . he | sold | it | at a <num> | % | increase | on the | price | he | bought | it | . what | percent | of | profit | did | he | make | on the original | price | ? <eos> |
| a | trader | bought | a | car | at <num> | % | discount | on its original | price | . he | sold | it | at a <num> | % | increase | on the | price | he | bought | it | . what | percent | of | profit | did | he | make | on the original | price | ? <eos> |
| a | trader | bought | a | car | at <num> | % | discount | on its original | price | . he | sold | it | at a <num> | % | increase | on the | price | he | bought | it | . what | percent | of | profit | did | he | make | on the original | price | ? <eos> |

### Top-6 (4 samples using it): (40, 102, 31, 119, 11, 2, 69, 16, 36)
| 40 | 102 | 31 | 119 | 11 | 2 | 69 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| what | is | the | sum | of the | numbers | between <num> and <num> | , inclusive | ? <eos> |
| what | is | the | sum | of the odd | integers | from <num> to <num> | , inclusive | ? <eos> |
| what | is | the | sum | of all the | multiples | of <num> between <num> | and <num> | ? <eos> |
| in what | time | a | sum | of money double | itself | at <num> % per | annum simple interest | ? <eos> |

### Top-7 (4 samples using it): (121, 4, 56, 83, 35, 89, 2, 84, 64, 22, 64, 81)
| 121 | 4 | 56 | 83 | 35 | 89 | 2 | 84 | 64 | 22 | 64 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| the | area | of a | triangle | is | with | base | <num> | m | and height <num> | m | ? <eos> |
| the | area | of a | triangle | is | with | base | <num> | m | and height <num> | m | ? <eos> |
| the | area | of a | triangle | is | with | base | <num> | m | and height <num> | m | ? <eos> |
| the | area | of a | triangle | is | with | base | <num> | m | and height <num> | m | ? <eos> |

### Top-8 (4 samples using it): (121, 4, 56, 14, 94, 71, 23, 4, 56, 14, 54, 38, 125, 129, 85, 102, 31)
| 121 | 4 | 56 | 14 | 94 | 71 | 23 | 4 | 56 | 14 | 54 | 38 | 125 | 129 | 85 | 102 | 31 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | angle | between the | minute | hand | and the | hour | hand | of a | clock | when the | time | is | <num> | , | is | <eos> |
| the | angle | between the | minute | hand | and the | hour | hand | of a | clock | when the | time | is | <num> | , | is | <eos> |
| the | angle | between the | minute | hand | and the | hour | hand | of a | clock | when the | time | is | <num> | , | is | <eos> |
| the | angle | between the | minute | hand | and the | hour | hand | of a | clock | when the | time | is | <num> | , | is | <eos> |

### Top-9 (4 samples using it): (8, 38, 125, 70, 83, 84, 64, 91, 0, 46, 0, 89, 2, 84, 64, 63, 29, 101, 38, 125, 84, 64, 81)
| 8 | 38 | 125 | 70 | 83 | 84 | 64 | 91 | 0 | 46 | 0 | 89 | 2 | 84 | 64 | 63 | 29 | 101 | 38 | 125 | 84 | 64 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| how many | seconds | will | a | train | <num> | meters | long | take | to | cross | a | bridge | <num> | meters | long if the | speed | of the | train | is | <num> | kmph | ? <eos> |
| how many | seconds | will | a | train | <num> | meters | long | take | to | cross | a | bridge | <num> | meters | long if the | speed | of the | train | is | <num> | kmph | ? <eos> |
| how many | seconds | will | a | train | <num> | meters | long | take | to | cross | a | bridge | <num> | meters | long if the | speed | of the | train | is | <num> | kmph | ? <eos> |
| how many | seconds | will | a | train | <num> | meters | long | take | to | cross | a | bridge | <num> | meters | long if the | speed | of the | train | is | <num> | kmph | ? <eos> |

### Top-10 (4 samples using it): (121, 4, 56, 83, 35, 129, 18, 38, 125, 30, 23, 69, 68, 112, 108, 2, 107, 38, 125, 41)
| 121 | 4 | 56 | 83 | 35 | 129 | 18 | 38 | 125 | 30 | 23 | 69 | 68 | 112 | 108 | 2 | 107 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | mean | of <num> | observations | was | <num> | . it | was | found | later that an | observation | <num> was wrongly | taken | as <num> | . the | corrected | new | mean | is | <eos> |
| the | mean | of <num> | observations | was | <num> | . it | was | found | later that an | observation | <num> was wrongly | taken | as <num> | . the | corrected | new | mean | is | <eos> |
| the | mean | of <num> | observations | was | <num> | . it | was | found | later that an | observation | <num> was wrongly | taken | as <num> | . the | corrected | new | mean | is | <eos> |
| the | mean | of <num> | observations | was | <num> | . it | was | found | later that an | observation | <num> was wrongly | taken | as <num> | . the | corrected | new | mean | is | : <eos> |

### Top-11 (4 samples using it): (31, 119, 11, 2, 99, 83, 84, 64, 91, 0, 106, 64, 107, 38, 125, 34, 71, 23, 130, 125, 41)
| 31 | 119 | 11 | 2 | 99 | 83 | 84 | 64 | 91 | 0 | 106 | 64 | 107 | 38 | 125 | 34 | 71 | 23 | 130 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | length | of the | bridge | , which a | train | <num> | metres | long and | travelling | at <num> | km | / | hr | can | cross | in <num> | seconds | , | is | : <eos> |
| the | length | of the | bridge | , which a | train | <num> | metres | long and | travelling | at <num> | km | / | hr | can | cross | in <num> | seconds | , | is | ? <eos> |
| the | length | of the | bridge | , which a | train | <num> | metres | long and | travelling | at <num> | km | / | hr | can | cross | in <num> | seconds | , | is | ? <eos> |
| the | length | of the | bridge | , which a | train | <num> | meters | long and | travelling | at <num> | km | / | hr | can | cross | in <num> | seconds | , | is | : <eos> |

### Top-12 (4 samples using it): (115, 83, 35, 89, 2, 1, 102, 31, 119, 17, 2, 117, 63, 100, 104, 38, 125, 48, 36)
| 115 | 83 | 35 | 89 | 2 | 1 | 102 | 31 | 119 | 17 | 2 | 117 | 63 | 100 | 104 | 38 | 125 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | palindrome | is | a | number | that | reads | the same | forward | and | backward | , such as <num> | . how many | odd , <num> - | digit | numbers | are | palindromes | ? <eos> |
| a | palindrome | is | a | number | that | reads | the same | forward | and | backward | , such as <num> | . how many | odd , <num> - | digit | numbers | are | palindromes | ? <eos> |
| a | palindrome | is | a | number | that | reads | the same | forward | and | backward | , such as <num> | . how many | odd , <num> - | digit | numbers | are | palindromes | ? <eos> |
| a | palindrome | is | a | number | that | reads | the same | forward | and | backward | , such as <num> | . how many | odd , <num> - | digit | numbers | are | palindromes | ? <eos> |

### Top-13 (4 samples using it): (121, 4, 56, 83, 35, 84, 64, 71, 23, 22, 64, 71, 23, 40, 102, 31, 119, 11, 2, 126)
| 121 | 4 | 56 | 83 | 35 | 84 | 64 | 71 | 23 | 22 | 64 | 71 | 23 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | speed | of a | car | is | <num> | km | in the first | hour | and <num> | km | in the second | hour | . what | is | the average | speed | of the | car | ? <eos> |
| the | speed | of a | car | is | <num> | km | in the first | hour | and <num> | km | in the second | hour | . what | is | the average | speed | of the | car | ? <eos> |
| the | speed | of a | car | is | <num> | km | in the first | hour | and <num> | km | in the second | hour | . what | is | the average | speed | of the | car | ? <eos> |
| the | speed | of a | car | is | <num> | km | in the first | hour | and <num> | km | in the second | hour | . what | is | the average | speed | of the | car | ? <eos> |

### Top-14 (4 samples using it): (121, 4, 56, 83, 35, 129, 108, 2, 30, 77, 71, 23, 20, 27, 130, 125, 124, 44, 94, 71, 23, 81)
| 121 | 4 | 56 | 83 | 35 | 129 | 108 | 2 | 30 | 77 | 71 | 23 | 20 | 27 | 130 | 125 | 124 | 44 | 94 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | population | of a | village | is | <num> | . it | increases | annually at the | rate | of <num> | % | p | . a | . what | will | be | its | population | after <num> | years | ? <eos> |
| the | population | of a | town | is | <num> | . it | decreases | annually at the | rate | of <num> | % | p | . a | . what | will | be | its | population | after <num> | years | ? <eos> |
| the | population | of a | town | is | <num> | . it | increases | annually at the | rate | of <num> | % | p | . a | . what | will | be | its | population | after <num> | years | ? <eos> |
| the | population | of a | town | is | <num> | . it | decreases | annually at the | rate | of <num> | % | p | . a | . what | will | be | its | population | after <num> | years | ? <eos> |

### Top-15 (4 samples using it): (115, 38, 125, 25, 4, 56, 94, 71, 23, 108, 105, 84, 64, 91, 0, 89, 2, 7, 9, 29, 101, 38, 125, 41)
| 115 | 38 | 125 | 25 | 4 | 56 | 94 | 71 | 23 | 108 | 105 | 84 | 64 | 91 | 0 | 89 | 2 | 7 | 9 | 29 | 101 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | train | covers | a | distance | of <num> | km | in <num> | min | . if it | takes | <num> | sec | to | pass | a | telegraph | post | , then the | length | of the | train | is | ? <eos> |
| a | train | covers | a | distance | of <num> | km | in <num> | min | . if it | takes | <num> | sec | to | pass | a | telegraph | post | , then the | length | of the | train | is | ? <eos> |
| a | train | covers | a | distance | of <num> | km | in <num> | min | . if it | takes | <num> | sec | to | pass | a | telegraph | post | , then the | length | of the | train | is | ? <eos> |
| a | train | covers | a | distance | of <num> | km | in <num> | min | . if it | takes | <num> | sec | to | pass | a | telegraph | post | , then the | length | of the | train | is | ? <eos> |

### Top-16 (3 samples using it): (127, 36)
| 127 | 36 |
| - | - |
| <num> x <num> = | ? <eos> |
| <num> x <num> = | ? <eos> |
| <num> + <num> = | ? <eos> |

### Top-17 (3 samples using it): (100, 81)
| 100 | 81 |
| - | - |
| <num> \xc3\x97 <num> = | ? <eos> |
| <num> \xc3\x97 <num> = | ? <eos> |
| <num> * <num> = | ? <eos> |

### Top-18 (3 samples using it): (115, 118, 44, 2, 16, 36)
| 115 | 118 | 44 | 2 | 16 | 36 |
| - | - | - | - | - | - |
| <num> | is | what | percent | of <num> | ? <eos> |
| <num> | is | what | percent | of <num> | ? <eos> |
| <num> | is | what | percent | of <num> | ? <eos> |

### Top-19 (3 samples using it): (8, 38, 125, 64, 16, 36)
| 8 | 38 | 125 | 64 | 16 | 36 |
| - | - | - | - | - | - |
| how many distinct prime | numbers | are | factors | of <num> | ? <eos> |
| how many different positive | integers | are | factors | of <num> | ? <eos> |
| how many different positive | integers | are | factors | of <num> | ? <eos> |

### Top-20 (3 samples using it): (102, 31, 119, 11, 110, 17, 2, 62, 2, 126)
| 102 | 31 | 119 | 11 | 110 | 17 | 2 | 62 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - |
| <unk> | a | speed | of <num> | kmph | in | meters | per | second | ? <eos> |
| <unk> | a | speed | of <num> | kmph | in | meters | per | second | ? <eos> |
| <unk> | a | speed | of <num> | kmph | in | meters | per | second | ? <eos> |

### Top-21 (3 samples using it): (102, 31, 119, 1, 102, 31, 119, 11, 2, 69, 16, 36)
| 102 | 31 | 119 | 1 | 102 | 31 | 119 | 11 | 2 | 69 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| find | the greatest | number | which | leaves | the same | remainder | when it | divides | <num> , <num> | and <num> | . <eos> |
| find | the greatest | number | which | leaves | the same | remainder | when it | divides | <num> , <num> | and <num> | . <eos> |
| find | the greatest | number | which | leaves | the same | remainder | when it | divides | <num> , <num> | and <num> | . <eos> |

### Top-22 (3 samples using it): (21, 125, 34, 71, 23, 11, 2, 54, 38, 125, 129, 85, 102, 31, 119, 126)
| 21 | 125 | 34 | 71 | 23 | 11 | 2 | 54 | 38 | 125 | 129 | 85 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | is | subtracted | from <num> | % | of a | number | , the | result | is | <num> | . | find | the | number | ? <eos> |
| <num> | is | subtracted | from <num> | % | of a | number | , the | result | is | <num> | . | find | the | number | ? <eos> |
| <num> | is | subtracted | from <num> | % | of a | number | , the | result | is | <num> | . | find | the | number | ? <eos> |

### Top-23 (3 samples using it): (115, 83, 35, 90, 34, 117, 27, 2, 16, 36)
| 115 | 83 | 35 | 90 | 34 | 117 | 27 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - |
| what least | number | should | be | added | to <num> , | so that the sum | is | completely divisible by <num> | ? <eos> |
| what least | number | should | be | added | to <num> , | so that the sum | is | completely divisible by <num> | ? <eos> |
| what least | number | must | be | added | to <num> , | so that the sum | is | completely divisible by <num> | ? <eos> |

### Top-24 (3 samples using it): (102, 31, 119, 55, 10, 117, 69, 16, 36)
| 102 | 31 | 119 | 55 | 10 | 117 | 69 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| calculate | the | ratio | between x and y | if <num> % | of x equal | to <num> % | of y | ? <eos> |
| calculate | the | ratio | between x and y | if <num> % | of x equal | to <num> % | of y | ? <eos> |
| calculate | the | ratio | between x and y | if <num> % | of x equal | to <num> % | of y | ? <eos> |

### Top-25 (3 samples using it): (40, 102, 31, 119, 74, 27, 2, 102, 31, 119, 11, 2, 126)
| 40 | 102 | 31 | 119 | 74 | 27 | 2 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| what | is | the smallest positive | integer | x | such that <num> | x | is | the | cube | of a positive | integer | ? <eos> |
| what | is | the smallest positive | integer | x | such that <num> - | x | is | the | cube | of a positive | integer | ? <eos> |
| what | is | the smallest positive | integer | x | such that <num> + | x | is | the | cube | of a positive | integer | ? <eos> |

### Top-26 (3 samples using it): (71, 23, 107, 38, 125, 129, 107, 38, 125, 70, 83, 35, 129, 85, 102, 31, 119, 126)
| 71 | 23 | 107 | 38 | 125 | 129 | 107 | 38 | 125 | 70 | 83 | 35 | 129 | 85 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| in a | division | , | <unk> | is | <num> | , | <unk> | is | <num> and | quotient | is | <num> | . | find | the | remainder | . <eos> |
| in a | division | , | <unk> | is | <num> | , | <unk> | is | <num> and | quotient | is | <num> | . | find | the | remainder | . <eos> |
| in a | division | , | <unk> | is | <num> | , | <unk> | is | <num> and | quotient | is | <num> | . | find | the | remainder | . <eos> |

### Top-27 (3 samples using it): (121, 4, 56, 83, 34, 71, 23, 22, 64, 84, 64, 40, 102, 31, 119, 126)
| 121 | 4 | 56 | 83 | 34 | 71 | 23 | 22 | 64 | 84 | 64 | 40 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | sector | of a | circle | has radius | of <num> | cm | and central | angle | <num> | o | . | find | its | perimeter | ? <eos> |
| the | sector | of a | circle | has radius | of <num> | cm | and central | angle | <num> | o | . | find | its | perimeter | ? <eos> |
| the | sector | of a | circle | has radius | of <num> | cm | and central | angle | <num> | o | . | find | its | perimeter | ? <eos> |

### Top-28 (3 samples using it): (102, 31, 119, 17, 2, 112, 20, 27, 2, 74, 17, 2, 78, 14, 48, 36)
| 102 | 31 | 119 | 17 | 2 | 112 | 20 | 27 | 2 | 74 | 17 | 2 | 78 | 14 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| find | the | expenditure | on | <unk> | a well <num> | m | deep and of <num> | m | diameter | at | rs | . <num> per | cubic | meter | ? <eos> |
| find | the | expenditure | on | <unk> | a well <num> | m | deep and of <num> | m | diameter | at | rs | . <num> per | cubic | meter | ? <eos> |
| find | the | expenditure | on | <unk> | a well <num> | m | deep and of <num> | m | diameter | at | rs | . <num> per | cubic | meter | ? <eos> |

### Top-29 (3 samples using it): (115, 38, 125, 94, 71, 23, 18, 38, 125, 134, 18, 38, 125, 76, 2, 16, 36)
| 115 | 38 | 125 | 94 | 71 | 23 | 18 | 38 | 125 | 134 | 18 | 38 | 125 | 76 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | men | have | provisions | for <num> | days | . if <num> more | men | join | them | , for how many | days | will | the | provisions | last now | ? <eos> |
| <num> | men | have | provisions | for <num> | days | . if <num> more | men | join | them | , for how many | days | will | the | provisions | last now | ? <eos> |
| <num> | men | have | provisions | for <num> | days | . if <num> more | men | join | them | , for how many | days | will | the | provisions | last now | ? <eos> |

### Top-30 (3 samples using it): (115, 38, 125, 25, 49, 17, 2, 123, 130, 125, 22, 64, 91, 0, 129, 85, 102, 31, 119, 46, 0, 36)
| 115 | 38 | 125 | 25 | 49 | 17 | 2 | 123 | 130 | 125 | 22 | 64 | 91 | 0 | 129 | 85 | 102 | 31 | 119 | 46 | 0 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | student | chose | a | number | , | multiplied | it by <num> | , then | subtracted | <num> from the | result | and | got | <num> | . what | was | the | number | he | chose | ? <eos> |
| a | student | chose | a | number | , | multiplied | it by <num> | , then | subtracted | <num> from the | result | and | got | <num> | . what | was | the | number | he | chose | ? <eos> |
| a | student | chose | a | number | , | multiplied | it by <num> | , then | subtracted | <num> from the | result | and | got | <num> | . what | was | the | number | he | chose | ? <eos> |

### Top-31 (3 samples using it): (115, 38, 125, 104, 38, 125, 17, 2, 84, 64, 34, 71, 23, 68, 18, 38, 125, 38, 125, 77, 71, 23, 48, 36)
| 115 | 38 | 125 | 104 | 38 | 125 | 17 | 2 | 84 | 64 | 34 | 71 | 23 | 68 | 18 | 38 | 125 | 38 | 125 | 77 | 71 | 23 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | can | give | b <num> | meters | start | and | c | <num> | meters | start | in a | kilometer | race | . how much | start | can | b | give | c | in a | kilometer | race | ? <eos> |
| a | can | give | b <num> | meters | start | and | c | <num> | meters | start | in a | kilometer | race | . how much | start | can | b | give | c | in a | kilometer | race | ? <eos> |
| a | can | give | b <num> | meters | start | and | c | <num> | meters | start | in a | kilometer | race | . how much | start | can | b | give | c | in a | kilometer | race | ? <eos> |

### Top-32 (3 samples using it): (115, 104, 38, 125, 124, 44, 2, 7, 54, 38, 125, 129, 108, 2, 69, 85, 102, 31, 119, 11, 2, 126)
| 115 | 104 | 38 | 125 | 124 | 44 | 2 | 7 | 54 | 38 | 125 | 129 | 108 | 2 | 69 | 85 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| when positive | integer | x | is | divided | by positive | integer | y | , the | remainder | is | <num> | . if | x | / y = <num> | , what | is | the | value | of | y | ? <eos> |
| when positive | integer | x | is | divided | by positive | integer | y | , the | remainder | is | <num> | . if | x | / y = <num> | , what | is | the | value | of | y | ? <eos> |
| when positive | integer | x | is | divided | by positive | integer | y | , the | remainder | is | <num> | . if | x | / y = <num> | , what | is | the | value | of | y | ? <eos> |

### Top-33 (3 samples using it): (115, 83, 35, 84, 64, 91, 0, 34, 120, 114, 112, 18, 38, 125, 1, 102, 31, 119, 11, 2, 74, 36)
| 115 | 83 | 35 | 84 | 64 | 91 | 0 | 34 | 120 | 114 | 112 | 18 | 38 | 125 | 1 | 102 | 31 | 119 | 11 | 2 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | train | is | <num> | meter | long | is | running | at a speed | of <num> km | / hour | . in what | time | will | it | pass | a | bridge | of <num> | meter | length | ? <eos> |
| a | train | is | <num> | meter | long | is | running | at a speed | of <num> km | / hour | . in what | time | will | it | pass | a | bridge | of <num> | meter | length | ? <eos> |
| a | train | is | <num> | meter | long | is | running | at a speed | of <num> km | / hour | . in what | time | will | it | pass | a | bridge | of <num> | meter | length | ? <eos> |

### Top-34 (3 samples using it): (115, 83, 56, 83, 116, 14, 107, 38, 125, 70, 83, 105, 46, 0, 84, 64, 22, 64, 112, 40, 102, 31, 119, 17, 2, 126)
| 115 | 83 | 56 | 83 | 116 | 14 | 107 | 38 | 125 | 70 | 83 | 105 | 46 | 0 | 84 | 64 | 22 | 64 | 112 | 40 | 102 | 31 | 119 | 17 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | reduction | of <num> | % | in the | price | of | oil | enables | a | house | wife | to | obtain | <num> | kgs | more for | rs | . <num> | , what | is | the reduced | price | for | kg | ? <eos> |
| a | reduction | of <num> | % | in the | price | of | oil | enables | a | house | wife | to | obtain | <num> | kgs | more for | rs | . <num> | , what | is | the reduced | price | for | kg | ? <eos> |
| a | reduction | of <num> | % | in the | price | of | oil | enables | a | house | wife | to | obtain | <num> | kgs | more for | rs | . <num> | , what | is | the reduced | price | for | kg | ? <eos> |

### Top-35 (3 samples using it): (115, 83, 35, 124, 44, 94, 71, 23, 130, 125, 39, 2, 44, 2, 18, 38, 125, 84, 64, 91, 0, 84, 64, 22, 64, 40, 102, 31, 119, 126)
| 115 | 83 | 35 | 124 | 44 | 94 | 71 | 23 | 130 | 125 | 39 | 2 | 44 | 2 | 18 | 38 | 125 | 84 | 64 | 91 | 0 | 84 | 64 | 22 | 64 | 40 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | persons | can | <unk> | a | road | in <num> | days | , | working | <num> | hours | a | day | . in how many | days | will | <num> | persons | , | working | <num> | hours | a | day | , | complete | the | work | ? <eos> |
| <num> | persons | can | <unk> | a | road | in <num> | days | , | working | <num> | hours | a | day | . in how many | days | will | <num> | persons | , | working | <num> | hours | a | day | , | complete | the | work | ? <eos> |
| <num> | persons | can | <unk> | a | road | in <num> | days | , | working | <num> | hours | a | day | . in how many | days | will | <num> | persons | , | working | <num> | hours | a | day | , | complete | the | work | ? <eos> |

### Top-36 (3 samples using it): (115, 83, 7, 9, 29, 101, 38, 125, 12, 99, 29, 101, 38, 125, 12, 23, 63, 4, 56, 83, 49, 17, 104, 38, 125, 48, 36)
| 115 | 83 | 7 | 9 | 29 | 101 | 38 | 125 | 12 | 99 | 29 | 101 | 38 | 125 | 12 | 23 | 63 | 4 | 56 | 83 | 49 | 17 | 104 | 38 | 125 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| in | town | x | , <num> | percent | of the | population | are | employed | , and <num> | percent | of the | population | are | employed | males | . what | percent | of the | employed | people | in | town | x | are | females | ? <eos> |
| in | town | x | , <num> | percent | of the | population | are | employed | , and <num> | percent | of the | population | are | employed | males | . what | percent | of the | employed | people | in | town | x | are | females | ? <eos> |
| in | town | x | , <num> | percent | of the | population | are | employed | , and <num> | percent | of the | population | are | employed | males | . what | percent | of the | employed | people | in | town | x | are | females | ? <eos> |

### Top-37 (3 samples using it): (129, 68, 54, 38, 125, 84, 64, 22, 64, 63, 2, 107, 38, 125, 42, 27, 2, 40, 102, 31, 119, 11, 2, 16, 36)
| 129 | 68 | 54 | 38 | 125 | 84 | 64 | 22 | 64 | 63 | 2 | 107 | 38 | 125 | 42 | 27 | 2 | 40 | 102 | 31 | 119 | 11 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| <num> | years | ago , | paula | was | <num> | times | as old as | karl | . in <num> | years | , | paula | will | be | twice as old as | karl | . what | is | the | sum | of their | ages | now | ? <eos> |
| <num> | years | ago , | paula | was | <num> | times | as old as | karl | . in <num> | years | , | paula | will | be | twice as old as | karl | . what | is | the | sum | of their | ages | now | ? <eos> |
| <num> | years | ago , | paula | was | <num> | times | as old as | karl | . in <num> | years | , | paula | will | be | twice as old as | karl | . what | is | the | sum | of their | ages | now | ? <eos> |

### Top-38 (3 samples using it): (79, 30, 20, 54, 38, 125, 79, 31, 119, 11, 110, 17, 2, 117, 7, 8, 38, 125, 70, 83, 34, 71, 23, 81)
| 79 | 30 | 20 | 54 | 38 | 125 | 79 | 31 | 119 | 11 | 110 | 17 | 2 | 117 | 7 | 8 | 38 | 125 | 70 | 83 | 34 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| running | at the same constant | rate | , <num> identical | machines | can | produce | a | total | of <num> | bottles | per | minute | . at this | rate | , how many | bottles | could | <num> such | machines | produce | in <num> | minutes | ? <eos> |
| running | at the same constant | rate | , <num> identical | machines | can | produce | a | total | of <num> | bottles | per | minute | . at this | rate | , how many | bottles | could | <num> such | machines | produce | in <num> | minutes | ? <eos> |
| running | at the same constant | rate | , <num> identical | machines | can | produce | a | total | of <num> | pens | per | minute | . at this | rate | , how many | pens | could | <num> such | machines | produce | in <num> | minutes | ? <eos> |

### Top-39 (3 samples using it): (115, 83, 35, 90, 30, 77, 71, 23, 18, 38, 125, 89, 2, 117, 54, 38, 125, 124, 44, 94, 71, 23, 40, 102, 31, 119, 74, 36)
| 115 | 83 | 35 | 90 | 30 | 77 | 71 | 23 | 18 | 38 | 125 | 89 | 2 | 117 | 54 | 38 | 125 | 124 | 44 | 94 | 71 | 23 | 40 | 102 | 31 | 119 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | watch | was | sold | at a | loss | of <num> | % | . if it | was | sold | for | rs | . <num> more | , there | would | have | been | a | gain | of <num> | % | . what | is | the | cost | price | ? <eos> |
| a | watch | was | sold | at a | loss | of <num> | % | . if it | was | sold | for | rs | . <num> more | , there | would | have | been | a | gain | of <num> | % | . what | is | the | cost | price | ? <eos> |
| a | watch | was | sold | at a | loss | of <num> | % | . if it | was | sold | for | rs | . <num> more | , there | would | have | been | a | gain | of <num> | % | . what | is | the | cost | price | ? <eos> |

### Top-40 (3 samples using it): (115, 83, 49, 17, 2, 107, 38, 125, 39, 2, 7, 63, 29, 101, 38, 125, 90, 34, 71, 23, 112, 1, 102, 31, 119, 11, 2, 11, 2, 126)
| 115 | 83 | 49 | 17 | 2 | 107 | 38 | 125 | 39 | 2 | 7 | 63 | 29 | 101 | 38 | 125 | 90 | 34 | 71 | 23 | 112 | 1 | 102 | 31 | 119 | 11 | 2 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a <num> | gallon | solution | of | salt | and | water | is | <num> | % | salt | . how many | gallons | of | water | must | be | added | to the | solution | in order | to | decrease | the | salt | to <num> | % | of the | volume | ? <eos> |
| a <num> | gallon | solution | of | salt | and | water | is | <num> | % | salt | . how many | gallons | of | water | must | be | added | to the | solution | in order | to | decrease | the | salt | to <num> | % | of the | volume | ? <eos> |
| a <num> | gallon | solution | of | salt | and | water | is | <num> | % | salt | . how many | gallons | of | water | must | be | added | to the | solution | in order | to | decrease | the | salt | to <num> | % | of the | volume | ? <eos> |

### Top-41 (3 samples using it): (115, 83, 80, 123, 72, 71, 23, 63, 118, 44, 94, 71, 23, 18, 38, 125, 70, 83, 35, 89, 2, 30, 48, 36)
| 115 | 83 | 80 | 123 | 72 | 71 | 23 | 63 | 118 | 44 | 94 | 71 | 23 | 18 | 38 | 125 | 70 | 83 | 35 | 89 | 2 | 30 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a and | b | invests | rs . <num> and | rs . <num> respectively | in a | business | . if a | doubles | his | capital | after <num> | months | . in what | ratio | should | a and | b | divide | that | year | ' s | profit | ? <eos> |
| a and | b | invests | rs . <num> and | rs . <num> respectively | in a | business | . if a | doubles | his | capital | after <num> | months | . in what | ratio | should | a and | b | divide | that | year | ' s | profit | ? <eos> |
| a and | b | invests | rs . <num> and | rs . <num> respectively | in a | business | . if a | doubles | his | capital | after <num> | months | . in what | ratio | should | a and | b | divide | that | year | ' s | profit | ? <eos> |

### Top-42 (3 samples using it): (115, 83, 35, 90, 106, 110, 17, 2, 9, 29, 101, 38, 125, 89, 2, 112, 68, 113, 63, 4, 56, 14, 107, 38, 125, 89, 2, 126)
| 115 | 83 | 35 | 90 | 106 | 110 | 17 | 2 | 9 | 29 | 101 | 38 | 125 | 89 | 2 | 112 | 68 | 113 | 63 | 4 | 56 | 14 | 107 | 38 | 125 | 89 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | glass | was | filled | with <num> | ounces | of | water | , and <num> | ounce | of the | water | evaporated | each | day | during a <num> - | day | period | . what | percent | of the original | amount | of | water | evaporated | during this | period | ? <eos> |
| a | glass | was | filled | with <num> | ounces | of | water | , and <num> | ounce | of the | water | evaporated | each | day | during a <num> - | day | period | . what | percent | of the original | amount | of | water | evaporated | during this | period | ? <eos> |
| a | glass | was | filled | with <num> | ounces | of | water | , and <num> | ounce | of the | water | evaporated | each | day | during a <num> - | day | period | . what | percent | of the original | amount | of | water | evaporated | during this | period | ? <eos> |

### Top-43 (3 samples using it): (115, 38, 125, 30, 110, 17, 2, 39, 2, 30, 2, 120, 114, 69, 18, 38, 125, 91, 0, 30, 77, 71, 23, 81)
| 115 | 38 | 125 | 30 | 110 | 17 | 2 | 39 | 2 | 30 | 2 | 120 | 114 | 69 | 18 | 38 | 125 | 91 | 0 | 30 | 77 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a and | b | go | around a circular | track | of | length | <num> | m | on a | cycle | at speeds | of <num> kmph | and <num> kmph | . after how much | time | will | they | meet | for the first | time | at the starting | point | ? <eos> |
| a and | b | go | around a circular | track | of | length | <num> | m | on a | cycle | at speeds | of <num> kmph | and <num> kmph | . after how much | time | will | they | meet | for the first | time | at the starting | point | ? <eos> |
| a and | b | go | around a circular | track | of | length | <num> | m | on a | cycle | at speeds | of <num> kmph | and <num> kmph | . after how much | time | will | they | meet | for the first | time | at the starting | point | ? <eos> |

### Top-44 (3 samples using it): (91, 0, 44, 94, 71, 23, 18, 38, 125, 84, 64, 18, 38, 125, 76, 2, 40, 102, 31, 119, 11, 2, 40, 102, 31, 119, 11, 2, 41)
| 91 | 0 | 44 | 94 | 71 | 23 | 18 | 38 | 125 | 84 | 64 | 18 | 38 | 125 | 76 | 2 | 40 | 102 | 31 | 119 | 11 | 2 | 40 | 102 | 31 | 119 | 11 | 2 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| there | are | <num> | people | in the | elevator | . their average | weight | is | <num> | lbs | . another | person | <unk> | the | elevator | , and | increases | the average | weight | to <num> | lbs | . what | is | the | weight | of the <num> th | person | . <eos> |
| there | are | <num> | people | in the | elevator | . their average | weight | is | <num> | lbs | . another | person | <unk> | the | elevator | , and | increases | the average | weight | to <num> | lbs | . what | is | the | weight | of the <num> th | person | . <eos> |
| there | are | <num> | people | in the | elevator | . their average | weight | is | <num> | lbs | . another | person | <unk> | the | elevator | , and | increases | the average | weight | to <num> | lbs | . what | is | the | weight | of the <num> th | person | . <eos> |

### Top-45 (3 samples using it): (121, 4, 56, 14, 107, 38, 125, 84, 64, 63, 29, 101, 38, 125, 84, 64, 27, 14, 107, 38, 125, 84, 64, 9, 29, 101, 38, 125, 41)
| 121 | 4 | 56 | 14 | 107 | 38 | 125 | 84 | 64 | 63 | 29 | 101 | 38 | 125 | 84 | 64 | 27 | 14 | 107 | 38 | 125 | 84 | 64 | 9 | 29 | 101 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the average | weight | of a , | b | and | c | is | <num> | kg | . if the average | weight | of a and | b | be | <num> | kg | and that of | b | and | c | be | <num> | kg | , then the | weight | of | b | is | : <eos> |
| the average | weight | of a , | b | and | c | is | <num> | kg | . if the average | weight | of a and | b | be | <num> | kg | and that of | b | and | c | be | <num> | kg | , then the | weight | of | b | is | : <eos> |
| the average | weight | of a , | b | and | c | is | <num> | kg | . if the average | weight | of a and | b | be | <num> | kg | and that of | b | and | c | be | <num> | kg | , then the | weight | of | b | is | : <eos> |

### Top-46 (2 samples using it): (33, 41)
| 33 | 41 |
| - | - |
| <num> / <num> | = <eos> |
| <num> / <num> | = <eos> |

### Top-47 (2 samples using it): (102, 31, 119, 11, 2, 41)
| 102 | 31 | 119 | 11 | 2 | 41 |
| - | - | - | - | - | - |
| find | the | sum | of first <num> natural | numbers | <eos> |
| find | the | sum | of first <num> natural | numbers | <eos> |

### Top-48 (2 samples using it): (115, 83, 23, 69, 57, 36)
| 115 | 83 | 23 | 69 | 57 | 36 |
| - | - | - | - | - | - |
| the | <unk> | ratio | of <num> : <num> | is | ? <eos> |
| the | <unk> | ratio | of <num> : <num> | is | ? <eos> |

### Top-49 (2 samples using it): (121, 4, 56, 14, 80, 126)
| 121 | 4 | 56 | 14 | 80 | 126 |
| - | - | - | - | - | - |
| the | average | of first <num> natural | numbers | is | ? <eos> |
| the | average | of first <num> even | numbers | is | ? <eos> |

### Top-50 (2 samples using it): (42, 55, 10, 41)
| 42 | 55 | 10 | 41 |
| - | - | - | - |
| <unk> | : <num> * <num> | + <num> * <num> | <eos> |
| solve below | question <num> x + | <num> = - <num> | <eos> |

### Top-51 (2 samples using it): (118, 44, 49, 17, 2, 123, 68, 69)
| 118 | 44 | 49 | 17 | 2 | 123 | 68 | 69 |
| - | - | - | - | - | - | - | - |
| solve | for | x | and | <unk> | : <num> | x | = <num> <eos> |
| solve | for | x | and | <unk> | : <num> | x | = <num> <eos> |

### Top-52 (2 samples using it): (100, 55, 10, 41)
| 100 | 55 | 10 | 41 |
| - | - | - | - |
| <unk> , <unk> | , <unk> , <unk> | , _ _ | <eos> |
| <num> , <num> | , x , - | <num> , - <num> | <eos> |

### Top-53 (2 samples using it): (115, 83, 116, 2, 39, 2, 16, 36)
| 115 | 83 | 116 | 2 | 39 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - |
| what | percent | of <num> | is | <num> | percent | of <num> | ? <eos> |
| what | percent | of <num> | is | <num> | percent | of <num> | ? <eos> |

### Top-54 (2 samples using it): (42, 114, 69, 16, 36)
| 42 | 114 | 69 | 16 | 36 |
| - | - | - | - | - |
| evaluate | : <num> - <num> | * <num> * <num> | = | ? <eos> |
| evaluate | : <num> - <num> | * <num> * <num> | = | ? <eos> |

### Top-55 (2 samples using it): (121, 4, 56, 14, 27, 2, 126)
| 121 | 4 | 56 | 14 | 27 | 2 | 126 |
| - | - | - | - | - | - | - |
| the | average | of first five prime | numbers | greater than <num> | is | ? <eos> |
| the | average | of first three prime | numbers | greater than <num> | is | ? <eos> |

### Top-56 (2 samples using it): (40, 102, 31, 119, 11, 2, 112, 81)
| 40 | 102 | 31 | 119 | 11 | 2 | 112 | 81 |
| - | - | - | - | - | - | - | - |
| what | is | the greatest prime | factor | of <num> | ^ | <num> - <num> | ? <eos> |
| what | is | the greatest prime | factor | of <num> | ^ | <num> - <num> | ? <eos> |

### Top-57 (2 samples using it): (118, 44, 2, 69, 85, 102, 31, 119, 126)
| 118 | 44 | 2 | 69 | 85 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - |
| half | a | number | plus <num> is <num> | . what | is | the | number | ? <eos> |
| half | a | number | plus <num> is <num> | . what | is | the | number | ? <eos> |

### Top-58 (2 samples using it): (8, 38, 125, 79, 91, 0, 70, 83, 35, 84, 64, 81)
| 8 | 38 | 125 | 79 | 91 | 0 | 70 | 83 | 35 | 84 | 64 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| how many | digits | are | required | to | number | a | book | containing | <num> | pages | ? <eos> |
| how many | digits | are | required | to | number | a | book | containing | <num> | pages | ? <eos> |

### Top-59 (2 samples using it): (121, 4, 56, 83, 35, 129, 85, 102, 31, 119, 126)
| 121 | 4 | 56 | 83 | 35 | 129 | 85 | 102 | 31 | 119 | 126 |
| - | - | - | - | - | - | - | - | - | - | - |
| the | sum | of two consecutive | integers | is | <num> | . | find | the | numbers | . <eos> |
| the | sum | of two consecutive | integers | is | <num> | . | find | the | numbers | . <eos> |

### Top-60 (2 samples using it): (115, 83, 107, 38, 125, 39, 2, 91, 0, 116, 2, 41)
| 115 | 83 | 107 | 38 | 125 | 39 | 2 | 91 | 0 | 116 | 2 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| two whole | numbers | whose | sum | is | <num> | can | not | be | in the | ratio | <eos> |
| two whole | numbers | whose | sum | is | <num> | can | not | be | in the | ratio | <eos> |

### Top-61 (2 samples using it): (40, 102, 31, 119, 116, 83, 35, 90, 16, 36)
| 40 | 102 | 31 | 119 | 116 | 83 | 35 | 90 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - |
| what | is | the | remainder | when <num> | ^ <num> | is | divided | by <num> | ? <eos> |
| what | is | the | remainder | when <num> | ^ <num> | is | divided | by <num> | ? <eos> |

### Top-62 (2 samples using it): (102, 31, 119, 11, 55, 10, 41)
| 102 | 31 | 119 | 11 | 55 | 10 | 41 |
| - | - | - | - | - | - | - |
| find | the | value | of ( <num> | + <num> / <num> | ) \xc3\x97 <num> | <eos> |
| find | the last | digit | of ( <num> | ^ <num> ) + | ( <num> ^ <num> | ) <eos> |

### Top-63 (2 samples using it): (8, 38, 125, 22, 64, 69, 126)
| 8 | 38 | 125 | 22 | 64 | 69 | 126 |
| - | - | - | - | - | - | - |
| how many positive | even | integers | less than <num> contain | digits | <num> or <num> | ? <eos> |
| how many positive | even | integers | less than <num> contain | digits | <num> or <num> | ? <eos> |

### Top-64 (2 samples using it): (121, 4, 56, 83, 62, 2, 69, 7)
| 121 | 4 | 56 | 83 | 62 | 2 | 69 | 7 |
| - | - | - | - | - | - | - | - |
| the | average | of first six prime | numbers | which | are | between <num> and <num> | is <eos> |
| the | average | of first six prime | numbers | which | are | between <num> and <num> | is <eos> |

### Top-65 (2 samples using it): (100, 55, 10, 100, 81)
| 100 | 55 | 10 | 100 | 81 |
| - | - | - | - | - |
| <num> x <num> | + <num> x <num> | + <num> x <num> | x <num> = | ? <eos> |
| if p / q | = <num> / <num> | , then <num> | p + q = | ? <eos> |

### Top-66 (2 samples using it): (22, 64, 69, 108, 2, 29, 101, 38, 125, 41)
| 22 | 64 | 69 | 108 | 2 | 29 | 101 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - |
| a <num> % | stock | yields <num> % | . the | market | value | of the | stock | is | : <eos> |
| a <num> % | stock | yields <num> % | . the | market | value | of the | stock | is | : <eos> |

### Top-67 (2 samples using it): (98, 119, 11, 2, 112, 9, 2, 16, 36)
| 98 | 119 | 11 | 2 | 112 | 9 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| how many | multiples | of <num> | are | less than <num> | , and also | multiples | of <num> | ? <eos> |
| how many | multiples | of <num> | are | less than <num> | , and also | multiples | of <num> | ? <eos> |

### Top-68 (2 samples using it): (53, 14, 27, 132, 64, 22, 64, 16, 36)
| 53 | 14 | 27 | 132 | 64 | 22 | 64 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| how many | integers | between <unk> and <unk> | have | tens | digit <num> and | units | digit <num> | ? <eos> |
| how many | integers | between <unk> and <unk> | have | tens | digit <num> and | units | digit <num> | ? <eos> |

### Top-69 (2 samples using it): (102, 31, 119, 46, 0, 90, 34, 61, 91, 0, 30, 48, 36)
| 102 | 31 | 119 | 46 | 0 | 90 | 34 | 61 | 91 | 0 | 30 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| find | the smallest | number | that | should | be | multiplied | with <num> | to | make | it a perfect | cube | . <eos> |
| find | the smallest | number | which | should | be | multiplied | with <num> | to | make | it a perfect | square | . <eos> |

### Top-70 (2 samples using it): (98, 2, 69, 7, 20, 27, 2, 16, 36)
| 98 | 2 | 69 | 7 | 20 | 27 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| how many positive | integers | less than <num> | are | multiples | of <num> but not | multiples | of <num> | ? <eos> |
| how many positive | integers | less than <num> | are | multiples | of <num> but not | multiples | of <num> | ? <eos> |

### Top-71 (2 samples using it): (40, 102, 31, 119, 74, 27, 2, 102, 31, 119, 11, 2, 41)
| 40 | 102 | 31 | 119 | 74 | 27 | 2 | 102 | 31 | 119 | 11 | 2 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| what | is | the smallest positive | integer | x | such that <num> | x | is | the | cube | of a positive | integer | <eos> |
| what | is | the smallest positive | integer | x | such that <num> - | x | is | the | cube | of a positive | integer | <eos> |

### Top-72 (2 samples using it): (40, 102, 31, 119, 117, 112, 2, 16, 36)
| 40 | 102 | 31 | 119 | 117 | 112 | 2 | 16 | 36 |
| - | - | - | - | - | - | - | - | - |
| what | is | the least | value | of x . so | that <num> x <num> | is | divisible by <num> | . <eos> |
| what | is | the least | value | of x . so | that <num> x <num> | is | divisible by <num> | . <eos> |

### Top-73 (2 samples using it): (66, 55, 10, 100, 18, 38, 125)
| 66 | 55 | 10 | 100 | 18 | 38 | 125 |
| - | - | - | - | - | - | - |
| <num> | , <num> , <num> | , <num> , <num> | , <num> , ( | . . . . | ) | <eos> |
| <num> | , <num> , <num> | , <num> , <num> | , <num> , ( | . . . . | ) | <eos> |

### Top-74 (2 samples using it): (8, 38, 125, 123, 112, 120, 114, 126)
| 8 | 38 | 125 | 123 | 112 | 120 | 114 | 126 |
| - | - | - | - | - | - | - | - |
| how much | interest | will | $ 10,000 earn | in <num> months | at an annual rate | of <num> % | ? <eos> |
| how much | interest | will | $ 10,000 earn | in <num> months | at an annual rate | of <num> % | ? <eos> |

### Top-75 (2 samples using it): (117, 85, 102, 31, 119, 11, 2, 27, 2, 69)
| 117 | 85 | 102 | 31 | 119 | 11 | 2 | 27 | 2 | 69 |
| - | - | - | - | - | - | - | - | - | - |
| in a throw of | dice what | is | the | probability | of | <unk> | <unk> <unk> <unk> | number | greater than <num> <eos> |
| in a throw of | dice what | is | the | probability | of | <unk> | <unk> <unk> <unk> | number | greater than <num> <eos> |

### Top-76 (2 samples using it): (40, 102, 31, 119, 74, 17, 2, 55, 10, 126)
| 40 | 102 | 31 | 119 | 74 | 17 | 2 | 55 | 10 | 126 |
| - | - | - | - | - | - | - | - | - | - |
| what | is | the smallest positive | perfect | square | that | is | divisible by <num> , | <num> , and <num> | ? <eos> |
| what | is | the smallest positive | perfect | square | that | is | divisible by <num> , | <num> , and <num> | ? <eos> |

### Top-77 (2 samples using it): (40, 102, 31, 119, 11, 2, 22, 64, 22, 64, 16, 36)
| 40 | 102 | 31 | 119 | 11 | 2 | 22 | 64 | 22 | 64 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| what | is | the | value | of <num> | x | ^ <num> \xe2\x88\x92 <num> | x | + <num> for | x | = <num> | ? <eos> |
| what | is | the | value | of <num> | x | ^ <num> \xe2\x88\x92 <num> | x | + <num> for | x | = <num> | ? <eos> |

### Top-78 (2 samples using it): (115, 83, 62, 83, 34, 71, 23, 72, 9, 29, 101, 38, 125, 41)
| 115 | 83 | 62 | 83 | 34 | 71 | 23 | 72 | 9 | 29 | 101 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| if a | sum | of | money | doubles itself | in <num> | years | at simple interest | , the | <unk> | per | annum | is | <eos> |
| if a | sum | of | money | doubles itself | in <num> | years | at simple interest | , the | <unk> | per | annum | is | <eos> |

### Top-79 (2 samples using it): (115, 83, 62, 83, 119, 11, 2, 34, 71, 23, 64, 40, 102, 31, 119, 74, 36)
| 115 | 83 | 62 | 83 | 119 | 11 | 2 | 34 | 71 | 23 | 64 | 40 | 102 | 31 | 119 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| an | article | with | cost | price | of <num> | is | sold | at <num> | % | profit | . what | is | the | selling | price | ? <eos> |
| an | article | with | cost | price | of <num> | is | sold | at <num> | % | profit | . what | is | the | selling | price | ? <eos> |

### Top-80 (2 samples using it): (130, 125, 49, 17, 2, 18, 38, 125, 129, 9, 2, 123, 33, 41)
| 130 | 125 | 49 | 17 | 2 | 18 | 38 | 125 | 129 | 9 | 2 | 123 | 33 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| what | is | rate | of | interest | if principal . | amount | be | <num> | , simple | interest | <num> and time | <num> year | . <eos> |
| what | is | rate | of | interest | if principal . | amount | be | <num> | , simple | interest | <num> and time | <num> year | . <eos> |

### Top-81 (2 samples using it): (115, 83, 35, 84, 64, 11, 2, 112, 108, 105, 46, 0, 46, 0, 16, 36)
| 115 | 83 | 35 | 84 | 64 | 11 | 2 | 112 | 108 | 105 | 46 | 0 | 46 | 0 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| an | <unk> | <unk> | <num> | % | of the | meters | as defective | . how many | will | he | <unk> | to | <unk> | <num> | ? <eos> |
| an | <unk> | <unk> | <num> | % | of the | meters | as defective | . how many | will | he | <unk> | to | <unk> | <num> | ? <eos> |

### Top-82 (2 samples using it): (115, 83, 35, 90, 120, 114, 18, 38, 125, 91, 0, 71, 23, 81)
| 115 | 83 | 35 | 90 | 120 | 114 | 18 | 38 | 125 | 91 | 0 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | car | is | running | at a speed | of <num> kmph | . what | distance | will | it | cover | in <num> | sec | ? <eos> |
| a | car | is | running | at a speed | of <num> kmph | . what | distance | will | it | cover | in <num> | sec | ? <eos> |

### Top-83 (2 samples using it): (115, 38, 125, 120, 114, 112, 108, 105, 46, 0, 71, 23, 81)
| 115 | 38 | 125 | 120 | 114 | 112 | 108 | 105 | 46 | 0 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | car | travels | at a speed | of <num> miles | per hour | . how far | will | it | travel | in <num> | hours | ? <eos> |
| a | car | travels | at a speed | of <num> miles | per hour | . how far | will | it | travel | in <num> | hours | ? <eos> |

### Top-84 (2 samples using it): (115, 2, 69, 102, 31, 119, 11, 2, 112, 68, 112, 99, 41)
| 115 | 2 | 69 | 102 | 31 | 119 | 11 | 2 | 112 | 68 | 112 | 99 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| if ( | t | - <num> ) | is | a | factor | of | t | ^ <num> - | <unk> | - <num> | , then k | = <eos> |
| if ( | t | - <num> ) | is | a | factor | of | t | ^ <num> - | <unk> | - <num> | , then k | = <eos> |

### Top-85 (2 samples using it): (115, 83, 34, 71, 23, 69, 33, 54, 38, 125, 129, 18, 38, 125, 41)
| 115 | 83 | 34 | 71 | 23 | 69 | 33 | 54 | 38 | 125 | 129 | 18 | 38 | 125 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| three | numbers | are | in the | ratio | <num> : <num> | : <num> | and their | average | is | <num> | . the largest | number | is | : <eos> |
| three | numbers | are | in the | ratio | <num> : <num> | : <num> | and their | average | is | <num> | . the largest | number | is | : <eos> |

### Top-86 (2 samples using it): (121, 4, 56, 83, 35, 84, 64, 107, 38, 125, 84, 64, 40, 102, 31, 119, 11, 2, 126)
| 121 | 4 | 56 | 83 | 35 | 84 | 64 | 107 | 38 | 125 | 84 | 64 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | diameter | of a cylindrical | tin | is | <num> | cm | and | height | is | <num> | cm | . | find | the | volume | of the | cylinder | ? <eos> |
| the | radius | of a cylindrical | vessel | is | <num> | cm | and | height | is | <num> | cm | . | find | the whole | surface | of the | cylinder | ? <eos> |

### Top-87 (2 samples using it): (115, 83, 35, 89, 2, 112, 40, 102, 31, 119, 17, 2, 69, 35, 90, 16, 36)
| 115 | 83 | 35 | 89 | 2 | 112 | 40 | 102 | 31 | 119 | 17 | 2 | 69 | 35 | 90 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| if | n | is | a prime | number | greater than <num> | , what | is | the | remainder | when | n | ^ <num> | is | divided | by <num> | ? <eos> |
| if | p | is | a prime | number | greater than <num> | , | find | the | remainder | when | p | ^ <num> + <num> | is | divided | by <num> | . <eos> |

### Top-88 (2 samples using it): (115, 83, 35, 124, 44, 94, 71, 23, 18, 38, 125, 84, 64, 34, 71, 23, 81)
| 115 | 83 | 35 | 124 | 44 | 94 | 71 | 23 | 18 | 38 | 125 | 84 | 64 | 34 | 71 | 23 | 81 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| if <num> | men | can | reap | <num> | hectares | in <num> | days | , then how many | hectares | can | <num> | men | reap | in <num> | days | ? <eos> |
| if <num> | men | can | reap | <num> | hectares | in <num> | days | , then how many | hectares | can | <num> | men | reap | in <num> | days | ? <eos> |

### Top-89 (2 samples using it): (121, 4, 56, 14, 101, 38, 125, 123, 40, 102, 31, 119, 11, 2, 48, 36)
| 121 | 4 | 56 | 14 | 101 | 38 | 125 | 123 | 40 | 102 | 31 | 119 | 11 | 2 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | ratio | of the | volumes | of two | cubes | is | <num> : <num> | . what | is | the | ratio | of their total | surface | areas | ? <eos> |
| the | ratio | of the | volumes | of two | cubes | is | <num> : <num> | . what | is | the | ratio | of their total | surface | areas | ? <eos> |

### Top-90 (2 samples using it): (91, 0, 84, 64, 9, 29, 101, 38, 125, 42, 123, 40, 102, 31, 119, 11, 2, 126)
| 91 | 0 | 84 | 64 | 9 | 29 | 101 | 38 | 125 | 42 | 123 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| after | decreasing | <num> | % | in the | price | of an | article | costs | rs | . <num> | . | find | the actual | cost | of an | article | ? <eos> |
| after | decreasing | <num> | % | in the | price | of an | article | costs | rs | . <num> | . | find | the actual | cost | of an | article | ? <eos> |

### Top-91 (2 samples using it): (53, 125, 70, 83, 84, 64, 91, 0, 78, 0, 1, 102, 31, 119, 11, 110, 17, 2, 126)
| 53 | 125 | 70 | 83 | 84 | 64 | 91 | 0 | 78 | 0 | 1 | 102 | 31 | 119 | 11 | 110 | 17 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| how long | does | a | train | <num> | m | long | travelling | at <num> kmph | takes | to | cross | a | bridge | of <num> | m | in | length | ? <eos> |
| how long | does | a | train | <num> | m | long | travelling | at <num> kmph | takes | to | cross | a | bridge | of <num> | m | in | length | ? <eos> |

### Top-92 (2 samples using it): (102, 31, 119, 87, 112, 26, 23, 69, 117, 18, 38, 125, 16, 36)
| 102 | 31 | 119 | 87 | 112 | 26 | 23 | 69 | 117 | 18 | 38 | 125 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| find | the | compound | interest | on $ <num> | for <num> | years | at <num> % | p . a | . if | <unk> | is | component yearly | ? <eos> |
| find | the | compound | interest | on $ <num> | for <num> | years | at <num> % | p . a | . if | <unk> | is | component yearly | ? <eos> |

### Top-93 (2 samples using it): (115, 38, 125, 30, 77, 71, 23, 11, 2, 40, 102, 31, 119, 11, 2, 126)
| 115 | 38 | 125 | 30 | 77 | 71 | 23 | 11 | 2 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | number <num> | is | equal to the | sum | of the | cubes | of two | integers | . what | is | the | product | of those | integers | ? <eos> |
| the | number <num> | is | equal to the | sum | of the | cubes | of two | integers | . what | is | the | product | of those | integers | ? <eos> |

### Top-94 (2 samples using it): (115, 38, 125, 42, 55, 10, 40, 102, 31, 119, 16, 36)
| 115 | 38 | 125 | 42 | 55 | 10 | 40 | 102 | 31 | 119 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - |
| if x and | y | are | integers | x - | = <num> | , what | is | the minimum possible | value | of xy | ? <eos> |
| if x and | y | are | integers | x - | = <num> | , what | is | the minimum possible | value | of xy | ? <eos> |

### Top-95 (2 samples using it): (115, 83, 84, 64, 91, 0, 114, 112, 68, 112, 40, 102, 31, 119, 11, 2, 126)
| 115 | 83 | 84 | 64 | 91 | 0 | 114 | 112 | 68 | 112 | 40 | 102 | 31 | 119 | 11 | 2 | 126 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | train | <num> | m | long | running | at <num> kmph | crosses a | platform | in <num> sec | . what | is | the | length | of the | platform | ? <eos> |
| a | train | <num> | m | long | running | at <num> kmph | crosses a | platform | in <num> sec | . what | is | the | length | of the | platform | ? <eos> |

### Top-96 (2 samples using it): (115, 83, 29, 101, 38, 125, 30, 23, 94, 71, 23, 40, 102, 31, 119, 17, 2, 74, 36)
| 115 | 83 | 29 | 101 | 38 | 125 | 30 | 23 | 94 | 71 | 23 | 40 | 102 | 31 | 119 | 17 | 2 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| if the | selling | price | of <num> | articles | is | same as the | cost | price | of <num> | articles | . | find | the | gain | or | loss | percentage | ? <eos> |
| if the | cost | price | of <num> | articles | is | same as the | selling | price | of <num> | articles | . | find | the | gain | or | loss | percentage | ? <eos> |

### Top-97 (2 samples using it): (115, 38, 125, 114, 69, 35, 84, 64, 22, 64, 40, 102, 31, 119, 11, 48, 36)
| 115 | 38 | 125 | 114 | 69 | 35 | 84 | 64 | 22 | 64 | 40 | 102 | 31 | 119 | 11 | 48 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| a | man | swims | downstream <num> km and | upstream <num> km | taking | <num> | hours | each | time | ; what | is | the | speed | of the | current | ? <eos> |
| a | man | swims | downstream <num> km and | upstream <num> km | taking | <num> | hours | each | time | ; what | is | the | speed | of the | current | ? <eos> |

### Top-98 (2 samples using it): (115, 83, 29, 101, 38, 125, 113, 27, 2, 124, 44, 2, 123, 40, 102, 31, 119, 74, 36)
| 115 | 83 | 29 | 101 | 38 | 125 | 113 | 27 | 2 | 124 | 44 | 2 | 123 | 40 | 102 | 31 | 119 | 74 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| the | cost | price | of a | radio | is | rs | . <num> and it | was | sold | for | rs | . <num> | , | find | the | loss | % | ? <eos> |
| the | cost | price | of a | radio | is | rs | . <num> and it | was | sold | for | rs | . <num> | , | find | the | loss | % | ? <eos> |

### Top-99 (2 samples using it): (115, 10, 100, 40, 102, 31, 119, 11, 2, 22, 64, 16, 36)
| 115 | 10 | 100 | 40 | 102 | 31 | 119 | 11 | 2 | 22 | 64 | 16 | 36 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| if <num> | a = <num> b | and ab \xe2\x89\xa0 <num> | , what | is | the | ratio | of a | / | <num> to b | / | <num> | ? <eos> |
| if <num> | a = <num> b | and ab \xe2\x89\xa0 <num> | , what | is | the | ratio | of a | / | <num> to b | / | <num> | ? <eos> |

### Top-100 (2 samples using it): (115, 83, 115, 38, 125, 55, 10, 100, 49, 17, 2, 33, 41)
| 115 | 83 | 115 | 38 | 125 | 55 | 10 | 100 | 49 | 17 | 2 | 33 | 41 |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| if x | ^ | <num> + | y | ^ | <num> = <num> and | xy = <num> , | then ( x \xe2\x88\x92 | y | ) | ^ | <num> | = <eos> |
| if x | ^ | <num> + | y | ^ | <num> = <num> and | xy = <num> , | then ( x \xe2\x88\x92 | y | ) | ^ | <num> | = <eos> |


