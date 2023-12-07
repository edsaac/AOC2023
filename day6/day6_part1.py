from dataclasses import dataclass
from functools import reduce

@dataclass
class Record:
    time: int
    distance: int

    def __post_init__(self):
        self.winning_strategies = list()
        for t0 in range(self.time):
            d = (self.time - t0) * t0
            if d > self.distance:
                self.winning_strategies.append(t0)
    
    @property
    def n_winnings(self):
        return len(self.winning_strategies)
        

with open("./day6/input.txt") as f:
    times = map(int, f.readline().split(":")[-1].strip().split())
    distances = map(int, f.readline().split(":")[-1].strip().split())

list_of_records = [Record(t,d) for t,d in zip(times,distances)]

for record in list_of_records:
    print(record, record.n_winnings)

print("Answer: ", reduce(lambda x,y: x*y, [r.n_winnings for r in list_of_records]))