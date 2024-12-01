files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip() for x in f.readlines()]

data = lines

def run(data, partTwo=False):
    
    return None
    
print("Part 1: ", run(data))
print("Part 2: ", run(data, True))