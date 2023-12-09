# Answer    1097

import numpy as np
from dataclasses import dataclass

@dataclass
class Prediction():
    readings: np.array
    
with open("day9/input.txt") as f:
    raw_data = f.readlines()
    readings = [list(map(int, line.split())) for line in raw_data]

stored_ans = 0

for reading in readings:
    below = [reading]
    
    for i in range(1, len(reading)):
        delta = np.diff(reading, i)
        below.append(delta.tolist())
        if not np.any(delta):
            break
    n_difs = len(below)

    below[-1].append(0)

    for i in range(n_difs - 2, -1, -1):
        below[i].append( below[i][0] - below[i+1][-1] )  ## Just changed an index here
    
    stored_ans += below[0][-1]

    for b in below:
        print(b)

print("Answer = ", stored_ans)