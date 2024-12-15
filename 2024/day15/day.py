files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().split("\n\n")

moves = [i for i in data[1] if i !='\n']
rawMap = data[0].splitlines()
def parseMap(rawMap, partTwo):
    boxes = set()
    walls = set()
    robot = None
    if partTwo:
        newMap = []
        for i in range(len(rawMap)):
            rawMap[i] = rawMap[i].replace("#", "##")
            rawMap[i] = rawMap[i].replace("O", "[]")
            rawMap[i] = rawMap[i].replace(".", "..")
            rawMap[i] = rawMap[i].replace("@", "@.")
    for i in range(len(rawMap)):
        for j in range(len(rawMap[i])):
            if rawMap[i][j] == '@': robot = complex(i, j)
            if rawMap[i][j] in 'O[': boxes.add(complex(i, j))
            if rawMap[i][j] == '#': walls.add(complex(i, j))
    return robot, boxes, walls

def moveP1(robot, move, boxes, walls):
    newRobot = robot + move
    if newRobot in walls: return robot, boxes
    if newRobot in boxes:
        boxesMoved = []
        while newRobot in boxes:
            boxesMoved.append(newRobot)
            newRobot += move
        if newRobot in walls: return robot, boxes
        boxes.remove(robot + move)
        boxes.add(newRobot)
        return robot+move, boxes
    return newRobot, boxes

def moveP2(robot, move, boxes, walls):
    newRobot = robot+move
    fullBoxes = set([complex(box.real, box.imag+1) for box in boxes]).union(boxes)
    if newRobot in walls: return robot, None
    if newRobot in fullBoxes:
        if move.real != 0:
            nb, bm = moveP2(newRobot, move, boxes, walls)
            if nb == newRobot: return robot, None

            if newRobot in boxes: nextRobot = newRobot+1j
            else: nextRobot = newRobot-1j

            nb2, bm2 = moveP2(nextRobot, move, boxes, walls)
            if nb2 == nextRobot: return robot, None

            return robot+move, bm+bm2+[newRobot, nextRobot]
        else:
            boxesMoved = []
            while newRobot in fullBoxes:
                boxesMoved.append(newRobot)
                newRobot += move
            if newRobot in walls: return robot, None
            return robot+move, boxesMoved
    return newRobot, []

def prettyPrint(robot, boxes, walls, partTwo):
    for i in range(int(max(walls, key=lambda x: x.real).real+1)):
        row = ""
        j = 0
        while j < int(max(walls, key=lambda x: x.imag).imag+1):
            if complex(i, j) == robot: row += "@"
            elif complex(i, j) in boxes: 
                if partTwo:
                    row += "[]"
                    j += 1
                else: row += "O"
            elif complex(i, j) in walls: row += "#"
            else: row += "."
            j += 1
        print(row)

def run(rawMap, moves, partTwo=False):
    moveDir = {"<" : -1j, ">" : 1j, "^" : -1, "v" : 1}
    robot, boxes, walls = parseMap(rawMap, partTwo)
    # prettyPrint(robot, boxes, walls, partTwo)
    for m, i in enumerate(moves): 
        if partTwo:   
            newRobot, boxesMoved = moveP2(robot, moveDir[i], boxes, walls)
            if newRobot == robot: continue
            newBoxes = set()
            for box in boxes:
                if box in boxesMoved:
                    newBoxes.add(box+moveDir[i])
                else: newBoxes.add(box)
            robot, boxes = newRobot, newBoxes
        else: robot, boxes = moveP1(robot, moveDir[i], boxes, walls)
    # prettyPrint(robot, boxes, walls, partTwo)
    return int(sum(box.real*100+box.imag for box in boxes))
    
print("Part 1: ", run(rawMap, moves))
print("Part 2: ", run(rawMap, moves, True))