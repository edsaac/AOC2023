
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

def jash(string: str):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

with open("day15/input.txt") as f:
    data = f.read().replace("\n","").split(",")


# print(jash("HASH"))
print("Answer: ", sum([jash(chunk) for chunk in data]))