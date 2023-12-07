# There are no repeated numbers inside each list
#Answer: 21088

from dataclasses import dataclass

with open("./day4/input.txt") as f:
    all_data = f.read().splitlines()


@dataclass
class Card:
    id: int
    winning: list[int]
    scratched: list[int]
    
    def __post_init__(self):
        self.intersection = list(set(self.winning) & set(self.scratched))
        self.prize = 0 if len(self.intersection) == 0 else 2**(len(self.intersection) - 1)

list_of_cards = list()

for line in all_data:
    id = int(line.split(":")[0].split()[-1])
    winning, scratched = line.split(":")[1].split("|")
    card = Card(id, winning.strip().split(), scratched.strip().split())
    list_of_cards.append(card)
    print(id, card.intersection, card.prize)

print("Answer: ", sum([p.prize for p in list_of_cards]))