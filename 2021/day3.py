class Num:
    def __init__(self, str):
        self.nums = [int(str[0]), int(str[1]), int(str[2]), int(str[3]),int(str[4]), int(str[5]), int(str[6]), int(str[7]),int(str[8]), int(str[9]), int(str[10]), int(str[11])]

def binToNum(bin):
    i = 0
    num = 0
    for i in range(len(bin)):
        num += 2^(i)*bin[i]
    return num

with open('day3.txt') as f:
    lines = f.readlines()

numbers = []
for str in lines:
    numbers.append([int(str[0]), int(str[1]), int(str[2]), int(str[3]),int(str[4]), int(str[5]), int(str[6]), int(str[7]),int(str[8]), int(str[9]), int(str[10]), int(str[11])])

co2 = numbers2693
ind = 0
while len(co2) > 1 and ind < 12:
    total = 0

    for i in co2:
        total += i[ind]
    avg = total/len(co2)

    print(ind)
    print(int(round(avg,0)))

    for i in co2:
        if i[ind] != int(round(avg,0)):
            co2.remove(i)
            print(i)

    print("A")
    for i in co2:
        print(i)
    ind += 1


for i in co2:
    print(i)
#
#
# if total[0] > len(numbers)/2:
#         average = 1
#     else:
#         average = 0
#
# not_average = []
# for i in average:
#     if i == 0:
#         not_average.append(1)
#     else:
#         not_average.append(0)
#
# a = binToNum(average)
# b = binToNum(not_average)
# print(average)
# print(not_average)
# print(a)
# print(b)
# print(a*b)

co2 = 2693
