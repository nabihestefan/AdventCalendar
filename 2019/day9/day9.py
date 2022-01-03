import sys
sys.path.append('../')
from intCode import *
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

print("Part 1: ", IntCode(ints,[1]).execute())
print("Part 2: ", IntCode(ints,[2]).execute())
