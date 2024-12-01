from collections import deque
files = ['input.txt', 'inputTest.txt']
robots = []
with open(files[0], 'r') as f:
    for i in f.readlines():
        words = i.split()
        oreCore = int(words[6])
        clayCore = int(words[12])
        obsCore = int(words[18])
        obsCclay = int(words[21])
        geoCore = int(words[27])
        geoCobs = int(words[30])
        robots.append((oreCore,clayCore,obsCore,obsCclay, geoCore, geoCobs))


def blueprintSimulation(blueprint,time):
    oreCore, clayCore, obsCore, obsCclay, geoCore, geoCobs = blueprint
    queue = deque([(1,0,0,0, 0,0,0,0, time)])
    maxGeode = 0
    seen = set()
    while queue:
        state = queue.popleft()
        Rore, Rclay, Robs, Rgeo, ore, clay, obs, geo, mins = state
        maxGeode = max(maxGeode, geo)
        if mins == 0: continue

        # I never need to go above the max I might need for an element. Eliminate those possibilities
        maxOre = max(oreCore, clayCore, obsCore, geoCore)
        if Rore >= maxOre: Rore = maxOre
        if Rclay >= obsCclay: Rclay = obsCclay
        if Robs >= geoCobs: Robs = geoCobs

        # # If I have enough of a material that I cant use all of it, just cap it at max use to eliminate possibilities
        if ore >= mins*maxOre-Rore*(mins-1): ore = mins*maxOre-Rore*(mins-1)
        if clay >= mins*obsCclay-Rclay*(mins-1): clay = mins*obsCclay-Rclay*(mins-1)
        if obs >= mins*geoCobs-Robs*(mins-1): obs = mins*geoCobs-Robs*(mins-1)


        state = (Rore, Rclay, Robs, Rgeo, ore, clay, obs, geo, mins)
        if state in seen: continue
        seen.add(state)

        # Add step with no new robots
        queue.append((
            Rore, Rclay, Robs, Rgeo, 
            ore + Rore, clay + Rclay, obs + Robs, geo + Rgeo, 
            mins-1
        ))
        # go through every robot in blueprint
        if ore >= oreCore:
            queue.append((
                Rore+1, Rclay, Robs, Rgeo, 
                ore + Rore - oreCore, clay + Rclay, obs + Robs, geo + Rgeo, 
                mins-1
            ))
        if ore >= clayCore:
            queue.append((
                Rore, Rclay+1, Robs, Rgeo, 
                ore + Rore - clayCore, clay + Rclay, obs + Robs, geo + Rgeo, 
                mins-1
            ))
        if ore >= obsCore and clay >= obsCclay:
            queue.append((
                Rore, Rclay, Robs+1, Rgeo, 
                ore + Rore - obsCore, clay + Rclay - obsCclay, obs + Robs, geo + Rgeo, 
                mins-1
            ))
        if ore >= geoCore and obs >= geoCobs:
            queue.append((
                Rore, Rclay, Robs, Rgeo+1, 
                ore + Rore - geoCore, clay + Rclay, obs + Robs - geoCobs, geo + Rgeo, 
                mins-1
            ))


    return maxGeode

def part1(robots):
    quality = 0
    for ind, i in enumerate(robots):
        quality += (ind+1)*blueprintSimulation(i, 24)
    return quality

def part2(robots):
    quality = 1
    for i in robots[0:3]:
        quality *= blueprintSimulation(i, 32)
    return quality


print("Part 1: ", part1(robots))
print("Part 2: ", part2(robots))
