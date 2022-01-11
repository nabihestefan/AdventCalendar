## Parsing
def getMinDrop(disc, i):
    posNum, curPos = disc
    posI = ((posNum-curPos)-i)%posNum
    return posI

files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    discs = []
    for ind,i in enumerate(f.readlines()):
        words = i.strip().split()
        posNum = int(words[3])
        curPos = int(words[-1][:-1])
        discs.append((posNum, curPos, getMinDrop((posNum, curPos), ind+1)))

def testDrop(drop, disc):
    return drop > disc[2] and (drop-disc[2])%disc[0] == 0


def run(discs):
    drop = discs[0][2]
    incRate = discs[0][0]
    for ind, disc in enumerate(discs[1:]):
        while not testDrop(drop,disc): drop += incRate
        incRate *= disc[0]
    return drop

print("Part 1: ", run(discs))
discs.append((11,0,getMinDrop((11,0), ind+2)))
print("Part 2: ", run(discs))
