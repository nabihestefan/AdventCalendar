#for speed purposes
import heapq
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

class Nanobot:
    def __init__(self,x,y,z,r):
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.reachable = 0

    def inRangeBot(self, otherBot):
        if d3((self.x,self.y,self.z), (otherBot.x, otherBot.y, otherBot.z)) <= self.radius:
            self.reachable += 1
    def inRange(self, pos):
        return d3((self.x, self.y, self.z),pos) <= self.radius

def d3(a,b=(0,0,0)): return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

bots = []
for i in lines:
    x,y,z = map(int, i[i.index("<")+1:i.index(">")].split(","))
    r = int(i[i.index("r=")+2:])
    bots.append(Nanobot(x,y,z,r))

Rbot = max(bots, key=lambda x: x.radius)
for bot in bots: Rbot.inRangeBot(bot)

print("Part 1: ", Rbot.reachable)


maxX, maxY, maxZ = 0,0,0
for bot in bots:
    maxX = max(maxX, abs(bot.x)+bot.radius)
    maxY = max(maxY, abs(bot.y)+bot.radius)
    maxZ = max(maxZ, abs(bot.z)+bot.radius)
maxSqrSide = max(maxX, maxY, maxZ)

boxsize = 1
while boxsize < maxSqrSide: boxsize*=2

initial = ((-boxsize,-boxsize,-boxsize), (boxsize,boxsize,boxsize))

def intersect(box,bot):
    d = 0
    for i,b in ((0,bot.x),(1,bot.y),(2,bot.z)):
        boxL, boxH = box[0][i], box[1][i]-1
        d += abs(b-boxL) + abs(b-boxH)
        d -= boxH-boxL
    d //= 2
    return d <= bot.radius

def countIntersects(box): return sum(1 for b in bots if intersect(box,b))

workHeap = [(-len(bots), -2*boxsize, 3*boxsize, initial)]
while workHeap:
    negReach, negSz, distToOG, box = heapq.heappop(workHeap)
    if negSz == -1:
        print("Part 2: ", distToOG)
        break
    newSz = negSz // -2
    for octant in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
                   (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        newBox0 = tuple(box[0][i] + newSz * octant[i] for i in (0, 1, 2))
        newBox1 = tuple(newBox0[i] + newSz for i in (0, 1, 2))
        newBox = (newBox0, newBox1)
        newReach = countIntersects(newBox)
        heapq.heappush(workHeap,
                       (-newReach, -newSz, d3(newBox0, (0, 0, 0)), newBox))
