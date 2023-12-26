files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x for x in f.read().split('\n\n')]

inst = data[0]

paths = {}
for i in data[1].split('\n'):
    node, lr = i.split(' = ')
    paths[node] = lr.strip()[1:-1].split(', ')

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def run(inst, paths, partTwo):
    curs = [x for x in paths.keys() if x[-1] == "A"] if partTwo else ["AAA"]
    starts = {i:-1 for i in range(len(curs))}
    steps = 0
    while -1 in starts.values():
        for i, cur in enumerate(curs):
            if starts[i] != -1: continue
            if starts[i] == -1 and cur[-1] == "Z": starts[i] = steps
            if inst[steps%len(inst)] == 'L': curs[i] = paths[cur][0]
            elif inst[steps%len(inst)] == 'R': curs[i] = paths[cur][1]
        steps += 1
    lcm = 1
    for i in starts.values(): lcm = lcm * i // gcd(lcm, i)
    return lcm
            
print("Part 1: ", run(inst, paths, False))
print("Part 2: ", run(inst, paths, True))