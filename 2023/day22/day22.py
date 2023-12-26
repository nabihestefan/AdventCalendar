files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    bricks = []
    for line in f.readlines():
        st, en = line.split('~')
        st = tuple(map(int, st.split(",")))
        en = tuple(map(int, en.split(",")))
        brick = []
        for x in range(st[0], en[0]+1):
            for y in range(st[1], en[1]+1):
                for z in range(st[2], en[2]+1):
                    brick.append((x,y,z))
        bricks.append(brick)

def drop(bricks, test):
    moved = set()
    newBricks = []
    while True:
        flat = set([coord for b in bricks for coord in b])
        for i, brick in enumerate(bricks):
            canMove = True
            for x,y,z in brick:
                if z == 1: 
                    canMove = False
                    break
                if (x,y,z-1) in flat and (x,y,z-1) not in brick: 
                    canMove = False
                    break
            if canMove:
                if test: return False
                moved.add(i)
                newBricks.append([(x,y,z-1) for x,y,z in brick])
            else: newBricks.append(brick) 
        if bricks == newBricks:
            if test: return True
            return newBricks, moved
        bricks, newBricks = newBricks, []

def run(bricks):
    newBricks = []
    while True:
        newBricks, _ = drop(bricks, False)
        if newBricks == bricks: break
        bricks = newBricks

    p1 = p2 = 0
    for brick in bricks:
        newBricks = [b for b in bricks if b!=brick]
        if drop(newBricks, True): p1 += 1
        p2 += len(drop(newBricks, False)[1])
    
    return p1, p2
            
print("Part 1 & 2: ", run(bricks))