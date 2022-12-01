## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines = [a.strip() for a in f.readlines()]
    instructions = [[a[0:a.index(" ")], a[a.index(" ")+1:]] for a in lines]

for i in instructions:
    print(i)

registers = {"a":1, "b":0}
i = 0
while i < len(instructions):
    inst = instructions[i]
    print(i)
    print(inst)
    if inst[0] == "hlf":
        registers[inst[1]] /= 2
        i += 1
    elif inst[0] == "tpl":
        registers[inst[1]] *= 3
        i += 1
    elif inst[0] == "inc":
        registers[inst[1]] += 1
        i += 1
    elif inst[0] == "jmp":
        i += int(inst[1])
    elif inst[0] == "jie":
        if (registers[inst[1][0]] % 2) == 0:
            i += int(inst[1][2:])
        else:
            i += 1
    elif inst[0] == "jio":
        if registers[inst[1][0]] == 1:
            i += int(inst[1][2:])
        else:
            i += 1

print(registers["a"])
print(registers["b"])
