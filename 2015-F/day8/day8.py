## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [i.strip() for i in f.readlines()]

total_dif = 0

## Part 1
# for i in lines:
#     total_dif += 2
#     j = 0
#     while j < len(i):
#         if i[j] == '\\':
#             if i[j+1] == 'x':
#                 total_dif += 3
#             else:
#                 total_dif += 1
#                 j += 1
#         j += 1

## Part 2
for i in lines:
    j = 0
    before = total_dif
    total_dif += 4
    while j < len(i):
        if i[j] == '\\':
            if i[j+1] == 'x':
                total_dif += 1
            else:
                total_dif += 2
                j += 1
        j += 1

print(total_dif)
