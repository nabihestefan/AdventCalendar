files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    data =  [a.strip() for a in f.readlines()]

tree = dict()
weights = dict()
OGweights = dict()

for line in data:
    if "->" in line:
        line, right = line.split("->")
        children = [a.strip() for a in right.split(",")]
    else: children = []

    root, weight = line.split()[0].strip(), int(line.split()[1][1:-1])
    tree[root] = tuple(children)
    weights[root] = weight
    OGweights[root] = weight

def findWeight(root):
    for child in tree[root]: weights[root] += findWeight(child)
    return weights[root]

def part1():
    children = set([val for chil in tree.values() for val in chil])
    roots = set(tree.keys())
    return roots-children

def part2(root):
    weightsChildren = [weights[i] for i in tree[root]]
    if len(set(weightsChildren)) == 1: return True
    else:
        heavy, light = max(weightsChildren), min(weightsChildren)
        heavier = tree[root][weightsChildren.index(heavy)]
        if part2(heavier) == True: return OGweights[heavier] - (heavy-light)
        else: return part2(heavier)



root = part1().pop()
findWeight(root)

print("Part 1: ", root)
print("Part 2: ", part2(root))
