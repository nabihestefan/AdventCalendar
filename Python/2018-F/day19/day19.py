files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]
ip = int(lines[0][4])
insts = []
for i in lines[1:]:
    op = i[:4]
    a,b,c = map(int, i[5:].split(" "))
    insts.append((op,a,b,c))

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

opCodes = {"addr":addr, "addi":addi, "mulr":mulr, "muli":muli, "banr":banr,
            "bani":bani, "borr":borr, "bori":bori, "setr":setr, "seti":seti,
            "gtir":gtir, "gtri":gtri, "gtrr":gtrr, "eqir":eqir, "eqri":eqri,
            "eqrr":eqrr}

regs = [0,0,0,0,0,0]

while regs[ip] < len(insts):
    op,a,b,c = insts[regs[ip]]
    opCodes[op](regs, a,b,c)
    regs[ip] += 1

print("Part 1: ", regs[0])

#Explanation in part2.txt
num = 10551305
divisors = set()
for i in range(1,num//2):
    if num%i == 0:
        if i not in divisors:
            divisors.add(i)
            divisors.add(num//i)

print("Part 2: ", sum(divisors))
