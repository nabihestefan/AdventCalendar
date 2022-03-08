with open('input.txt', 'r') as f: map =  [a for a in f.readlines()]

def move(x,y,prevMove):
    moves = {"N": lambda x,y: (x, y-1), "E": lambda x,y: (x+1, y),
             "S": lambda x,y: (x, y+1), "W": lambda x,y: (x-1, y)}

    moveDict = {(0,-1): "N", (1,0): "E", (0,1): "S", (-1,0):"W"}

    if map[y][x] == "+":
        if prevMove in ["N", "S"]:
            next = [(1,0), (-1,0)]
        else:
            next = [(0,1), (0,-1)]

        for dx,dy in next:
            if map[y+dy][x+dx] != " ":
                prevMove = moveDict[(dx,dy)]

    nx, ny = moves[prevMove](x,y)

    return nx, ny, prevMove

def run():
    y,x = 0, map[0].index("|")
    prevMove = "S"
    letters = ""
    steps = 0
    while True:
        if map[y][x] == " ":
            return letters[:-1], steps
        x,y, prevMove = move(x,y,prevMove)
        if map[y][x] not in ["-", "|", "+"]:
            letters += map[y][x]
        steps += 1

print("Part 1&2: ", run())
