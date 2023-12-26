files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = f.readlines()

bareData = [list(map(int, x.strip().split(":")[1].split())) for x in lines]

p1 = []
for i in range(len(bareData[0])):
    p1.append((bareData[0][i], bareData[1][i]))

p2 = [int("".join(x.strip().split(":")[1].split())) for x in lines]

def run(data):
    total = 1
    for b, c in data:
        bot = (-b + (b**2 - 4*c)**0.5)/-2
        top = (-b - (b**2 - 4*c)**0.5)/-2
        total *= (top//1) - (-(-bot//1)) + 1
    return int(total)

## OLD SOLUTION
## Before I remembered **0.5 is square root and isnt a library
# def run(data):
#     total = 1
#     for dist, record in data:
#         count = 0
#         for i in range(dist+1):
#             if i*(dist-i) > record: count += 1
#         total *= count
#     return total
            
print("Part 1: ", run(p1))
print("Part 2: ", run([p2]))