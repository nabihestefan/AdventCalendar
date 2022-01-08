import sys
sys.path.append('../')
from intCode import *
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints =  [int(a) for a in f.readlines()[0].split(",")]

def run(ints, r1, r2, part2):
    iters = []
    for i in range(r1,r2):
        for j in range(r1,r2):
            for k in range(r1,r2):
                for l in range(r1,r2):
                    for m in range(r1,r2):
                        it = [i,j,k,l,m]
                        if len(it) == len(set(it)): iters.append(it)

    mX = 0
    for phases in iters:
        programs = [IntCode(ints,[phases[i]]) for i in range(5)]
        prev = 0
        if not part2:
            for program in programs:
                program.addInput(prev)
                prev = program.execute()
            mX = max(mX, prev)
        else:
            while all(not program.end for program in programs):
                for program in programs:
                    program.addInput(prev)
                    out = program.run()
                    if not program.end:
                        prev = out
            mX = max(mX, prev)
    return mX

print("Part 1: ", run(ints[:],0,5,False))
print("Part 2: ", run(ints[:],5,10,True))
