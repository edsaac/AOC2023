# Answer: 6935

import re
from itertools import permutations  #<- This is very slow
from more_itertools import distinct_permutations

ptn_hash = re.compile("[#]+")
ptn_ques = re.compile("[?]+")

def to_numeric(record:str):
    return [cluster.end() - cluster.start() for cluster in ptn_hash.finditer(record)]

def count_valid(record:str, expected:list[int]):
    n_broken = sum(expected)
    n_unknown = record.count("?")
    n_known = record.count("#")

    iterable = "#"*(n_broken - n_known) + "."*(n_unknown - (n_broken - n_known))
    
    # This is too inefficient :(
    possibles = ["".join(p) for p in distinct_permutations(iterable)]
    mod_records = [""] * len(possibles)

    for k, possible in enumerate(possibles):
        # print(possible)
        j = 0
        for i, chr in enumerate(record): 
            if chr == "?":
                mod_records[k] += possible[j]
                j += 1
            else:
                mod_records[k] += chr
    
    count_valid = 0
    for mr in mod_records:
        if to_numeric(mr) == expected:
            count_valid += 1
    
    return count_valid

with open("day12/input.txt") as f:
    all_data = f.read().splitlines()

    accumulate = 0
    for line in all_data:
        record, expected = line.split()
        expected = [int(i) for i in expected.split(",")]
        print(record, expected, acc := count_valid(record, expected))
        accumulate += acc

print("Answer:", accumulate)
