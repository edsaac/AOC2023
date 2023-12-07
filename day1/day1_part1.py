# Answer = 54081

with open("input.txt") as f:
    all_data = f.read()

results = []

for i, line in enumerate(all_data.splitlines()):
    
    first_number = True
    results.append([None,None])

    for letter in line:
        if letter.isdigit() and first_number:
            results[i][0] = letter
            first_number = False
        elif letter.isdigit():
            results[i][1] = letter

    if results[i][1] is None:
        results[i][1] = results[i][0]

catted = [int(result[0] + result[1]) for result in results]
print(sum(catted))