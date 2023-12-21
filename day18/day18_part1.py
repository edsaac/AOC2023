import itertools

def calculate_bounding_box(vertices:list[complex]):
    xx = [int(v.real) for v in vertices]
    yy = [int(v.imag) for v in vertices]
    return (min(xx), max(xx), min(yy), max(yy))

def draw_perimeter(vertices:list[complex]):
    xmin, xmax, ymin, ymax = calculate_bounding_box(vertices)
    grid = ["." * (xmax - xmin + 1)] * (ymax - ymin + 1)
    return [[*l] for l in grid]

def count_chars(field, char):
    count = 0
    for line in field:
        count += "".join(line).count(char)
    return count

## Constants
direction = {
    "R": complex(1 , 0),
    "L": complex(-1, 0),
    "D": complex(0 , 1),
    "U": complex(0 , -1),
}

with open("day18/input.txt") as f:
    data = f.readlines()

location = complex(0,0)
location_history = [location]

## Follow instructions
for instruction in data:
    where, value = instruction.split()[0], int(instruction.split()[1])
    for i in range(value):
        location += direction[where]
        location_history.append(location)

## Generate a field
field = draw_perimeter(location_history)

## 

xs = abs(min([int(loc.real) for loc in location_history]))
ys = abs(min([int(loc.imag) for loc in location_history]))


## Excavate the trenches
for loc in location_history:
    x,y = xs + int(loc.real), ys + int(loc.imag)
    field[y][x] = "#"

## Show result
for l in field: 
    print("".join(l))

print("~~~~~~~~~~~~~~")

## Excavate the interior
newfield = list()

for l in field:
    is_it_in = False
    templine = ""
    for char, chunk in itertools.groupby(l):
        n_chars = len(list(chunk))
        if char == "#":
            templine += "#" * n_chars
            if n_chars == 1:
                is_it_in = not is_it_in  #<- Cheap ray-tracing?

        elif char == ".":
            if is_it_in:
                templine += "X" * n_chars
            else:
                templine += "." * n_chars

    newfield.append([*templine])

## Show result
for l in newfield: 
    print("".join(l))

volume_interior = count_chars(newfield, "X")
volume_trench = count_chars(newfield, "#")
print("Answer: ", volume_interior + volume_trench)