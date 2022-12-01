## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    containers =  [int(a.strip()) for a in f.readlines()]

ways = []
def permutationsToSum(items, total, conts):
    perms = 0
    i = 0
    while i < len(items):
        if items[i] == total:
            ways.append(conts)
            perms += 1
        elif items[i] < total:
            perms += permutationsToSum(items[i+1:], total-items[i], conts+1)
        else:
            perms +=  0
        i += 1
    return perms
# Part1
print(permutationsToSum(containers, 150, 0))

# Part2
minimum = min(ways)
forms = 0
for i in ways:
    if i == minimum:
        forms += 1
print(forms)
