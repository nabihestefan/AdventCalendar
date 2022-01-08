files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(" ")]

class Tree:
    def __init__(self):
        self.nodes = []
        self.meta = []

    def addNode(self,node):
        self.nodes.append(node)

    def addData(self,data):
        self.meta.append(data)

    def sumDataP1(self):
        return sum(self.meta) + sum(node.sumDataP1() for node in self.nodes)

    def sumDataP2(self):
        if len(self.nodes) == 0: return sum(self.meta)
        else:
            return sum(self.nodes[i-1].sumDataP2() if i <= len(self.nodes) else 0 for i in self.meta)

def createTree(ints, i):
    nodes = ints[i]
    meta = ints[i+1]
    root = Tree()
    ind = i+2
    for j in range(nodes):
        node, ind = createTree(ints, ind)
        root.addNode(node)
    for j in range(meta):
        root.addData(ints[ind])
        ind += 1
    return root, ind

root, ind = createTree(ints[:], 0)
print("Part 1: ", root.sumDataP1())
print("Part 2: ", root.sumDataP2())
