
order = {"O":0, ".":1, "#":2}

with open("day14/input.txt") as f:
    mirror = f.read().splitlines()
    transposed = ["".join(m) for m in list(zip(*mirror))]

rolled = list()
for line in transposed:
    sorted_segments = list() 
    
    for segment in line.split("#"):
        sorted_segments.append("".join(sorted(segment, key=lambda x: order[x])))
    rolled.append("#".join(sorted_segments))

mirror = ["".join(m) for m in list(zip(*rolled))]
mirror_size = len(mirror)

total_load = 0
for i,l in enumerate(mirror):
    n_rocks = l.count("O")
    distance = mirror_size - i
    load = n_rocks * distance
    print(l, n_rocks , distance, load)
    total_load += load

print("Answer: ", total_load)
# print(mirror, transposed)
