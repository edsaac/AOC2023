from dataclasses import dataclass
from collections import namedtuple

## Constants
UP    = complex(0 ,-1)
DOWN  = complex(0 , 1)
LEFT  = complex(-1, 0)
RIGHT = complex(1 , 0)

dir_as_text = {UP:"UP", DOWN:"DOWN", LEFT:"LEFT", RIGHT:"RIGHT"}

with open("day16/test.txt") as f:
    DATA = [[*line] for line in f.read().splitlines()]

XMAX = len(DATA)
YMAX = len(DATA[0])

## Location
Position = namedtuple("Position", ["xy", "wh"])

## Beam
@dataclass
class Beam:
    xy:complex = complex(0,0)
    direction:complex = RIGHT
    ended:bool = False
    split:bool = False
    history:str = ""
    step:int = 0

    def __post_init__(self):
        self.subbeams = list()
        self.update_history()
    
    @property
    def instruction(self):
        x,y = int(self.xy.real), int(self.xy.imag)
        return DATA[y][x]

    @property
    def is_position_valid(self):
        x,y = int(self.xy.real), int(self.xy.imag)
        return not (x >= XMAX or y >= YMAX or x < 0 or y < 0)

    def run(self):
        while not self.ended:
            if self.is_position_valid:
                if self.instruction in ("|", "-"):
                    if self.step > 0:
                        self.split = True
                        self.ended = True

                    self.redirect(self.instruction)  #Update direction                
                    if not self.split:
                        self.advance()   #Update position
                        self.update_history()

                else:
                    self.redirect(self.instruction)  #Update direction
                    self.advance()   #Update position
                    self.update_history()

            else:
                self.ended = True
            
            if self.step > 100: break

    def update_history(self):
        position = Position(self.xy, dir_as_text.get(self.direction))
        self.history += f"{self.step} -> " + str(position)
    
    def advance(self):
        self.xy += self.direction
        self.step += 1

    def redirect(self, instruction):
        direction = self.direction
    
        if instruction == ".":
            ...

        elif instruction == "|":
            if self.direction in (LEFT, RIGHT):
                self.subbeams.append(Beam(self.xy, UP, ended=False, history=self.history))
                self.subbeams.append(Beam(self.xy, DOWN, ended=False, history=self.history))
            else:
                direction = self.direction
        
        elif instruction == "-":
            if self.direction in (UP, DOWN):
                self.subbeams.append(Beam(self.xy, RIGHT, ended=False, history=self.history))
                self.subbeams.append(Beam(self.xy, LEFT, ended=False, history=self.history))
            else:
                direction = self.direction
        
        elif instruction == "/":
            if   self.direction == RIGHT: direction = UP
            elif self.direction == LEFT:  direction = DOWN
            elif self.direction == UP:    direction = RIGHT
            elif self.direction == DOWN:  direction = LEFT

        elif instruction == "\\":
            if self.direction == RIGHT:   direction = DOWN
            elif self.direction == LEFT:  direction = UP
            elif self.direction == UP:    direction = LEFT
            elif self.direction == DOWN:  direction = RIGHT

        self.direction = direction

beam = Beam(complex(0,0), RIGHT)
beam.run()
print(beam.history)

for subbeam in beam.subbeams:
    subbeam.run()
    print(subbeam.history)

# for i in range(15):
#     beam.run()
#     print(i, beam)
