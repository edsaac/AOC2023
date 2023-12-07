# Wrong answer: 79612181
#               79608901
#               79610051
# Answer: 79613331

import re

with open("./day3/input.txt") as f:
    all_data = f.read().splitlines()

## Add margins to simplify indexing
all_data = [f".{l}." for l in all_data]  
N_COLS = len(all_data[0])

all_data = ["."*N_COLS] + all_data + ["."*N_COLS]
N_ROWS = len(all_data)

pattern_gear = re.compile(r"[*]")
valid_gears = list()
all_gears = list()

for i, line in enumerate(all_data):
    for mch in pattern_gear.finditer(line):
        gear_location = mch.start()
        gear_pair = list()

        ## Check left side:
        idx = 1
        while True:
            if line[gear_location - idx].isdigit(): 
                idx += 1
            else: 
                break
        if idx > 1:
            gear_pair.append(line[gear_location - idx + 1 : gear_location])

        ## Check right side:
        idx = 0
        while True:
            if line[gear_location + idx + 1].isdigit(): 
                idx += 1
            else: 
                break
        if idx > 0:
            gear_pair.append(line[gear_location + 1 : gear_location + idx + 1])

        ## Check top line
        for nums in re.finditer(r"[.](\d+)(?=[.])", all_data[i-1]):
            ## Find the closest match to the gear
            # print(nums, gear_location)
            if nums.start() - 1 < gear_location < nums.end() + 1: 
                gear_pair.append(nums.group(1))

        ## Check bottom line
        for nums in re.finditer(r"[.](\d+)(?=[.])", all_data[i+1]):
            ## Find the closest match to the gear
            if nums.start() - 1 < gear_location < nums.end() + 1: 
                gear_pair.append(nums.group(1))
    
        gear_pair = [int(g) for g in gear_pair]
        
        if len(gear_pair) == 2: valid_gears.append(gear_pair)
        all_gears.append(gear_pair)

        # print(f"L{i:<2d}: ", gear_pair)

    # print("")

# print(f"{len(valid_gears)=}")
# print(f"{len(all_gears)=}")

gear_ratios = [g1 * g2 for g1, g2 in valid_gears]
print("Answer:", sum(gear_ratios))
        

