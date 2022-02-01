with open('day2.txt') as f:
    lines = f.readlines()

instructions = []
for i in lines:
    amount = int(i[-2])
    dir = i[:-2]
    instructions.append((dir, amount))

horizontal = 0
depth = 0
aim = 0
for i in instructions:
    if i[0] == "forward ":
        horizontal += i[1]
        depth += i[1]*aim
    if i[0] == "down ":
        aim += i[1]
    if i[0] == "up ":
        aim -= i[1]

print(horizontal)
print(depth)
print(depth*horizontal)
