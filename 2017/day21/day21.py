with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

insts2 = dict()
insts3 = dict()

def rotate(section):
    if len(section) == 4:
        return [section[2], section[0],
                section[3], section[1]]

    return [section[6], section[3], section[0],
            section[7], section[4], section[1],
            section[8], section[5], section[2]]

def flip(section):
    if len(section) == 4:
        return [section[1], section[0],
                section[3], section[2]]

    return [section[2], section[1], section[0],
            section[5], section[4], section[3],
            section[8], section[7], section[6]]

for i in lines:
    og, to = i.strip().split("=>")
    start = []
    end = []
    for i in og:
        if i == ".": start.append(False)
        elif i == "#": start.append(True)
    for i in to:
        if i == ".": end.append(False)
        elif i == "#": end.append(True)
    if len(start) == 4: insts2[tuple(start)] = end
    elif len(start) == 9: insts3[tuple(start)] = end

insts = {2: insts2, 3:insts3}

def run(steps):
    grid = [[False, True, False], [False, False, True], [True, True, True]]
    for step in range(steps):
        #For every step
        next = []
        fixed = False
        for val in [2,3]:
            # Checked divisble by 2 or 3
            if len(grid)%val == 0 and not fixed:
                # If its divisible and it hasnt been fixed already
                fixed = True
                for row in range(len(grid)//val):
                    # For every row section
                    for i in range(val+1): next.append([])
                    # Create blank row in next grid
                    for col in range(len(grid)//val):
                        # For every column section
                        tempGrid = []
                        # Create temporary grid for key
                        for i in range(val):
                            tempGrid.append(grid[(row*val)+i][(col*val):(col*val)+val])
                        # Collapse key into single dim array
                        section = sum(tempGrid, [])
                        # Rotate and flip until you find key configuration
                        for rot in range(8):
                            if tuple(section) in insts[val].keys():
                                nextSec = insts[val][tuple(section)]
                                break
                            if rot == 4: section = flip(section)
                            else: section = rotate(section)
                        # Once found go through the array and add the new values
                        for i in
                        nextGrid = [] range(val+1):
                            next[(row*(val+1))+i] += nextSec[i*(val+1): i*(val+1)+(val+1)]

        # If youre ending dont copy to grid, not worth it
        if step == steps-1:
            return sum(sum(next, []))

        # Copy to grid for next iteration
        grid = next[:]

def part2():

    return None

print("Part 1: ", run(5))
print("Part 2: ", run(18))
