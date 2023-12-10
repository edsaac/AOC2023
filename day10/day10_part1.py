# Answer: 6897

with open("day10/input.txt") as f:
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
    return themap[int(whereami.imag)][int(whereami.real)]

## Find starting position
themap = list()
for i, line in enumerate(all_data):
    themap.append([*line])
    if "S" in line:
        whereami = complex(line.index("S"), i)
        print(whereami, get_pipe(whereami))

## Positive downwards to match the indices of the map
mydir = complex(0, 1)
step = 0

while True:
    whereami += mydir
    step += 1
    pipe = get_pipe(whereami)
    mydir = update_dir(direction=mydir, pipe=pipe)
    print(step, whereami, pipe)
    if pipe == "S": break

print("Answer:", step/2)