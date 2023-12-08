import sys
sys.path.append("../")
from intCode import IntCode
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

def getHullDamage(ints, script):
    scriptList = list(map(ord, list('\n'.join(script) + '\n')))
    comp = IntCode(ints[:], scriptList)
    image = []
    while True:
        output = comp.run()
        if output!= None and output > 127: return output


def part1(ints):
    script = [
        'NOT A T',
        'NOT C J',
        'AND D J',
        'OR T J',
        'WALK'
    ]
    return getHullDamage(ints[:], script)

def part2(ints):
    script = [
        'NOT C J',
        'AND D J',
        'AND H J',
        'NOT B T',
        'AND D T',
        'OR T J',
        'NOT A T',
        'OR T J',
        'RUN'
    ]
    return getHullDamage(ints[:], script)

print("Part 1: ", part1(ints[:]))
print("Part 2: ", part2(ints[:]))
