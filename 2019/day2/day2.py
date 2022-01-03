import sys
sys.path.append('../')
from intCode import *
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints =  [int(a) for a in f.readlines()[0].split(",")]

def execute(ints, noun, verb):
    part1 = IntCode(ints)
    part1.set(1,noun)
    part1.set(2,verb)
    part1.execute()
    return part1.program[0]

print("Part 1: ", execute(ints[:],12,2))


for noun in range(100):
    for verb in range(100):
         if execute(ints[:],noun,verb) == 19690720:
             print("Part 2: ", 100*noun+verb)
             exit()
