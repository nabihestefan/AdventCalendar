files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.split(",") for a in f.readlines()]
nums = [int(a) for a in lines[0]]


def run(nums, finish):
    dictSpoken = dict(zip(nums,range(1, len(nums) + 1)))
    lastSpoken = None
    for turn in range(len(nums)+1, finish+1):
        if lastSpoken == None:
            spoken = 0
        else:
            spoken = (turn-1) - lastSpoken

        try:
            lastSpoken = dictSpoken[spoken]
        except KeyError:
            lastSpoken = None

        dictSpoken[spoken] = turn
    return spoken

print("Part 1: ", run(nums, 2020))
print("Part 2: ", run(nums, 30000000))
