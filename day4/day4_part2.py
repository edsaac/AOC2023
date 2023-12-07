#Answer: 6874754

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
        self.prize = len(self.intersection)
        self.n_copies = 1

dict_of_cards = dict()

for line in all_data:
    id = int(line.split(":")[0].split()[-1])
    winning, scratched = line.split(":")[1].split("|")
    card = Card(id, winning.strip().split(), scratched.strip().split())
    dict_of_cards[id] = card

for id, card in dict_of_cards.items():
    for j in range(card.n_copies):
        for i in range(card.prize):
            dict_of_cards[id + i + 1].n_copies += 1

for id, card in dict_of_cards.items():
    print(id, card.n_copies)

print("Answer: ", sum([p.n_copies for p in dict_of_cards.values()]))