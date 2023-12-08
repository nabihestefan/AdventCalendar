with open("day3.txt", "r") as file:
    data = [str(line.strip()) for line in file]

def part1(data):
    epsilon = ""
    gamma = ""
    for i in range(len(data[0])):
        sum = 0
        for num in data: sum += int(num[i])
        if sum >= len(data)//2:
            epsilon += "0"
            gamma += "1"
        else:
            epsilon += "1"
            gamma += "0"
    return int(epsilon,2)*int(gamma,2)

def part2(data):
    ox_data = data[:]
    co_data = data[:]

    for i in range(len(ox_data[0])):
        ox_bit_list = []
        co_bit_list = []

        for point in ox_data:
            ox_bit_list.append(point[i])

        for point in co_data:
            co_bit_list.append(point[i])

        if ox_bit_list.count('1') >= ox_bit_list.count('0'):
            ox_common_point = '1'
        else:
            ox_common_point = '0'

        if co_bit_list.count('1') < co_bit_list.count('0'):
            co_common_point = '1'
        else:
            co_common_point = '0'

        ox_to_remove = []
        co_to_remove = []

        for point in ox_data:
            if point[i] != ox_common_point:
                ox_to_remove.append(point)

        for trash in ox_to_remove:
            if len(ox_data) > 1:
                ox_data.remove(trash)

        for point in co_data:
            if point[i] != co_common_point:
                co_to_remove.append(point)

        for trash in co_to_remove:
            if len(co_data) > 1:
                co_data.remove(trash)

    return int(ox_data[0],2) * int(co_data[0],2)

print("Part 1: ", part1(data))
print("Part 2: ", part2(data))
