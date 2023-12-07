from dataclasses import dataclass
from math import sqrt, floor, ceil

@dataclass
class Record:
    time: int
    distance: int

    def __post_init__(self):
        """
         distance = time_sailing * velocity
         time_sailing = time - time_holding
         velocity = time_holding
         -----------------------------------------
         distance = (time - time_holding) * time_holding 
                            ^^^^^^^^^^^^
                            Solve for this 
        """
        lower_bound = (self.time - sqrt(self.time**2 - (4*self.distance)))/2
        upper_bound = (self.time + sqrt(self.time**2 - (4*self.distance)))/2
        self.winner_times_range = (ceil(lower_bound), floor(upper_bound))

    @property
    def n_winnings(self):
        return self.winner_times_range[1] - self.winner_times_range[0] + 1
        

with open("./day6/input.txt") as f:
    record = Record(
        int(f.readline().split(":")[-1].strip().replace(" ","")),
        int(f.readline().split(":")[-1].strip().replace(" ",""))
    )

print(record, record.winner_times_range)
print("Answer: ", record.n_winnings)