with open('input.txt', 'r') as f:
    data = [x.split("\n") for x in f.read().split("\n\n")]

elves = []
for elf in data: elves.append(sum(map(int, elf)))
print("Part 1: ", max(elves))

total = 0
for i in range(3): total += elves.pop(elves.index(max(elves)))
print("Part 2: ", total)
    