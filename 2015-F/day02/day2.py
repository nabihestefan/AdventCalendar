## Parsing
with open('day2.txt', 'r') as f:
    lines =  f.readlines()
    dimensions = [a.strip().split('x') for a in lines]

total = 0
for i in dimensions:
    print(i)
    dims = [int(i[0]),int(i[1]),int(i[2])]

    ##Part 1
    # sideWL = 2*w*l
    # sideWH = 2*w*h
    # sideLH = 2*l*h
    #
    # gift = sideWL + sideWH + sideLH + int(min(sideWL,sideWH,sideLH)/2)
    # total += gift

    ##Part 2
    total += dims[0]*dims[1]*dims[2]
    minim = min(dims)
    dims.remove(minim)
    total += 2*min(dims) + 2*minim
print(total)
