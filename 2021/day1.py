with open('day1.txt') as f:
    lines = f.readlines()
measurements = []
for i in lines:
    measurements.append(int(i))

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
