import networkx as nx
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(a.strip()) for a in f.readlines()]

class Unit:
    def __init__(self, type, x,y, dmg):
        self.type = type
        self.x = x
        self.y = y
        self.hp = 200
        self.alive = True
        self.pow = dmg

    def pos(self): return self.x, self.y

    def attack(self, dmg):
        if self.alive:
            self.hp -= dmg
            if self.hp <= 0: self.alive = False

def findClosest(g, excluded, start, targets):
    if start not in g: return [], None

    seen = set()
    q = [(start,0)]
    foundDist = None
    closest = []
    while q:
        point, dist = q.pop(0)
        if foundDist is not None and dist > foundDist:
            return closest, foundDist
        if point in seen or point in excluded:
            continue
        seen.add(point)
        if point in targets:
            foundDist = dist
            closest.append(point)
        for n in g.neighbors(point):
            if n not in seen:
                q.append((n, dist+1))
    return closest, foundDist

def readingOrder(pos): return pos[1], pos[0]

def nbs(x, y): return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def run(data, dmg, partTwo):
    units = []
    g = nx.Graph()
    for y in range(len(data)):
        for x in range(len(data[0])):
            p = data[y][x]
            if p in "GE":
                units.append(Unit(p, x, y, 3 if p=="G" else dmg))
            if p in "GE.":
                for x2,y2 in nbs(x,y):
                    if 0 <= x2 <= len(data[0]) and 0 <= y2 <= len(data[0]) and data[y2][x2] in "GE.":
                        g.add_edge((x,y),(x2,y2))
    r = 0
    while True:
        order = sorted(units, key=lambda x: readingOrder(x.pos()))

        for i,c in enumerate(order):
            if not c.alive: continue

            enemies = [e for e in units if e.type!=c.type and e.alive]
            enemyPos = [e.pos() for e in enemies]

            nearby = nbs(*c.pos())

            enemiesInRange = [p for p in nearby if p in enemyPos]

            if not enemiesInRange:
                surr = []
                for e in enemies: surr.extend(nbs(*e.pos()))
                surr = [s for s in surr if s in g]

                excluded = [e.pos() for e in units if e.alive and e != c]
                closest, dist = findClosest(g, excluded, c.pos(), surr)

                if closest:
                    choice = min(closest, key=readingOrder)
                    for s in sorted(nearby, key=readingOrder):
                        _,d = findClosest(g, excluded, s, [choice])
                        if d == dist-1:
                            c.x, c.y = s
                            break
                enemiesInRange = [p for p in nbs(*c.pos()) if p in enemyPos]

            if enemiesInRange:
                enemies = [e for e in enemies if e.pos() in enemiesInRange]

                lowestHP = min(enemies, key=lambda e: (e.hp, readingOrder(e.pos())))
                lowestHP.attack(c.pow)

                if partTwo and lowestHP.type == "E" and not lowestHP.alive:
                    return False, 0

                alive = set(e.type for e in units if e.alive)
                if len(alive)==1:
                    if i == len(order)-1: r +=1
                    return True, r*sum(e.hp for e in units if e.alive)
        r += 1





_, score = run(data[:], 3, False)
print("Part 1: ", score)

dmg = 3
while True:
    works, score = run(data[:], dmg, True)
    if works:
        print("Part 2: ", score)
        break
    dmg += 1
