data = []
with open("day3.txt", "r") as file:
    for line in file:
        temp = str(line.strip())
        data.append(temp)

ox_data = data.copy()
co_data = data.copy()

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

print(int(ox_data[0],2), int(co_data[0],2), int(ox_data[0],2) * int(co_data[0],2))
