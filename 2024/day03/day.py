import re
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f: data = f.read()

def run(data):
    p1 = p2 = 0
    execute = True
    for i,j,k in re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)|(don\'t\(\)|do\(\))', data):
        if k == "don't()": execute = False
        elif k == "do()": execute = True
        else:
            p1 += int(i) * int(j)
            if execute: p2 += int(i) * int(j)
    return p1, p2
    
print("Part 1&2: ", run(data))