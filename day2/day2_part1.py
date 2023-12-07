# There are only 12 red cubes, 13 green cubes, and 14 blue cubes
# Answer: 1853

from dataclasses import dataclass
import re

with open("input.txt") as f:
    all_data = f.read()

pattern_id = re.compile(r"\s(\d+)[:]")
pattern_red = re.compile(r"(\d+) red")
pattern_green = re.compile(r"(\d+) green")
pattern_blue = re.compile(r"(\d+) blue")

@dataclass
class Subset:
    red: int = 0
    green: int = 0
    blue: int = 0

SUBSETMAX = Subset(12, 13, 14)

@dataclass
class Game:
    id: int
    subsets: list[Subset]
    possible: bool = True

    def __post_init__(self):
        self.check_if_possible()

    def check_if_possible(self):
        for subset in self.subsets:
            if subset.red > SUBSETMAX.red or subset.green > SUBSETMAX.green or subset.blue > SUBSETMAX.blue: 
                self.possible = False
                break

def main():
    list_of_games = list()

    for line in all_data.splitlines():
        
        game_id = int(pattern_id.search(line).group(1))
        subset_list = list()

        for textset in line.split(":")[-1].split(";"):
            
            if (reds := pattern_red.search(textset)):
                reds = int(reds.group(1))
            else: 
                reds = 0

            if (greens := pattern_green.search(textset)):
                greens = int(greens.group(1))
            else: 
                greens = 0
            
            if (blues := pattern_blue.search(textset)):
                blues = int(blues.group(1))
            else: 
                blues = 0
            
            subset_list.append(
                Subset(reds, greens, blues)
            )

        list_of_games.append(
            Game(game_id, subset_list)
        )

        # if game_id == 6:        
        # print(Game(game_id, subset_list))

    print("Answer: ", sum([game.id for game in list_of_games if game.possible]))

if __name__ == "__main__":
    main()
# print(all_data)