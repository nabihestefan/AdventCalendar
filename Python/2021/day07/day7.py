## Parsing
with open('day7.txt') as f:
    positions = [int(x) for x in f.readlines()[0].split(',')]

## Part 1
total = sum([abs(a-0) for a in positions])
new_t = 0

for i in range(1,len(positions)):
    new_t = sum([abs(a - i) for a in positions])
    if new_t < total:
        total = new_t
    else:
        print(total)
        break

## Part 2
total = sum([abs(int((abs(a-0)*(abs(a-0)+1))/2)) for a in positions])
new_t = 0

for i in range(1,len(positions)):
    new_t = sum([abs(int((abs(a-i)*(abs(a-i)+1))/2)) for a in positions])
    if new_t < total:
        total = new_t
    else:
        print(total)
        break
