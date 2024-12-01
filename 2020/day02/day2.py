with open('day2.txt') as f:
    lines = f.readlines()

input = []
for i in lines:
    first = i.index(" ")
    nums = i[0:first]
    if nums[1] == "-":
        if len(nums) == 3:
            numbers = (int(i[0:1]), int(i[2:3]))
        else:
            numbers = (int(i[0:1]), int(i[2:4]))
    else:
        if len(nums) == 4:
            numbers = (int(i[0:2]), int(i[3:4]))
        else:
            numbers = (int(i[0:2]), int(i[3:5]))
    input.append((numbers, i[first+1], i[first+4:-1]))

valid = 0
for i in input:
    if (i[2][i[0][0]-1] == i[1]) ^ (i[2][i[0][1]-1] == i[1]):
        valid += 1

print(valid)
