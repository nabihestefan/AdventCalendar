files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().split("\n\n")

WIRES = dict()
for line in data[0].splitlines():
    wire, val = line.split(': ')
    WIRES[wire] = bool(int(val))

ogGates = dict()
for line in data[1].splitlines():
    gate, output = line.split(' -> ')
    gate1, gateType, gate2 = gate.split(' ')
    if gateType == 'AND': func = lambda x, y: x & y
    elif gateType == 'OR': func = lambda x, y: x | y
    elif gateType == 'XOR': func = lambda x, y: x ^ y
    ogGates[output] = (func, gate1, gate2, gateType)

def resolve(gates, gate):
    if gate in WIRES: return WIRES[gate]
    func, gate1, gate2, _ = gates[gate]
    return func(resolve(gates, gate1), resolve(gates, gate2))

def p1(gates):
    for gate in gates:
        WIRES[gate] = resolve(gates, gate)

    val = dict()
    for wire in WIRES:
        if wire[0] != "z": continue
        val[int(wire[1:])] = WIRES[wire]
    
    total = 0
    for i in range(len(val.keys())):
        total |= int(val[i]) << i

    return total
    
# Part 2
# ('Z bin:     ', '0b11 1011 1100 1010 0101 1100 1101 1100 0110 0011 1111 0000')
# ('Exp Z bin: ', '0b11 1011 1100 1001 1101 1011 1101 1100 0110 0100 0111 0000')
# Bits that are wrong
# 7, 8, 9, 10, 24, 25, 26, 31, 32, 33
# Manually inspect. Last swap wasn't activated in my sum and I had to manually find it


def p2(gates):
    swaps = [("swt", "z07"), ("wsv", "rjm"), ("bgs", "z31"), ("z13", "pqc")]
    for swap in swaps: gates[swap[0]], gates[swap[1]] = gates[swap[1]], gates[swap[0]]
    x = y = 0
    for wire in WIRES:
        if wire[0] == "x": x |= WIRES[wire] << int(wire[1:])
        elif wire[0] == "y": y |= WIRES[wire] << int(wire[1:])

    zExp = str(bin(x+y))[2:][::-1]
    Z = str(bin(p1(gates)))[2:][::-1]
    print(zExp)
    print(Z)
    for i in range(len(Z)):
        if Z[i] != zExp[i]:
            print(i, Z[i], zExp[i])
    
    if x+y == p1(gates): return ",".join(sorted(list(sum(swaps, ()))))
    return "Failed"

print("Part 1: ", p1(ogGates))
# Reset WIRES
WIRES = dict()
for line in data[0].splitlines():
    wire, val = line.split(': ')
    WIRES[wire] = bool(int(val))
print("Part 2: ", p2(ogGates))