import z3
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split(" @ ") for x in f.readlines()]

p1Data = []
p2Data = []
for pos, vel in data:
    x, y, z = [int(x) for x in pos.strip().split(",")]
    dx, dy, dz = [int(x) for x in vel.strip().split(",")]
    b = y - (dy/dx)*x
    p1Data.append((x, b, dx, dy))
    p2Data.append((x, y, z, dx, dy, dz))

def p1(data):
    total = 0
    minR, maxR = 200000000000000, 400000000000000
    for i in range(len(data)):
        xi, bi, dxi, dyi = data[i]
        for j in range(i+1, len(data)):
            xj, bj, dxj, dyj = data[j]
            if dyi/dxi == dyj/dxj: continue
            x = (bj - bi)/(dyi/dxi - dyj/dxj)
            y = (dyi/dxi)*x + bi
            if minR <= x <= maxR and minR <= y <= maxR:
                ti = (x - xi)/dxi
                tj = (x - xj)/dxj
                if ti >= 0 and tj >= 0: total += 1
    return total
            
def p2(data):
    F = lambda x: z3.Real(x)
    x, y, z = F("x"), F("y"), F("z")
    dx, dy, dz = F("dx"), F("dy"), F("dz")

    solver = z3.Solver()

    for i, rock in enumerate(data[:5]):
        xi, yi, zi, dxi, dyi, dzi = rock

        t = F("t{}".format(i))
        solver.add(t >= 0)
        solver.add(x + t*dx == xi + t*dxi)
        solver.add(y + t*dy == yi + t*dyi)
        solver.add(z + t*dz == zi + t*dzi)
    model = solver.model()
    sx, sy, sz = model.eval(x).as_long(), model.eval(y).as_long(), model.eval(z).as_long()
    return sx + sy + sz 

print("Part 1: ", p1(p1Data))
print("Part 2: ", p2(p2Data))