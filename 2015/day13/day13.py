## Parsing
from itertools import permutations

files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

people = []
positions = []
for i in lines:
    space = i.index(" ")
    would = i.index("would")
    happiness = i.index("happiness")
    to = i.index("to")
    person1 = i[0:space]
    person2 = i[to+3:-1]
    num = i[would+11:happiness-1]
    if i[would+6:would+10] == "lose":
        positions.append((person1, int(num)*-1, person2))
    else:
        positions.append((person1, int(num), person2))
## Part 1

def arrangement_weight(perm):
    happiness = 0
    i = 0
    while i < len(perm):
        person1 = perm[i-1]
        person2 = perm[i]
        for j in positions:
            if j[0] == person1 and j[2] == person2:
                happiness += j[1]

            if j[0] == person2 and j[2] == person1:
                happiness += j[1]
        i += 1
    return happiness

for i in positions:
    if not(i[0] in people):
        people.append(i[0])

perms = permutations(people)

maxim = 0
arrangement = people
for i in perms:
    new = arrangement_weight(i)
    if new > maxim:
        maxim = new
        arrangement = i

print(maxim)
print(arrangement)

##Part 2
for i in people:
    positions.append(("Me", 0, i))
    positions.append((i, 0, "Me"))

people.append("Me")

perms = permutations(people)

maxim = 0
for i in perms:
    new = arrangement_weight(i)
    if new > maxim:
        maxim = new
        arrangement = i

print(maxim)
print(arrangement)
