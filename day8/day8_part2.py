# Answer: 20685524831999

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
        
whereami = list(filter(lambda x: x[-1]=="A", directions.keys()))
print(whereami)

# while not all([wh[-1] == "Z" for wh in whereami]):
#     # print(step, whereami)
#     for instruction in instructions:
#         whereami = [getattr(directions[wh], instruction) for wh in whereami]
#         step += 1
#         if all([wh[-1] == "Z" for wh in whereami]): break


from math import lcm

number_of_steps = list()
for wh in whereami:
    step = 0
    while wh[-1] != "Z":
        for instruction in instructions:
            wh = getattr(directions[wh], instruction)
            step += 1
            if wh[-1] == "Z": 
                number_of_steps.append(step)
                break

    print("Small answer = ", step, wh)

## That answer is not necessarily true...
print("Answer: ", lcm(*number_of_steps))