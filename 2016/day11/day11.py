from copy import deepcopy
## DEFINITELY needed online help ngl
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def getHash(pos, floors):
	return str(pos) + str([(len(floors[i]), sum(x < 0 for x in floors[i])) for i in range(4)])

start = [[], [], [], []]
items = {"nothing":0}
for i,line in enumerate(lines):
    if 'nothing relevant' in line: pass
    words = line.split()
    for ind,w in enumerate(words):
        if "." in w: w = w[:-1]
        if "microchip" in w:
            material = words[ind-1].split("-")[0]
            if material not in items.keys():
                items[material] = max(items.values())+1
            start[i].append(items[material])

        if "generator" in w:
            material = words[ind-1]
            if material not in items.keys():
                items[material] = max(items.values())+1
            start[i].append(-1*items[material])

def run(start):
    def move(pos, floors, dir, fromI, toI):
    	if fromI != None and toI != None:
    		floors[pos + dir].insert(toI, floors[pos].pop(fromI))

    def exploreState(req, pos, floors, dir, moves, i, j = None):
    	if dir * pos < req:
    		move(pos, floors, dir, j, 0)
    		move(pos, floors, dir, i, 0)

    		nextHash = getHash(pos + dir, floors)

    		if nextHash not in states and floors[pos + dir] and isValidState(floors[pos + dir]) and isValidState(floors[pos]):
    			queue.append([pos + dir, deepcopy(floors), moves + 1, nextHash])

    		move(pos + dir, floors, -dir, 0, i)
    		move(pos + dir, floors, -dir, 0, j)

    def isValidState(floor):
    	hasGen   = sum(x < 0 for x in floor)
    	unpaired = sum(x > 0 and -x not in floor for x in floor)
    	return not (hasGen and unpaired)

    endHash = getHash(3,[[],[],[],sum(start,[])])
    states = set()
    queue = []

    queue.append([0,start,0,getHash(0,start)])

    while True:
        pos,floors,moves,curHash = queue.pop(0)

        if curHash not in states:
            states.add(curHash)

            if curHash == endHash: return moves

            for i in range(len(floors[pos])):
                for j in range(i+1, len(floors[pos])):
                    exploreState(3,pos,floors,1,moves,i,j)
                    exploreState(0,pos,floors,-1,moves,i,j)

                exploreState(3,pos,floors,1,moves,i)
                exploreState(0,pos,floors,-1,moves,i)

print("Part 1: ", run(start))
m = max(items.values())+1
start[0] += [-m,m,-(m+1),(m+1)]
print("Part 2: ", run(start))
