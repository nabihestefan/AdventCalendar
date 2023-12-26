files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [(int(x.strip()), i) for i, x in enumerate(f.readlines())]

def run(partTwo, data):
    nums = [(i[0]*811589153 if partTwo else i[0], i[1]) for i in data]

    for _ in range(10 if partTwo else 1):
        for i in data:
            if partTwo: i = (i[0]*811589153, i[1])
            if i[0] == 0: zeroVal = i

            index = nums.index(i)
            nums.remove(i)
            index = (index + i[0]) % (len(nums))
            if index == 0: nums.append(i)
            else: nums.insert(index, i)

    zero = nums.index(zeroVal)
    return sum(nums[(zero+i)%len(nums)][0] for i in [1000,2000,3000])

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
