files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip().split() for a in f.readlines()]

regDict = {"a":0, "b":1, "c":2, "d":3}

def run(regs):
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[0] == "cpy":
            regs[regDict[line[2]]] = int(line[1]) if line[1].isdigit() else regs[regDict[line[1]]]

        if line[0] == "inc":
            regs[regDict[line[1]]] += 1

        if line[0] == "dec":
            regs[regDict[line[1]]] -= 1

        if line[0] == "jnz":
            if int(line[1]) if line[1].isdigit() else regs[regDict[line[1]]] != 0:
                i += int(line[2]) - 1
        i += 1
    return regs[0]

print("Part 1: ", run([0,0,0,0]))
print("Part 2: ", run([0,0,1,0]))
