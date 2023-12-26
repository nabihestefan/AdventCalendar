files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(map(int, line.split())) for line in f.readlines()]

def resolve(numbers, partTwo):
    if len(set(numbers)) == 1:
        return numbers[-1]
    if partTwo:
        return numbers[0] - resolve([numbers[i+1] - numbers[i] for i in range(len(numbers)-1)], partTwo)
    else:
        return numbers[-1] + resolve([numbers[i+1] - numbers[i] for i in range(len(numbers)-1)], partTwo)

def run(data, partTwo):
    total = 0
    for numbers in data:
        total += resolve(numbers, partTwo)
    return total
            
print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))