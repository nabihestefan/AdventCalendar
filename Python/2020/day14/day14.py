from itertools import product
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]


instructions = []
for inst in lines:
    if inst[:4] == "mask":
        instructions.append(("mask", inst[inst.index("=")+2:]))
    else:
        instructions.append((inst[inst.index("[")+1:inst.index("]")], bin(int(inst[inst.index("=")+2:]))))

mem = {}
mask = ""
for spot, line in instructions:
    if spot == "mask":
        mask = line
    else:
        line = line[2:]
        new = list(mask)
        i = 1
        for c in line[::-1]:
            if i >= len(new):
                new = [c] + new
            elif new[-1*i] == "X": new[-1*i] = c
            i+=1
        new = "".join(new).replace("X", "0")
        if len(line) > len(new):
            print(line, new)
        mem[spot] = int(new, 2)

print("Part 1: ", sum(mem[key] for key in mem.keys()))

def permutations(line):
    possible = []
    bits = [i for i,v in enumerate(line) if v == "X"]
    perms = [''.join(seq) for seq in product('01', repeat=len(bits))]
    for perm in perms:
        bitV = dict(zip(bits, perm))
        for i in bitV:
            line = line[:i] + [bitV[i]] + line[i+1:]
        possible.append("".join(line))
    return possible

mem = {}
mask = ""
for spot, fill in instructions:
    if spot == "mask":
        mask = fill
    else:
        line = bin(int(spot))[2:]
        new_spot = list(mask)
        i = 1
        for c in line[::-1]:
            if i >= len(new_spot):
                new_spot = [c] + new_spot
            elif new_spot[-1*i] == "0": new_spot[-1*i] = c
            i+=1

        for i in permutations(new_spot):
            mem[i] = int(fill,2)


print("Part 2: ", sum(mem[key] for key in mem.keys()))
