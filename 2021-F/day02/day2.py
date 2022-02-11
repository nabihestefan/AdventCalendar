with open('day2.txt') as f:
    instructions = [(i[:-2].strip(), int(i[-2:].strip())) for i in f.readlines()]

def part1():
    horizontal = 0
    depth = 0
    for i in instructions:
        if i[0] == "forward":
            horizontal += i[1]
        if i[0] == "down":
            depth += i[1]
        if i[0] == "up":
            depth -= i[1]
    return depth*horizontal

def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for i in instructions:
        if i[0] == "forward":
            horizontal += i[1]
            depth += i[1]*aim
        if i[0] == "down":
            aim += i[1]
        if i[0] == "up":
            aim -= i[1]
    return depth*horizontal

print("Part 1: ", part1())
print("Part 2: ", part2())
