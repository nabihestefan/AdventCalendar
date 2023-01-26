from copy import deepcopy
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip().split() for a in f.readlines()]

regDict = {"a":0, "b":1, "c":2, "d":3}

def run(regs, lines):
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[0] == "cpy":
            if line[2].isdigit(): pass
            regs[regDict[line[2]]] = int(line[1]) if line[1].isdigit() or line[1][1:].isdigit() else regs[regDict[line[1]]]

        if line[0] == "inc":
            regs[regDict[line[1]]] += 1

        if line[0] == "dec":
            regs[regDict[line[1]]] -= 1

        if line[0] == "jnz":
            if int(line[1]) if line[1].isdigit() else regs[regDict[line[1]]] != 0:
                i += int(line[2])-1 if line[2].isdigit() or line[2][1:].isdigit() else regs[regDict[line[2]]]-1

        if line[0] == "tgl":
            x = regs[regDict[line[1]]]
            if i+x >= len(lines):
                i+=1
                continue
            inst = lines[i+x]
            if inst[0] == "inc": lines[i+x][0] = "dec"
            elif inst[0] in ["dec", "tgl"]: lines[i+x][0] = "inc"
            elif inst[0] == "jnz": lines[i+x][0] = "cpy"
            elif inst[0] == "cpy": lines[i+x][0] = "jnz"
        i += 1
    return regs[0]

print("Part 1: ", run([7,0,0,0], deepcopy(lines)))
print("Part 2: ", run([12,0,0,0], deepcopy(lines)))
