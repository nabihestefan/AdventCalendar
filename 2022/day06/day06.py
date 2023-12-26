files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().strip()

def run(length, data):
    for i, _ in enumerate(data):
        if length == len(set(data[i:i+length])): return i+length
            
print("Part 1: ", run(4, data))
print("Part 2: ", run(14, data))
