files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: modules =  [int(a.strip()) for a in f.readlines()]

def massToFuel(mass):
    return (mass//3)-2 if ((mass//3)-2)>=0 else 0


total = 0
fuel = 0
for i in modules:
    total += massToFuel(i)
    while i > 0:
        i = massToFuel(i)
        fuel += i

print("Part 1: ", total)
print("Part 2: ", fuel)
