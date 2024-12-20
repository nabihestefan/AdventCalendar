files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

patterns = set(data[0].split(", "))
designs = [x.strip() for x in data[2:]]

KNOWN = {"": 1}

def designPossible(design, patterns):
    if design in KNOWN: return KNOWN[design]
    p = 0
    for patt in patterns:
        if design[:len(patt)] == patt:
            p += designPossible(design[len(patt):], patterns)
    KNOWN[design] = p
    return p

def run(designs, patterns):
    p1 = p2 = 0
    for d in designs:
        p = designPossible(d, patterns)
        p1 += (p > 0)
        p2 += p
    return p1, p2
    
print("Part 1&2: ", run(designs, patterns))