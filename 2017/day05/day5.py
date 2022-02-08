with open('input.txt', 'r') as f: nums = [int(a) for a in f.readlines()]

def run(nums, part2):
    steps, i = 0,0
    while i < len(nums):
        steps += 1
        inst = nums[i]
        nums[i] = inst + 1 if inst < 3 or not part2 else inst -1
        i += inst
    return steps


print("Part 1: ", run(nums[:], False))
print("Part 2: ", run(nums[:], True))
