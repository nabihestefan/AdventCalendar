files = ['input.txt', 'inputTest.txt']
## Parsing
def parseInst(line):
    if "deal" in line:
        if "new" in line:
            return "new", 0
        else:
            return "increment", int(line[line.index("increment ")+10:])
    else:
        return "cut", int(line[line.index(" ")+1:])

with open(files[0], 'r') as f:
    insts =  [parseInst(a) for a in f.readlines()]


def newStack(deck): return deck[::-1]

def cutN(deck, n): return deck[n:] + deck[:n]

def incrementN(deck, n):
    deckLen = len(deck)
    newDeck = [0] * deckLen
    step = 0
    for i in range(deckLen):
        newDeck[step%deckLen] = deck[i]
        step += n
    return newDeck

deck = list(range(10007))

for inst, n in insts:
    if inst == "new":
        deck = newStack(deck[:])
    elif inst == "cut":
        deck = cutN(deck[:], n)
    elif inst == "increment":
        deck = incrementN(deck[:], n)

print("Part 1: ", deck.index(2019))

L = 119315717514047
card = 2020
T = 101741582076661

a,b = 1,0
for inst,n in insts[::-1]:
    if inst == "new":
        b += 1
        a *= -1
        b *= -1
    elif inst == "cut":
        b += n
    elif inst == "increment":
        p = pow(n, L-2,L)
        a *= p
        b *= p

print("Part 2: ", (
        pow(a, T, L) * 2020+b*(pow(a, T, L) +L- 1)*(pow(a-1, L-2, L)))%L)
