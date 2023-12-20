# Each cycle tilts the platform four times so that the rounded rocks roll 
# north, then west, then south, then east

# Answer: 104619

from typing import Literal
from functools import cache

def calculate_load(mirror:str):
    mirror = mirror.splitlines()
    mirror_size = len(mirror)
    
    total_load = 0
    for i,l in enumerate(mirror):
        n_rocks = l.count("O")
        distance = mirror_size - i
        load = n_rocks * distance
        total_load += load
    
    return total_load

@cache
def cycl(mirror: str):
    return tilt(tilt(tilt(tilt(mirror,"N"),"W"),"S"),"E")

@cache
def tilt(
        mirror:str, 
        direction=Literal["N", "W", "S", "E"]
    ):
    
    if not direction in [*"NSWE"]:
        raise ValueError("Direction must be N, S, W or E")

    mirror = mirror.splitlines()

    if direction == "N":
        order = {"O":0, ".":1, "#":2}
        transposed = ["".join(m) for m in list(zip(*mirror))]
    elif direction == "W":
        order = {"O":0, ".":1, "#":2}
        transposed = mirror
    elif direction == "E":
        order = {"O":1, ".":0, "#":2}
        transposed = mirror
    elif direction == "S":
        order = {"O":1, ".":0, "#":2}
        transposed = ["".join(m) for m in list(zip(*mirror))]
    
    rolled = list()
    for line in transposed:
        sorted_segments = list() 
        
        for segment in line.split("#"):
            sorted_segments.append("".join(sorted(segment, key=lambda x: order[x])))
        rolled.append("#".join(sorted_segments))

    if direction in ("E", "W"):
        return "\n".join(rolled)
    if direction in ("N", "S"):
        return "\n".join(["".join(m) for m in list(zip(*rolled))])

with open("day14/input.txt") as f:
    mirror = f.read().splitlines()

cycled = "\n".join(mirror)
dict_of_cycles = {hash(cycled): 0}

N_CYCLES = 1_000_000_000
for i in range(1, N_CYCLES + 1):
    cycled = cycl(cycled)

    if hash(cycled) in dict_of_cycles.keys():
        begin_repeat = dict_of_cycles.get(hash(cycled))
        repeat_repeat = i
        print(f" ~~ Cycle {i} is equal to cycle ", begin_repeat)
        # print(f"\nCycle {i}")
        # for l in cycled.splitlines(): 
        #     print(l)
        break
    else:
        dict_of_cycles[hash(cycled)] = i
        # # print(f"\nCycle {i}")
        # for l in cycled.splitlines(): 
        #     print(l)

len_repeat = repeat_repeat - begin_repeat

ACTUAL_CYCLES = begin_repeat + ((N_CYCLES - begin_repeat) % len_repeat)
print(f"Cycle {N_CYCLES} is equivalent to cycle {ACTUAL_CYCLES}")

cycled = "\n".join(mirror)
for i in range(1, ACTUAL_CYCLES + 1):
    cycled = cycl(cycled)

print("Answer: ", calculate_load(cycled))
