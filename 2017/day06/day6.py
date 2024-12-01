with open('input.txt', 'r') as f:
    nums = [int(a) for a in f.readlines()[0].split("\t")]

def reDist(nums):
    maxVal = max(nums)
    maxI = nums.index(maxVal)
    nums[maxI] = 0
    i = (maxI+1)%len(nums)
    for _ in range(maxVal):
        nums[i] += 1
        i = (i+1)%len(nums)
    return nums

def run(nums, part2):
    configs = set()
    while tuple(nums) not in configs:
        configs.add(tuple(nums))
        nums = reDist(nums[:])
    if not part2: return len(configs)

    final = nums[:]
    steps = 1
    nums = reDist(nums[:])
    while nums != final:
        nums = reDist(nums[:])
        steps += 1
    return steps

print("Part 1:", run(nums, False))
print("Part 2:", run(nums, True))
