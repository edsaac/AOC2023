# Answer    17621

from collections import namedtuple

Direction = namedtuple("Direction", ("L", "R"))

with open("day8/input.txt") as f:
    instructions = f.readline().strip()
    print(f"There are {len(instructions) = }")
    all_data = f.read().splitlines()[1:]

    directions = dict()
    for data in all_data:
        node = data.split("=")[0].strip()
        left, right = data.split("=")[1].strip().replace("(","").replace(")","").replace(", ", ",").split(",")
        directions[node] = Direction(L = left, R = right)
        
whereami = "AAA"
step = 0

while whereami != "ZZZ":
    for instruction in instructions:
        whereami = getattr(directions[whereami], instruction)
        step += 1
        if whereami == "ZZZ": break

print("Answer = ", step, whereami)