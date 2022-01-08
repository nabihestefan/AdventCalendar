## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0   ], 'r') as f:
    line =  f.readlines()[0].strip()

def decompress(line):
    if '(' not in line:
        return len(line)
    answer = 0
    while '(' in line:
        answer += line.find("(")
        stopPoint = line[line.find("(")+1:line.find(")")].split("x")
        line = line[line.find(")")+1:]
        if partTwo:
            answer += decompress(line[:int(stopPoint[0])]) * int(stopPoint[1])
        else:
            answer += len(line[:int(stopPoint[0])]) * int(stopPoint[1])
        line = line[int(stopPoint[0]):]
    answer += len(line)
    return answer


partTwo = False
print("Part 1: ", decompress(line))

partTwo = True
print("Part 2: ", decompress(line))
