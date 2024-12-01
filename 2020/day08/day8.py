from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]


def run(lines):
    acc = 0
    visited = []
    i = 0
    while i < len(lines):
        if i in visited: return (False, acc)
        visited.append(i)
        if lines[i][:3] == "nop":
            i += 1
        elif lines[i][:3] == "acc":
            acc += int(lines[i][4:])
            i += 1
        elif lines[i][:3] == "jmp":
            i += int(lines[i][4:])
    return True, acc

def replacing(lines):
    change = 0
    newCop = deepcopy(lines)
    while not run(newCop)[0]:
        newCop = deepcopy(lines)
        i = -1
        ind = 0
        while i < change:
            if newCop[ind][:3] == "nop":
                i += 1
            if newCop[ind][:3] == "jmp":
                i += 1
            ind += 1
        if newCop[ind-1][:3] == "nop": newCop[ind-1] = newCop[ind-1].replace("nop", "jmp")
        else: newCop[ind-1] = newCop[ind-1].replace("jmp", "nop")
        change += 1

    return run(newCop)[1]


print("Part 1: ", run(lines)[1])
print("Part 2: ", replacing(lines))
