files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    gridSN = int(f.readlines()[0].strip())



powers = {}
for x in range(1,301):
    for y in range(1,301):
        powers[(x,y)] = ((((((y*(x+10))+gridSN)*(x+10))//100)%10)-5)


def findPower(side,x,y):
    return sum([powers[(i,j)] for i in range(x,x+side) for j in range(y,y+side)])

gridSN = 18
def run(partTwo):
    mx=my=mv=mside= -1
    for x in range(1,301):
        for y in range(1,301):
            if partTwo:
                side = min(300-y, 300-x, 20)
                for side in range(1,side+1):
                    val = findPower(side,x,y)
                    if val > mv:
                        mx,my,mv,mside = x,y,val,side

            else:
                if x >= 298 or y >= 298:
                    break
                mside = 3
                val = findPower(3,x,y)
                if val > mv:
                    mx,my,mv = x,y,val
    return mx, my, mside

print("Part 1: ", run(False)[0:2])
print("Part 2: ", run(True))
