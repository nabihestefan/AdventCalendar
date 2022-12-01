## Parsing
from itertools import *
from functools import *
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    weights = set([int(a.strip()) for a in f.readlines()])

parts = 4
sectionWeight = sum(weights) // parts
firsts = []
for n1 in range(1, len(weights)):
    for g1 in combinations(weights, n1):
        if sum(g1) != sectionWeight: continue
        qe = reduce(lambda a,b: a*b, g1, 1)
        weights2 = weights - set(g1)
        for n2 in range(1, len(weights2)):
            for g2 in combinations(weights2, n2):
                if sum(g2) != sectionWeight: continue
                weights3 = weights2 - set(g2)
                # Part 1
                # if sum(g3) != sectionWeight: continue
                # print(qe)
                # exit(0)
                for n3 in range(1, len(weights3)):
                    for g3 in combinations(weights3, n3):
                        if sum(g3) != sectionWeight: continue
                        g4 = weights3 - set(g3)
                        if sum(g4) != sectionWeight: continue
                        print(qe)
                        exit(0)
