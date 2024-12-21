files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    codes = [x.strip() for x in f.readlines()]
NUM_KEY = {"7": (3,0), "8": (3,1), "9": (3,2),
           "4": (2,0), "5": (2,1), "6": (2,2),
           "1": (1,0), "2": (1,1), "3": (1,2),
                       "0": (0,1), "A": (0,2)}

MOVE_KEY = {            "^": (0,1), "A": (0,2),
            "<": (1,0), "v": (1,1), ">": (1,2)}

MOVES = dict()

def cheapestMove(start, end, robot, partTwo):
    if (start, end, robot) in MOVES:
        return MOVES[(start, end, robot)]
    queue = [(start, "")]
    moves = 1e25
    while queue:
        pos, path = queue.pop(0)
        if pos == (0,0): continue
        if pos == end:
            moves = min(moves, getPath(path+"A", partTwo, robot+1))
            continue
        
        if robot != 0:
            if pos[0] < end[0]: queue.append(((pos[0]+1, pos[1]), path+"v"))
            elif pos[0] > end[0]: queue.append(((pos[0]-1, pos[1]), path+"^"))
        else:
            if pos[0] < end[0]: queue.append(((pos[0]+1, pos[1]), path+"^"))
            elif pos[0] > end[0]: queue.append(((pos[0]-1, pos[1]), path+"v"))

        if pos[1] < end[1]: queue.append(((pos[0], pos[1]+1), path+">"))
        elif pos[1] > end[1]: queue.append(((pos[0], pos[1]-1), path+"<"))

    MOVES[(start, end, robot)] = moves
    return moves

def getPath(code, partTwo, robot, move=True):
    if (robot == 3 and not partTwo) or robot == 26: return len(code)
    moves = 0
    pos = (0,2)
    for c in code:
        newPos = MOVE_KEY[c] if move else NUM_KEY[c]
        moves += cheapestMove(pos, newPos, robot, partTwo)
        pos = newPos
    return moves

def run(codes, partTwo=False):
    total = 0
    for code in codes:
        moves = getPath(code, partTwo, 0, False)
        total += moves * int(code[:-1])
    return total
    
print("Part 1: ", run(codes))
MOVES = dict()
print("Part 2: ", run(codes, True))