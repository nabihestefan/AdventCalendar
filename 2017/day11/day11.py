with open('input.txt', 'r') as f: lines = f.readlines()[0].strip().split(",")

def run():
    maxDist = x = y = 0
    dirs = {"n":(0,-1), "ne":( 0.5,-0.5), "nw":(-0.5,-0.5),
            "s":(0, 1), "sw":(-0.5, 0.5), "se":( 0.5, 0.5)}
    for i in lines:
        x,y = x + dirs[i][0], y + dirs[i][1]
        maxDist = max(maxDist , abs(x) + abs(y))
    return int(abs(x)+abs(y)), int(maxDist)

print("Part 1 & 2: ", run())
