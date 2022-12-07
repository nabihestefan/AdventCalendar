files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split(" ") for x in f.readlines()]

class Node:
    def __init__(self, name, parent):
        self.nodes = set()
        self.name = name
        self.parent = parent
        self.size = None
    
def addSize(node):
    size = 0
    for i in node.nodes:
        if i.size == None: addSize(i)
        size += i.size
    node.size = size

def getTotal(node):
    if len(node.nodes) == 0:
        return 0
        
    size = node.size if node.size < 100000 else 0
    for i in node.nodes: size += getTotal(i)
    
    return size

def getMinDelete(node, currentMinDelete, spaceNeeded):
    if len(node.nodes) == 0: return currentMinDelete

    if node.size < currentMinDelete.size and node.size > spaceNeeded:
        currentMinDelete = node

    for i in node.nodes: 
        currentMinDelete = getMinDelete(i, currentMinDelete, spaceNeeded)

    return currentMinDelete  

def run(data):
    current = Node("/", None)
    for i in data[1:]:
        if i[0] == "$" and i[1] == "cd": 
            if i[2] == "..":
                current = current.parent
            else:
                for j in current.nodes:
                    if j.name == i[2]:
                        current = j
                        break
                node = Node(i[2], current)
                current.nodes.add(node)
                current = node
        
        elif i[0] != "$" and i[0] != "dir": 
            node = Node(i[1], current)
            node.size = int(i[0])
            current.nodes.add(node)
    
    while current.parent != None: current = current.parent
    addSize(current)

    print("Part 1: ", getTotal(current))
    
    spaceNeeded = 30000000 - (70000000 - current.size)

    smallest = getMinDelete(current, current, spaceNeeded)
    print("Part 2: ", smallest.size)

run(data)