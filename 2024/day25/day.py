with open('input.txt', 'r') as f:
    data = [x.splitlines() for x in f.read().split('\n\n')]

locks, keys = [], []
for line in data:
    d = [0 for _ in range(len(line[0]))]
    key = False
    if "." in line[0]:
        line = line[::-1]
        key = True
    for i in line[1:]:
        for index, j in enumerate(i):
            if j == "#": d[index] += 1
    if key: keys.append(d)
    else: locks.append(d)

def run(locks, keys):
    total = 0
    for l in locks:
        for k in keys:
            t = [x+y>5 for x,y in zip(l,k)]
            if True in t: continue
            total += 1
    return total
    
print("Part 1: ", run(locks,keys))
print("Part 2: Click the button!")