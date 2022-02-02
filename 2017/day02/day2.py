with open('input.txt', 'r') as f:
    nums =  [sorted(map(int, a.strip().split("\t"))) for a in f.readlines()]



def run(nums, partTwo):
    checksum = 0
    for row in nums:
        if not partTwo:
            checksum += row[-1] - row[0]
        else:
            found = False
            while not found:
                div = row.pop(0)
                for i in row:
                    if i%div==0:
                        checksum += i//div
                        found = True
    return checksum

print("Part 1: ", run(nums, False))
print("Part 2: ", run(nums, True))
