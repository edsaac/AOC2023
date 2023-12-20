from collections import namedtuple
from difflib import SequenceMatcher

Fold = namedtuple("Fold", ["location", "n_matches", "orientation"])

def find_fold(puzzle:list[str]):
    puzzle_size = len(puzzle[0])
    possible_folds = [[(p[:i], p[i:]) for p in puzzle] for i in range(1, puzzle_size)]
   
    corrected_list = list()

    for i, fold in enumerate(possible_folds, start=1):
        mirrored = [(l[::-1], r) for l,r in fold]
        len_left, len_right = len(mirrored[0][0]), len(mirrored[0][1])
        len_min = min(len_left, len_right)
        cropped = [(l[:len_min],r[:len_min]) for l,r in mirrored]
        
        smudges = 0
        for left,right in cropped:
            for l,r in zip(left, right):
                if l!=r: 
                    smudges += 1
        
        if smudges == 1:  
            corrected_list.append([(l,l) for l,_ in cropped])
        else: 
            corrected_list.append(cropped)

    is_valid_reflection = False
    most_likely_fold = -1
    reflected_cols = -1

    for i, fold in enumerate(corrected_list, start=1):

        is_valid_reflection = all([l==r for l,r in fold])
        
        if is_valid_reflection:
            if len_min > reflected_cols:
                most_likely_fold = i
                reflected_cols = len_min
            
    return most_likely_fold, reflected_cols


def puzzle_find_fold(puzzle:list[str]):

    vertical = Fold(*find_fold(puzzle), "Vertical")
    tr_puzzle = [i for i in zip(*puzzle)]
    horizontal = Fold(*find_fold(tr_puzzle), "Horizontal")

    if vertical.n_matches > horizontal.n_matches:
        return vertical
    elif vertical.n_matches < horizontal.n_matches:
        return horizontal
    else:
        return "Hard to know"


with open("day13/test.txt") as f:
    list_of_puzzles = list()
    buffer = ""
    
    for line in f:
        if line != "\n":
            buffer += line
        else:
            list_of_puzzles.append(buffer)
            buffer = ""
    
    list_of_puzzles.append(buffer)

list_solved = [puzzle_find_fold(p.splitlines()) for p in list_of_puzzles]
quantify = [p.location if p.orientation == "Vertical" else p.location * 100 for p in list_solved]

print(*list_solved, sep="\n")
print("Answer: ", sum(quantify))


