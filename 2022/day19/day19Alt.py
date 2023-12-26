from collections import deque
files = ['input.txt', 'inputTest.txt']
robots = []
with open(files[1], 'r') as f:
    for i in f.readlines():
        words = i.split()
        oreCore = int(words[6])
        clayCore = int(words[12])
        obsCore = int(words[18])
        obsCclay = int(words[21])
        geoCore = int(words[27])
        geoCobs = int(words[30])
        robots.append([(oreCore,0,0,0),(clayCore,0,0,0), (obsCore,obsCclay,0,0),(geoCore,0,geoCobs,0)])


def blueprintSimulation(blueprint,time):
    queue = deque([((1,0,0,0),(0,0,0,0),time)])
    maxGeode = 0
    seen = set()
    while queue:
        state = queue.popleft()
        robs, mats, mins = state
        maxGeode = max(maxGeode, mats[3])
        if mins == 0: continue

        # I never need to go above the max I might need for an element. Eliminate those possibilities
        # If I have enough of a material that I cant use all of it, just cap it at max use to eliminate possibilities
        robs = list(robs)
        mats = list(mats)
        for ind in range(3):
            maxMat = max([x[ind] for x in blueprint])
            if robs[ind] >= maxMat: robs[ind] = maxMat
            if mats[ind] >= mins*maxMat-robs[ind]*(mins-1): mats[ind] = mins*maxMat-robs[ind]*(mins-1)
        robs = tuple(robs)
        mats = tuple(mats)

        if (robs, mats, mins) in seen: continue
        seen.add((robs, mats, mins))

        # Add step with no new robots

        queue.append((robs, tuple(x+y for x,y in zip(mats, robs)), mins-1))
        # go through every robot in blueprint
        for iR, robCost in enumerate(blueprint):
            if False in [x>=y  for x,y in zip(mats, robCost)]: continue
            newRobots = list(robs)
            newRobots[iR] += 1
            queue.append((tuple(newRobots), tuple(x+y-z for x,y,z in zip(mats,robs,robCost)), mins-1))


    return maxGeode

def part1(robots):
    quality = 0
    for ind, i in enumerate(robots):
        quality += (ind+1)*blueprintSimulation(i, 24)
    return quality

def part2(robots):
    quality = 1
    for i in robots[0:3]:
        print(i)
        quality *= blueprintSimulation(i, 32)
    return quality


print("Part 1: ", part1(robots))
print("Part 2: ", part2(robots))
