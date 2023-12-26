with open('day1.txt') as f:
    lines = f.readlines()

nums = []
for i in lines:
    nums.append(int(i))

i = 0
j = 1
k = 2
while i < len(nums):
    while j < len(nums):
        while k < len(nums):
            if nums[i]+nums[j]+nums[k]==2020:
                print(nums[i]*nums[j]*nums[k])
            k += 1
        j += 1
        k = j + 1

    i += 1
    j = i + 1
