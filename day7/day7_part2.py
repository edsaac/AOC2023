# Answer: 251135960

from dataclasses import dataclass
from collections import Counter

CARDS = [*"J23456789TQKA"]
TYPES = ["fivekind", "fourkind", "fullhouse", "threekind", "twopair", "onepair", "highcard"]

@dataclass
class Hand:
    id: int
    cards: list[str]
    bid: int
    rank: int = -1

    def __post_init__(self):
        self.cnt = Counter(self.cards)
        self.typo = TYPES[self.get_type(self.cnt)]

        self.jk_cards = self.replace_joker()
        self.jk_cnt = Counter(self.jk_cards)
        self.jk_typo = TYPES[self.get_type(self.jk_cnt)]
    
    def replace_joker(self):
        if "J" not in self.cards:
            return self.cards

        else:
            match self.typo:
                case "highcard":
                    best_card = sorted(self.cards, key=lambda x: CARDS.index(x), reverse=True)[0]

                case ("onepair" | "threekind"):
                    if self.cnt.most_common(1)[0][0] == "J":
                        best_card = sorted(self.cards, key=lambda x: CARDS.index(x), reverse=True)[0]
                    else:
                        best_card = self.cnt.most_common(1)[0][0]

                case "twopair":
                    if "J" in (mc := [k[0] for k in self.cnt.most_common(2)]):
                        best_card = mc[1] if mc[0] == "J" else mc[0]
                    else:
                        best_card = sorted([k[0] for k in self.cnt.most_common(2)], key=lambda x: CARDS.index(x), reverse=True)[0]
            
                case ("fullhouse" | "fourkind"):
                    if self.cnt.most_common(1)[0][0] == "J":
                        best_card = self.cnt.most_common(2)[1][0]
                    else:
                        best_card = self.cnt.most_common(1)[0][0]

                case "fivekind":
                    best_card = "A"
            
            return [card if card != "J" else best_card for card in self.cards]
    
    @property
    def winning(self):
        return self.rank * self.bid
    
    def get_type(self, cnt):

        match len(cnt):
            case 1: return 0 
            case 2: return 1 if 4 in cnt.values() else 2
            case 3: return 3 if 3 in cnt.values() else 4
            case 4: return 5
            case 5: return 6

    def __gt__(self, other):
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return CARDS.index(self.cards[i]) > CARDS.index(other.cards[i])
    
    def __lt__(self, other):
        return not (self > other)

    def __eq__(self, other):
        return self.cards == other.cards


with open("./day7/input.txt") as f:
    all_data = f.read().splitlines()

list_of_hands = list()
dict_of_hands = {k: list() for k in TYPES}

for i, line in enumerate(all_data):
    cards, bid = line.split()
    hand = Hand(i, [*cards], int(bid))    
    list_of_hands.append(hand)
    dict_of_hands[hand.jk_typo].append(hand)

sorted_hands = {k:sorted(v, reverse=True) for k,v in dict_of_hands.items()}

rank = len(list_of_hands)
for dk, hands in sorted_hands.items():
    for hand in hands:
        hand.rank = rank
        rank -= 1
        # print(hand, hand.typo, hand.jk_cards, hand.jk_typo)

print("Answer: ", sum([h.winning for h in list_of_hands]))