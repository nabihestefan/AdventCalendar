files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

gsPt1 = []
gsPt2 = []
g = []
for i in lines:
    if i == "":
        gsPt1.append(g)
        g = []
    else:
        for c in i:
            if not c in g:
                g.append(c)
gsPt1.append(g)

g = {}
l = 0
for i in lines:
    if i == "":
        gsPt2.append((g, l))
        g = {}
        l = 0
    else:
        for c in i:
            if c not in g.keys(): g[c] = 1
            else: g[c] += 1
        l += 1
gsPt2.append((g, l))

total = 0
for g in gsPt1:
    total += len(g)
print("Part 1: ", total)

total = 0
for g in gsPt2:
    for i in g[0].keys():
        if g[0][i] == g[1]:
            total += 1
print("Part 2: ", total)
