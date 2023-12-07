# Answer: 249726565

from dataclasses import dataclass
from collections import Counter

CARDS = [*"23456789TJQKA"]
TYPES = ["fivekind", "fourkind", "fullhouse", "threekind", "twopair", "onepair", "highcard"]

@dataclass
class Hand:
    id: int
    cards: list[str]
    bid: int
    rank: int = -1

    def __post_init__(self):
        self.typo = TYPES[self.get_type()]
    
    @property
    def winning(self):
        return self.rank * self.bid
    
    def get_type(self):
        cnt = Counter(self.cards)
        n_uniques = len(cnt)

        match n_uniques:
            case 1:
                return 0 
            case 2:          
                if 4 in cnt.values():
                     return 1
                else:
                     return 2
            case 3:
                if 3 in cnt.values():
                     return 3
                else:
                     return 4
            case 4:
                return 5
            case 5:
                return 6

    def __gt__(self, other):
        for i in range(len(cards)):
            if self.cards[i] != other.cards[i]:
                return CARDS.index(self.cards[i]) > CARDS.index(other.cards[i])
    
    def __lt__(self, other):
        for i in range(len(cards)):
            if self.cards[i] != other.cards[i]:
                return CARDS.index(self.cards[i]) < CARDS.index(other.cards[i])

    def __eq__(self, other):
        return self.cards == other.cards


with open("./day7/input.txt") as f:
    all_data = f.read().splitlines()

list_of_hands = list()
dict_of_hands = {k:list() for k in TYPES}

for i, line in enumerate(all_data):
    cards, bid = line.split()
    hand = Hand(i, [*cards], int(bid))
    
    list_of_hands.append(hand)
    dict_of_hands[hand.typo].append(hand)

sorted_hands = {k:sorted(v, reverse=True) for k,v in dict_of_hands.items()}

rank = len(list_of_hands)
for k, hands in sorted_hands.items():
    for hand in hands:
        hand.rank = rank
        rank -= 1
        # print(hand)

# for hand in list_of_hands:
#     print(hand)

print("Answer: ", sum([h.winning for h in list_of_hands]))