## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    number =  f.readlines()[0].strip()

num = number[0]
times = 0
new_number = ""
def iteration(number):
    num = number[0]
    times = 0
    new_number = ""
    for i in number:
        if i != num:
            new_number += str(times)
            new_number += num
            num = i
            times = 1
        else:
            times += 1

    new_number += str(times)
    new_number += num
    return new_number

for i in range(50):
    number = iteration(number)
print(len(number))
