files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

robots = []
for i in data:
    pos, vel = i.split(" ")
    robots.append([list(map(int, pos.split("=")[1].split(","))), list(map(int, vel.split("=")[1].split(",")))])

def moveRobot(pos, vel, amount=1):
    np = pos[0] + vel[0]*amount, pos[1] + vel[1]*amount
    return (np[0]%101, np[1]%103), vel

def prettyPrint(robots, minx=0, maxx=101, miny=0, maxy=103):
    grid = [[" " for _ in range(101)] for _ in range(103)]
    for x,y in robots:
        grid[y][x] = "#"
    for row in grid[miny:maxy]:
        print("".join(row[minx:maxx]))

def run(robots):
    newRobots = [moveRobot(pos,vel,100)[0] for pos,vel in robots]
    X_LINE = 50
    Y_LINE = 51
    q1 = q2 = q3 = q4 = 0
    for x,y in newRobots:
        if x < X_LINE and y < Y_LINE: q1 += 1
        elif x < X_LINE and y > Y_LINE: q2 += 1
        elif x > X_LINE and y < Y_LINE: q3 += 1
        elif x > X_LINE and y > Y_LINE: q4 += 1

    i = 100
    while True:
        robots = [moveRobot(pos,vel) for pos,vel in robots]
        r = [x[0] for x in robots]
        i += 1
        if len(r) == len(set(r)): break
    
    prettyPrint(r, 38, 69, 17, 50)
    return q1*q2*q3*q4, i
    

print("Part 1: ", run(robots))
# print("Part 2: ", p2(robots))