files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().split("\n\n")

rules = dict()
for i,j in [map(int, c.split("|")) for c in data[0].split("\n")]:
    rules[i] = rules.get(i, []) + [j]
instructions = [map(int, x.strip().split(",")) for x in data[1].split("\n")]

def inOrder(inst, rules):
    for i, val in enumerate(inst):
        for r in rules.get(val, []):
            if r in inst[:i]: return False
    return True

def reOrder(inst, rules):
    newInst = []
    while len(inst) > len(newInst): # Once we're halfway through we have the value we need
        for val in inst:
            valid = True
            for k,r in rules.items():
                if (k not in inst) or (k in newInst): continue # Either it shouldnt be there or it already is
                if (val in r) and (k not in newInst): # The value will be added but not yet
                    valid = False
                    break
            if valid:
                newInst.append(val)
                inst.remove(val)
                break
    return newInst[-1]


def run(instructions, rules):
    p1 = p2 =0
    for inst in instructions:
        if inOrder(inst, rules): p1 += inst[(len(inst)-1)/2]
        else: p2 += reOrder(inst, rules)

    return p1, p2
    
print("Part 1&2: ", run(instructions, rules))