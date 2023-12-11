# Answer: 6897

with open("day10/test.txt") as f:
    all_data = f.read().splitlines()

## Define directions
def update_dir(direction, pipe):
    match pipe:
        case "|": return complex(0, 1) if direction == complex(0,1) else complex(0, -1)
        case "-": return complex(1, 0) if direction == complex(1,0) else complex(-1, 0)
        case "F": return complex(0, 1) if direction == complex(-1, 0) else complex(1, 0)
        case "7": return complex(0, 1) if direction == complex(1, 0) else complex(-1, 0)
        case "L": return complex(1, 0) if direction == complex(0, 1) else complex(0, -1)
        case "J": return complex(-1, 0) if direction == complex(0, 1) else complex(0, -1) 

def get_pipe(whereami):
    return the_loop[int(whereami.imag)][int(whereami.real)]

## Find starting position
the_loop = list()

for i, line in enumerate(all_data):
    the_loop.append([*line])
    if "S" in line:
        whereami = complex(line.index("S"), i)
        print(whereami, get_pipe(whereami))

## Positive downwards to match the indices of the map
mydir = complex(0, 1)
vertices = [whereami]

while True:
    whereami += mydir
    vertices.append(whereami)
    pipe = get_pipe(whereami)
    mydir = update_dir(direction=mydir, pipe=pipe)
    print(whereami, pipe)
    if pipe == "S": 
        break

is_in = False
ntiles = 0
for i, line in enumerate(all_data):
    for chr in line:
        if chr in "|-F7LJ":
            ## Have to identify edges from crossings
            ## So this is not gonna work
            ntiles += 1
            is_in = not is_in
# print("Answer:", (len(vertices)-1)/2)
