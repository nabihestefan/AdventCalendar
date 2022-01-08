import sys
sys.path.append("../")
from intCode import *
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

def isInter(grid, x,y):
    inter = True
    for nb in [(1,0), (0,1), (-1,0), (0,-1)]:
        inter = (inter and grid[(y+nb[0],x+nb[1])] == ord("#"))
    return inter

def dispGrid(grid,w,h):
    print('\n'.join(["".join(map(chr,[grid[(x,y)] for x in range(w)])) for y in range(h)]))

def makeMap(comp):
    x=y=w=h=0
    comp = IntCode(ints)
    grid = {}
    line = []
    char = comp.run()
    while char != None:
        if char == 10:
            y += 1
            w = max(w,x)
            x = 0
        else:
            grid[(x,y)] = char
            x += 1
        char = comp.run()
    h = y-1
    return grid, w, h

def p1(comp):
    grid,w,h = makeMap(comp)
    totalAlign = 0
    for y in range(1,w-1):
        for x in range(1,h-1):
            if isInter(grid,x,y):
                totalAlign += x*y
    dispGrid(grid,w,h)
    return totalAlign


def strToASCII(string):
    return list(map(ord,list(string)))

def p2(ints):
    # Found by hand
    main = "A,B,A,B,C,C,B,A,B,C"
    A = "L,4,R,8,L,6,L,10"
    B = "L,6,R,8,R,10,L,6,L,6"
    C = "L,4,L,4,L,10"
    inputs = [ord(x) for x in main] + [ord("\n")] + \
              [ord(x) for x in A] + [ord("\n")] + \
              [ord(x) for x in B] + [ord("\n")] + \
              [ord(x) for x in C] + [ord("\n")] + \
              [ord("n")] + [ord("\n")]
    comp = IntCode(ints, inputs)
    comp.set(0,2)
    outputs = []
    first = True
    while not comp.end:
        output = comp.output
        print(comp.pointer)
        if comp.pointer == 955:
            print(str(comp.program[comp.pointer]).zfill(5))
            Instr = comp.getInstr(comp.program[comp.pointer]%100)
            print()
            for arg in comp.getArgs(Instr.argNum):
                print(arg.val, arg.addr)
            print()
        outputs.append(output)
        comp.run()
        # print(len(inputs))
        if comp.end:
            print(comp.pointer)
            # print(len(outputs))
            break

    return output

print("Part 1: ", p1(IntCode(ints[:])))
print("Part 2: ", p2(ints[:]))
