files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

def decToSNAFU(dec):
    if dec == 0: return ""
    if (dec % 5) == 0: return decToSNAFU(dec // 5) + "0" 
    if (dec % 5) == 1: return decToSNAFU(dec // 5) + "1"
    if (dec % 5) == 2: return decToSNAFU(dec // 5) + "2"
    if (dec % 5) == 3: return decToSNAFU((dec+2) // 5) + "="
    if (dec % 5) == 4: return decToSNAFU((dec+1) // 5) + "-"

def run(partTwo, data):
    total = 0
    indexes = ["=", "-", "0", "1", "2"]
    for i in data:
        for ind, c in enumerate(i[::-1]):
            total += (5 ** ind) * (indexes.index(c)-2)
    return decToSNAFU(total)

print("Part 1: ", run(False, data))
print("Part 2: Done!")
