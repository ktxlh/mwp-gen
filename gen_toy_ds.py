from itertools import permutations, combinations
# See https://www.geeksforgeeks.org/permutation-and-combination-in-python/ 

fields = {"V":"grow grew grows used use uses put puts did do does were was am is are",
          "ARG0":"Kate",
          "ARG1":"apples bananas",
          "ARG2":"apples bananas",
          "ARG3":"basket",
          "ARG4":"games",
          "ARGM-TMP":"today",
          "ARGM-LOC":"park"}
for k,v in list(fields.items()):
    fields[k] = v.split()

START = "__start#__"
END = "__end#__"
pass