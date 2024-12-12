files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(x.strip()) for x in f.readlines()]

def fill(data, checked, i, j):
    group = [(i, j)]
    letter = data[i][j]
    checked[i][j] = False
    while len(group) > 0:
        i, j = group.pop(0)
        if i-1 >= 0 and data[i-1][j] == letter and checked[i-1][j] == None:
            checked[i-1][j] = False
            group.append((i-1, j))
        if i+1 < len(data) and data[i+1][j] == letter and checked[i+1][j] == None:
            checked[i+1][j] = False
            group.append((i+1, j))
        if j-1 >= 0 and data[i][j-1] == letter and checked[i][j-1] == None:
            checked[i][j-1] = False
            group.append((i, j-1))
        if j+1 < len(data[0]) and data[i][j+1] == letter and checked[i][j+1] == None:
            checked[i][j+1] = False
            group.append((i, j+1))
    return checked

def getPriceP1(checked):
    area = sum([x.count(False) for x in checked])
    perimeter = 0
    for i in range(len(checked)):
        for j in range(len(checked[0])):
            if checked[i][j] != False: continue
            if i-1 < 0                  or checked[i-1][j] != False: perimeter += 1
            if i+1 >= len(checked)      or checked[i+1][j] != False: perimeter += 1
            if j-1 < 0                  or checked[i][j-1] != False: perimeter += 1
            if j+1 >= len(checked[0])   or checked[i][j+1] != False: perimeter += 1
    return area*perimeter

def getPriceP2(checked):
    area = sum([x.count(False) for x in checked])
    perimeter = 0
    for i in range(len(checked)):
        for j in range(len(checked[0])):
            if checked[i][j] != False: continue
            # Check adjacent presense
            n  = i-1 >= 0               and checked[i-1][j] == False
            s  = i+1 < len(checked)     and checked[i+1][j] == False
            e  = j+1 < len(checked[0])  and checked[i][j+1] == False
            w  = j-1 >= 0               and checked[i][j-1] == False

            # Convex
            if not n and not w: perimeter += 1
            if not n and not e: perimeter += 1
            if not s and not w: perimeter += 1
            if not s and not e: perimeter += 1

            # Concave
            if n and w and checked[i-1][j-1] != False: perimeter += 1
            if n and e and checked[i-1][j+1] != False: perimeter += 1
            if s and w and checked[i+1][j-1] != False: perimeter += 1
            if s and e and checked[i+1][j+1] != False: perimeter += 1
    return area*perimeter

def run(data):
    # None is not seen, False is seen and not counted, True is seen and counted
    checked = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    p1 = p2 = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if checked[i][j]: continue
            checked = fill(data, checked, i, j)
            p1 += getPriceP1(checked)
            p2 += getPriceP2(checked)
            checked = [[True if x==False else x for x in y] for y in checked]
    return p1, p2
    
print("Part 1&2: ", run(data))