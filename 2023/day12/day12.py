files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [(x.split(" ")[0], list(map(int, x.split(" ")[1].split(","))))  for x in f.readlines()]

def resolve(line, sets, curSet, index, memory):
    key = (index, curSet, ",".join([str(x) for x in sets]))
    if key in memory: return memory[key]

    for i in range(index, len(line)):
        char = line[i]
        
        if line[i] == "#": 
            if len(sets) == 0 or curSet >= sets[0]: return 0
            else: curSet += 1

        if line[i] == ".": 
            if curSet == 0: continue
            elif curSet != sets[0]: return 0
            elif curSet == sets[0]:
                ## If I finished a set, remove it and act like its a .
                if len(sets) == 1: 
                    if "#" in line[i+1:]: return 0
                    else: return 1
                return resolve(line, sets[1:], 0, i+1, memory)
            
        solve = 0
        if line[i] == "?":
            if curSet == sets[0]:
                ## If I finished a set, remove it and act like its a .
                if len(sets) == 1: 
                    if "#" in line[i+1:]: return 0
                    else: return 1
                solve += resolve(line, sets[1:], 0, i+1, memory)

            elif curSet > 0:
                ## If in the middle of a set act like its a # and continue
                solve += resolve(line, sets, curSet+1, i+1, memory)
            else:
                ## If I haven't started a set yet, try both options
                solve += resolve(line, sets, 1, i+1, memory) + resolve(line, sets, 0, i+1, memory)
            memory[key] = solve
            return solve
        
    if (sets == [] and curSet == 0) or (curSet == sets[0] and len(sets) == 1): return 1
    return 0

def run(data):
    total = 0
    for line, sets in data:
        total += resolve(line, sets, 0, 0, dict())
    return total
            
print("Part 1: ", run(data))
print("Part 2: ", run([(x+"?"+x+"?"+x+"?"+x+"?"+x, y+y+y+y+y) for x,y in data]))