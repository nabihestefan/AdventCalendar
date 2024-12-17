files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip() for x in f.readlines()]

A = int(lines[0].split(":")[1].strip())
B = int(lines[1].split(":")[1].strip())
C = int(lines[2].split(":")[1].strip())
program = map(int, lines[4].split(":")[1].strip().split(","))

## Original P1
def run(A, B, C, program):
    i = 0
    out = ""
    while i < len(program):
        opcode, operand = program[i], program[i+1]
        # Make it combo if needed
        if opcode in [0, 2, 5, 6, 7]:
            if operand == 4: operand = A
            elif operand == 5: operand = B
            elif operand == 6: operand = C

        if opcode == 0: A = int(A/pow(2,operand))
        elif opcode == 1: B = B^operand
        elif opcode == 2: B = operand%8
        elif opcode == 3 and A != 0: i = operand - 2
        elif opcode == 4: B = B^C
        elif opcode == 5: out += str(operand%8)+","
        elif opcode == 6: B = int(A/pow(2,operand))
        elif opcode == 7: C = int(A/pow(2,operand))
        i += 2
    return out[:-1]

# Manually simplified from visual inspection
def simpleProgram(a):
    b = (a%8)^5
    c = a//(2**b)
    b = (b^6)^c
    return  b % 8

# P1 after manually simplifying for p2
def p1(A):
    out = ""
    while A:
        out += str(simpleProgram(A))+","
        A = A//8
    return out[:-1]

def p2(program):
    a = 3
    for val in program[::-1][1:]:
        t = 8*a
        while simpleProgram(t) != val: t += 1
        a = t
    return a
    
print("Part 1: ", run(A, B, C, program))
print("Part 1 (again): ", p1(A))
print("Part 2: ", p2(program))