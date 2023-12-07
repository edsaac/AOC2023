## Answer is 54649
import re

with open("input.txt") as f:
    all_data = f.read()

## Common replacements
written_numbers =  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
replacement_numbers = [*"123456789"]

## Edge cases
written_numbers = ["eightwo", "eighthree", "twone", "sevenine", "oneight", "threeight", "fiveight", "nineight"] + written_numbers
replacement_numbers = ["82", "83", "21", "79", "18", "38", "58", "98"] + replacement_numbers

results = list()

for i, line in enumerate(all_data.splitlines()):
    
    # print(line)
    first_number = True
    results.append([None,None])
    
    for written_number, number in zip(written_numbers, replacement_numbers):
        line = re.sub(written_number, number, line)
    
    for letter in line:
        if letter.isdigit() and first_number:
            results[i][0] = letter
            first_number = False
        elif letter.isdigit():
            results[i][1] = letter
    
    if results[i][1] is None:
        results[i][1] = results[i][0]

    # print("\t", line, results[i][0] + results[i][1])

print("Answer is",  sum([ int(result[0] + result[1]) for result in results]))