files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

nums = []
symbols = set()
for i, line in enumerate(data):
    j = 0
    while j < len(line):
        if not data[i][j].isdigit() and data[i][j] != ".":
            symbols.add((i,j))
            j += 1
            continue
        num = ""
        add = False
        start = j
        while j < len(line) and data[i][j].isdigit():
            num += data[i][j]
            j += 1
        if num != "": 
            nums.append((int(num), i, (start,j)))
            continue
        j += 1

def adj(i,js):
    return [(i-1, x) for x in range(js[0]-1, js[1]+1)] + [(i+1, x) for x in range(js[0]-1, js[1]+1)] + [(i, js[0]-1), (i, js[1])]

def run(nums, symbols):
    p1, p2 = 0, 0
    gears = {}
    for num, i, js in nums:
        for pos in adj(i, js):
            if pos in symbols: 
                p1 += num
                if data[pos[0]][pos[1]] == "*":
                    gears[pos] = gears.get(pos, []) + [num]
    for key in gears:
        if len(gears[key]) == 2:
            p2 += gears[key][0] * gears[key][1]

    return p1, p2
    
            
print("Part 1 & 2: ", run(nums, symbols))