files = ['input.txt', 'inputTest.txt']
## Parsing
instructions = []
for line in open(files[0]):
    x = line.index("x")
    y = line.index("y")
    z = line.index("z")
    instructions.append((line[0:line.index(" ")],
                (int(line[x+2:line.index("..")]), int(line[line.index("..")+2:line.index(",")])),
                (int(line[y+2:line.index("..", y)]), int(line[line.index("..", y)+2:line.index(",", y)])),
                (int(line[z+2:line.index("..", z)]), int(line[line.index("..", z)+2:-1]))))

class Cube:
    def __init__(self, x, y, z, oper = 1):
        self.x = x
        self.y = y
        self.z = z
        self.oper = oper

    def size(self):
        x = self.x[1] - self.x[0] + 1
        y = self.y[1] - self.y[0] + 1
        z = self.z[1] - self.z[0] + 1
        return x*y*z * self.oper

def inBounds(i):
    if (i[1][0] > 50 and i[1][1] > 50) or (i[2][0] > 50 and i[2][1] > 50) or (i[3][0] > 50 and i[3][1] > 50):
        return False
    if (i[1][0] < -50 and i[1][1] < -50) or (i[2][0] < -50 and i[2][1] < -50) or (i[3][0] < -50 and i[3][1] < -50):
        return False
    return True

def lineInter(a,b):
    left = max(a[0],b[0])
    right = min(a[1],b[1])
    if right - left < 0:
        return False
    return (left, right)

def intersection(a,b):
    x = lineInter(a.x, b.x)
    y = lineInter(a.y, b.y)
    z = lineInter(a.z, b.z)
    if x and y and z:
        return Cube(x,y,z)
    return False

def run(partTwo):
    cubes = []
    for i in instructions:
        if inBounds(i) or partTwo:
            xs = i[1]
            ys = i[2]
            zs = i[3]
            if i[0] == "on": oper = 1
            else: oper = -1
            cubes.append(Cube(xs, ys, zs, oper))

    final = [cubes[0]]
    for cube in cubes[1:]:
        for otherCube in final.copy():
            inter = intersection(cube, otherCube)
            if inter:
                if otherCube.oper == 1:
                    inter.oper = -1
                final.append(inter)
        if cube.oper == 1:
            final.append(cube)

    count = 0
    for i in final:
        count += i.size()
    return count

print("Part 1: ", run(False))
print("Part 2: ", run(True))
