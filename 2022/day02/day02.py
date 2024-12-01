files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.replace(" ", "") for x in f.read().split("\n")]

def run(partTwo, data):
    moves = {"X":1, "Y":2, "Z":3}
    if partTwo:
        states = {"AX": "Z", "BY": "Y", "CZ": "X",
                  "AY": "X", "BZ": "Z", "CX": "Y",
                  "AZ": "Y", "BX": "X", "CY": "Z"}
        results = {"X":0, "Y":3, "Z":6}
    else:
        states = {"AX": 3, "BY": 3, "CZ": 3,
                  "AY": 6, "BZ": 6, "CX": 6,
                  "AZ": 0, "BX": 0, "CY": 0}
    
    total = 0
    for i in data:
        if partTwo: 
            total += moves[states[i]]
            total += results[i[1]]
        else: 
            total += states[i]
            total += moves[i[1]]
    return total

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
