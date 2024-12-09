files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = map(int, list(f.read().strip()))

def p1(diskmap):
    diskmap = []
    for i,num in enumerate(data):
        if i%2 == 0: diskmap += [i//2]*num
        else: diskmap += ["."]*num
    
    while "." in diskmap:
        while diskmap[-1] == ".":
            diskmap.pop()
        diskmap[diskmap.index(".")] = diskmap.pop()
    
    return sum([i*int(n) for i,n in enumerate(diskmap)])

def p2(data):
    disks = dict()
    spaces = dict()
    index = 0
    for i, num in enumerate(data):
        if i%2 == 0: disks[i//2] = (index, num)
        else: spaces[index] = num
        index += num
    
    for d in sorted(disks.keys(),reverse=True):
        start, length = disks[d]
        for s in sorted(spaces.keys()):
            if s > start: break
            if spaces[s] >= length:
                disks[d] = (s, length)
                spaceLeft = spaces[s] - length
                spaces.pop(s)
                if spaceLeft > 0:
                    spaces[s+length] = spaceLeft
                break
    
    checksum = 0
    for num, (start, length) in disks.items():
        checksum += num*(start*length+length*(length-1)//2)

    return checksum
    
print("Part 1: ", p1(data))
print("Part 2: ", p2(data))