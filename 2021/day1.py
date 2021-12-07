with open('day1.txt') as f:
    measurements = [int(x) for x in f.readlines()[.split('\n')]

i = 2
increases = 0
trios =[]
while i < len(measurements):
    trios.append(measurements[i-2]+measurements[i-1]+measurements[i])
    i += 1

i = 1
while i < len(trios):
    if trios[i-1] < trios[i]:
        increases += 1
    i += 1


print(increases)
