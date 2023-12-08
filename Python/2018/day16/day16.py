files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    code, insts =  f.read().split("\n\n\n")

samples = []
for i in code.split("\n\n"):
    lines = i.split("\n")
    bef = eval(lines[0][lines[0].index(":")+2:])
    inst = [int(i) for i in lines[1].split(" ")]
    after = eval(lines[2][lines[2].index(":")+2:])
    samples.append((bef, inst, after))

instructions = [[int(i) for i in line.split(" ")] for line in insts.split("\n")[1:-1]]

def addr(reg,a,b,c): reg[c] = reg[b]+reg[a]
def addi(reg,a,b,c): reg[c] = b+reg[a]
def mulr(reg,a,b,c): reg[c] = reg[b]*reg[a]
def muli(reg,a,b,c): reg[c] = b*reg[a]
def banr(reg,a,b,c): reg[c] = reg[b]&reg[a]
def bani(reg,a,b,c): reg[c] = b&reg[a]
def borr(reg,a,b,c): reg[c] = reg[b]|reg[a]
def bori(reg,a,b,c): reg[c] = b|reg[a]
def setr(reg,a,b,c): reg[c] = reg[a]
def seti(reg,a,b,c): reg[c] = a
def gtir(reg,a,b,c): reg[c] = int(a > reg[b])
def gtri(reg,a,b,c): reg[c] = int(reg[a] > b)
def gtrr(reg,a,b,c): reg[c] = int(reg[a] > reg[b])
def eqir(reg,a,b,c): reg[c] = int(a == reg[b])
def eqri(reg,a,b,c): reg[c] = int(reg[a] == b)
def eqrr(reg,a,b,c): reg[c] = int(reg[a] == reg[b])

def test(bef, inst, after, op):
    r = bef[:]
    opCodes[op](r, inst[1], inst[2], inst[3])
    return r == after


opCodes = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
opDict = dict()

threePlus = 0
for bef, inst, after in samples:
    valid = 0
    for i in range(len(opCodes)):
        if test(bef, inst, after, i): valid+=1
    if valid >= 3: threePlus += 1

print("Part 1: ", threePlus)


while len(opCodes) > 0:
    for bef, inst, after in samples:
        valid = []
        for i in range(len(opCodes)):
            if test(bef, inst, after, i): valid.append(i)
        if len(valid)==1: opDict[inst[0]] = opCodes.pop(valid[0])

reg = [0,0,0,0]

for op,a,b,c in instructions: opDict[op](reg,a,b,c)

print("Part 2: ", reg[0])
