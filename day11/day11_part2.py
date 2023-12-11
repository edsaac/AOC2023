# Answer: 746207878188

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
    if line.count("#") == 0:
        expanded_universe.append("X"*len(line))
    else:
        expanded_universe.append(line)

flipped_universe = ["".join(list(i)) for i in zip(*expanded_universe)]
expanded_universe = list()

for line in flipped_universe:
    if line.count("#") == 0:
        expanded_universe.append("X"*len(line))
    else:
        expanded_universe.append(line)

universe = ["".join(list(i)) for i in zip(*expanded_universe)] 

## Give galaxy coordinates

list_galaxies = list()
big_gaps_y = 0
expansion_factor = 1e6

for i, line in enumerate(universe):
    if len(set(line)) == 1:
        big_gaps_y += 1
    
    else:
        for m in re.finditer("[#]", line):
            big_gaps_x = line[:m.start()].count("X")
            list_galaxies.append(
                Galaxy(
                    complex(
                        m.start() + big_gaps_x*expansion_factor - big_gaps_x, 
                        i + big_gaps_y*expansion_factor - big_gaps_y
                    )
                )
            )

sum_of_distances = 0
for g1, g2 in combinations(list_galaxies, 2):
    sum_of_distances += g1.distance_to(g2)

print("Answer: ", sum_of_distances)
