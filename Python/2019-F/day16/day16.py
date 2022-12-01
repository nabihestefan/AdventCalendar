files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints =  [int(a) for a in f.readlines()[0].strip()]

basePattern = [0,1,0,-1]

def p1(ints):
    for phase in range(100):
        newInts = []
        for indi,i in enumerate(ints):
            newInt = 0
            for indj, j in enumerate(ints):
                baseInd = basePattern[(((indj+1)//(indi+1)))%4]
                newInt += j*baseInd
            newInts.append(abs(newInt)%10)
        ints = newInts[:]

    return "".join(str(a) for a in ints[:8])



def p2(ints):
    offset = int(''.join(map(str, ints[:7])))
    ints = (ints[:]*10000)[offset:]+[0]
    for phase in range(100):
        for i in range(len(ints)-2, -1, -1):
            ints[i] = (ints[i+1]+ints[i])%10

    return "".join(map(str, ints[:8]))

print("Part 1: ", p1(ints[:]))
print("Part 2: ", p2(ints[:]))
