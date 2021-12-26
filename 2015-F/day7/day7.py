## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  f.readlines()

wires = {}
for i in lines:
    arrow = i.index("->")
    wires[i[arrow+3:].strip()] = i[0:arrow-1]


## General

def value(wire):
    print(wire)
    try:
        wires[wire] = int(wire)
        return int(wire)
    except ValueError:
        wireValue = wires[wire]
        try:
            wires[wire] = int(wireValue)
            return int(wireValue)
        except ValueError:
            try:
                space = wireValue.index(" ")
                wire1 = wireValue[0:space]
                wireValue = wireValue[space+1:].strip()
                if wire1 == "NOT":
                    function = wire1
                    wire1 = wireValue[0:].strip()
                else:
                    space = wireValue.index(" ")
                    function = wireValue[0:space]
                    wire2 = wireValue[space+1:].strip()

                if function == "AND":
                    wireValue = value(wire1) & value(wire2)
                    wires[wire] = int(wireValue)
                    return wires[wire]
                elif function == "OR":
                    wireValue = value(wire1) | value(wire2)
                    wires[wire] = int(wireValue)
                    return wires[wire]
                elif function == "NOT":
                    num = bin(value(wire1))[2:]
                    for i in range(len(num),16):
                        num = "0" + num
                    answer = ""
                    for i in num:
                        if i == "1":
                            answer += "0"
                        else:
                            answer += "1"
                    wires[wire] = int(answer, 2)
                    return wires[wire]
                elif function == "LSHIFT":
                    wireValue = value(wire1) << int(wire2)
                    wires[wire] = int(wireValue)
                    return wires[wire]
                elif function == "RSHIFT":
                    wireValue = value(wire1) >> int(wire2)
                    wires[wire] = int(wireValue)
                    return wires[wire]
            except ValueError:
                wires[wire] = value(wireValue)
                return wires[wire]

## Part 1
v = value('a')
print(v)

## Part 2
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  f.readlines()

wires = {}
for i in lines:
    arrow = i.index("->")
    wires[i[arrow+3:].strip()] = i[0:arrow-1]
wires['b'] = v
v = value('a')
print(v)
