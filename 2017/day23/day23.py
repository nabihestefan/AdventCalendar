with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]


def part1():
    regs = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0}
    mults = 0
    i = 0
    while i < len(lines):
        inst,x,y = lines[i].split(" ")
        if inst.strip() == "set":
            if y in regs.keys():
                regs[x] = regs[y]
            else:
                regs[x] = int(y)
        elif inst.strip() == "sub":
            if y in regs.keys():
                regs[x] -= regs[y]
            else:
                regs[x] -= int(y)
        elif inst.strip() == "mul":
            mults += 1
            if y in regs.keys():
                regs[x] *= regs[y]
            else:
                regs[x] *= int(y)
        elif inst.strip() == "jnz":
            if x in regs.keys():
                if regs[x] != 0: i += int(y) - 1
            else:
                if int(x) != 0: i += int(y) - 1

        i += 1
    return mults

def part2():
    h = 0
    for num in range(105700, 122700+1, 17):
        for i in range(2, num):
                if num % i == 0:
                    h += 1
                    break
    return h

print("Part 1: ", part1())
print("Part 2: ", part2())
