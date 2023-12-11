# Answer: 9370588

from dataclasses import dataclass
import re
from itertools import combinations

@dataclass
class Galaxy:
    location: complex

    def distance_to(self, other):
        delta = self.location - other.location
        return abs(delta.real) + abs(delta.imag)

with open("day11/input.txt") as f:
    universe = f.read().splitlines()

## Expanded map modification
expanded_universe = list()

for line in universe:
    expanded_universe.append(line)
    if line.count("#") == 0:
        expanded_universe.append(line)

flipped_universe = ["".join(list(i)) for i in zip(*expanded_universe)]
expanded_universe = list()

for line in flipped_universe:
    expanded_universe.append(line)
    if line.count("#") == 0:
        expanded_universe.append(line)

universe = ["".join(list(i)) for i in zip(*expanded_universe)] 

## Give galaxy coordinates

list_galaxies = list()

for i, line in enumerate(universe):
    for m in re.finditer("[#]", line):
        list_galaxies.append(
            Galaxy(complex(m.start(), i))
        )

sum_of_distances = 0
for g1, g2 in combinations(list_galaxies, 2):
    sum_of_distances += g1.distance_to(g2)

print("Answer: ", sum_of_distances)
