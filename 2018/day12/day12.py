files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]


    pots = set(i for i,c in enumerate(lines[0][len("initial state: "):]) if c == "#")
rules = set()
for line in lines[2:]:
    if line[-1] == "#": rules.add(line[:5])

def next(pots, rules):
    start = min(pots)
    end = max(pots)
    new = set()
    for i in range(start-3, end+4):
        sect = "".join("#" if i + k in pots else "." for k in [-2, -1, 0, 1, 2])
        if sect in rules: new.add(i)
    return new



prev = 0
prevD = 0

for i in range(2000):
    if i == 20:
        print("Part 1: ", sum(pots))
    pots = next(pots, rules)
    s = sum(pots)
    d = s - prev
    prev = s
# from i-1 (prev) it increases by d constantly
print("Part 2: ", s + d*(50000000000-i-1))
