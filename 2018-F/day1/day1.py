from collections import defaultdict
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a.strip()) for a in f.readlines()]

print("Part 1: ", sum(ints))

f = 0
seen = [f]
for i in ints:
    f += i
    seen.append(f)

seen = seen[:-1]

mods = {}
for i,v in enumerate(seen):
    l = mods.get(v%f,[])
    l.append((i,v))
    mods[v%f] = l

minInd, minDiff, minFreq = None, None, None
for group in mods.values():
    sortedVals = sorted(group, key=lambda t: t[1])
    for i in range(1,len(sortedVals)):
        diff = sortedVals[i][1] -sortedVals[i-1][1]
        ind = sortedVals[i-1][0] if f > 0 else sortedVals[i][0]
        freq = sortedVals[i][1] if f > 0 else sortedVals[i-1][1]
        if minDiff is None or diff < minDiff or (diff == minDiff and ind < minInd):
            minInd, minDiff, minFreq = ind, diff, freq

print("Part 2: ", minFreq)
