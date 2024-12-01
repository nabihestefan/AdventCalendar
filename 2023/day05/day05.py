files = ['input.txt', 'inputTest.txt']          
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.read().split("\n\n")]

class Mapping:
    def __init__(self, str):
        lines = str.split("\n")[1:]
        self.maps = [list(map(int, line.split())) for line in lines]

    def checkSingle(self, seed):
        for dest, src, length in self.maps:
            if src <= seed < src+length:
                return dest + (seed - src)
        return seed
    
    def updateRange(self, seedRanges):
        nextStep = []
        for dest, src, length in self.maps:
            newRange = []
            while seedRanges:
                strt, ed = seedRanges.pop()
                before = (strt, min(ed,src))
                inter = (max(strt,src), min(ed,src+length))
                after = (max(strt,src+length), ed)
                if before[0] < before[1]: newRange.append(before)
                if inter[0] < inter[1]: 
                    nextStep.append((inter[0]-src+dest, inter[1]-src+dest))
                if after[0] < after[1]: newRange.append(after)
            seedRanges = newRange
        return nextStep+newRange
    
seeds = [int(x) for x in data[0].split(":")[1].split()]
maps = [Mapping(x) for x in data[1:]]
            

def run(seeds, data):
    p1 = p2 = 10000000000000
    for seed in seeds: 
        for singleMap in maps:
            seed = singleMap.checkSingle(seed)
        p1 = min(p1, seed)
        
    for strt, length in list(zip(seeds[::2], seeds[1::2])):
        ranges = [(strt, strt+length)]
        for singleMap in maps:
            ranges = singleMap.updateRange(ranges)
        p2 = min(p2, min(ranges)[0])
        
    return p1, p2

print("Part 1 & 2: ", run(seeds, maps))

