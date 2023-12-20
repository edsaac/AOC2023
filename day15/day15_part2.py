from dataclasses import dataclass
from typing import Literal
from collections import OrderedDict

@dataclass
class Step:
    label: str
    number: int
    operation: Literal["=","-"]

    @property
    def box(self):
        return jash(self.label) 

def jash(string: str):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

#====================================================

boxes = {i:OrderedDict() for i in range(256)}

with open("day15/input.txt") as f:
    data = f.read().replace("\n","").split(",")

list_steps = list()

for step in data:
    if "=" in step:
        label, number = step.split("=")
        list_steps.append(Step(label, int(number), "="))
    elif "-" in step:
        label = step.split("-")[0]
        list_steps.append(Step(label, -1, "-"))

for step in list_steps:
    if step.operation == "=":
        boxes[step.box][step.label] = step.number
    elif step.operation == "-":
        if step.label in boxes[step.box]:
            del boxes[step.box][step.label]

focusing_power = 0
for box_number, box in boxes.items():
    for slot_number, focal in enumerate(box.values(), start=1):
        focusing_power += (box_number + 1) * slot_number * focal

print("Answer: ", focusing_power)