with open('input.txt', 'r') as f:
    data = [x for x in f.readlines()]


elves = []
val = 0
total = 0
for i in data:
    if i == "\n":
        elves.append(val)
        val = 0
    else:
        val += int(i)
print("Part 1: ", max(elves))
for i in range(3): total += elves.pop(elves.index(max(elves)))
print("Part 2: ", total)
    