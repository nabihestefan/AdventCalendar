files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    line = f.readlines()[0]

row = int(line[line.index("row")+4: line.index(", column")])
col = int(line[line.index("column")+7: line.index(".\n")])

number = 20151125
r,c = 1,1

while True:
    if r == row and c == col:
        break
    r -= 1
    c += 1
    if r == 0:
        r = c
        c = 1
    number = (number * 252533) % 33554393

print(number)
