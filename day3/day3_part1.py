#Answer: 543867

import re

with open("input.txt") as f:
    all_data = f.read().splitlines()

## Add margins to simplify indexing
all_data = [f".{line}." for line in all_data]  
N_COLS = len(all_data[0])

all_data = ["."*N_COLS] + all_data + ["."*N_COLS]
N_ROWS = len(all_data)


pattern = re.compile(r"\d+")
part_numbers = list()

for i, line in enumerate(all_data):
    for mch in pattern.finditer(line):

        ## Find symbols around each matched number
        top_pad = all_data[i-1][mch.start()-1 : mch.end()+1]
        lateral_pad = line[mch.start()-1] + line[mch.end()]
        bottom_pad = all_data[i+1][mch.start()-1 : mch.end()+1]
        padding = top_pad + lateral_pad + bottom_pad

        if len(set(padding)) > 1:
            part_numbers.append(mch.group())
        
print("Answer:", sum([int(s) for s in part_numbers]))
        

