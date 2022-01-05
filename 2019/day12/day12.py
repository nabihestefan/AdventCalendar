files = ['input.txt', 'inputTest.txt']
## Parsing
def getxyz(line):
    x = int(line[line.index("x=")+2: line.index(", y")])
    y = int(line[line.index("y=")+2: line.index(", z")])
    z = int(line[line.index("z=")+2: line.index(">\n")])
    return x,y,z

def gcd(a,b):
    if b==0: return a
    else: return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

with open(files[0], 'r') as f:
    moonPos = [getxyz(a) for a in f.readlines()]

def run(pos,vel,steps = float('inf')):
    ogPos, ogVel = pos[:], vel[:]
    step = 0
    while step < steps and (not step or pos != ogPos or vel != ogVel):
        for i in range(len(pos)):
            vel[i] += sum(1 if pos[i] < curPos else -1 for curPos in pos if curPos != pos[i])
        for i in range(len(pos)):
            pos[i] += vel[i]
        step += 1
    return step

def part1(moonPos):
    px, vx = [x for x, _, _ in moonPos], [0] * len(moonPos)
    py, vy = [y for _, y, _ in moonPos], [0] * len(moonPos)
    pz, vz = [z for _, _, z in moonPos], [0] * len(moonPos)

    for p,v in zip((px,py,pz),(vx,vy,vz)):
        run(p,v,1000)

    return sum((abs(px[i])+abs(py[i])+abs(pz[i]))*(abs(vx[i])+abs(vy[i])+abs(vz[i])) for i in range(len(moonPos)))


def part2(moonPos):
    px, vx = [x for x, _, _ in moonPos], [0] * len(moonPos)
    py, vy = [y for _, y, _ in moonPos], [0] * len(moonPos)
    pz, vz = [z for _, _, z in moonPos], [0] * len(moonPos)
    stepsX = run(px,vx)
    stepsY = run(py,vy)
    stepsZ = run(pz,vz)

    return lcm(lcm(stepsX, stepsY),stepsZ)

print("Part 1: ", part1(moonPos[:]))
print("Part 2: ", part2(moonPos[:]))
