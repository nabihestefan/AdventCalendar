files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().split("\n\n")

machines = []
div = ["+", "+", "="]
for d in data:
    m = []
    for i, str in enumerate(d.split("\n")):
        m.append([int(str.split(div[i])[1]) for str in str.split(",")])
    machines.append(m)


def getPrice(machine, partTwo):
    a,b,p = machine
    if partTwo: p = (p[0]+10000000000000, p[1]+10000000000000)
    # Crude matrix visualization
    # [a0 b0] [ap] = [p0]
    # [a1 b1] [bp]   [p1]

    # [ap] = [a0 b0]^-1 * [p0]
    # [bp]   [a1 b1]      [p1]

    # [a0 b0]^-1 = 1/det * [b1 -b0]
    # [a1 b1]              [-a1 a0]

    # Substitute the things in and simplify equations and voila!

    det = a[0]*b[1] - b[0]*a[1]
    ap =  b[1]*p[0] - b[0]*p[1]
    bp =  a[0]*p[1] - a[1]*p[0]
    
    if ap%det != 0 or bp%det != 0: return 0
    ap = ap//det
    bp = bp//det

    if ap<0 or bp<0: return 0
    if not partTwo and (ap>100 or bp>100): return 0
    return 3*ap + bp

def run(machines, partTwo=False):
    total = 0
    for m in machines:
        total+= getPrice(m, partTwo)
    return total
    
print("Part 1: ", run(machines))
print("Part 2: ", run(machines, True))