files = ['day8.txt', 'day8Test.txt']

with open(files[0], 'r') as f:
    lines =  f.readlines()
    content = [i.strip().split('|')[0].split(' ') for i in lines]
    content = [i[0:10] for i in content]

    answer = [i.strip().split('|')[1].split(' ') for i in lines]
    answer = [i[1:] for i in answer]

total = 0

for i in range(0,len(content)):
    output = ""
    for j in answer[i]:
        if len(j) == 2:
            output += "1"
        elif len(j) == 3:
            output += "7"
        elif len(j) == 4:
            output += "4"
        elif len(j) == 7:
            output += "8"
        elif len(j) == 5:
            key = content[i]
            key.sort(key = len)
            for k in key:
                if len(k) == 2 and ((k[0] in j) and (k[1] in j)):
                    output += "3"
                    break
                elif len(k) == 4:
                    x = 0
                    for letter in k:
                        if letter in j:
                            x += 1
                    if x == 3:
                        output += "5"
                        break
                    else:
                        output += "2"
                        break
        elif len(j) == 6:
            key = content[i]
            key.sort(key = len)
            for k in key:
                if len(k) == 2 and ((k[0] in j) ^ (k[1] in j)):
                    output += "6"
                    break
                elif len(k) == 4:
                    if ((k[0] in j) and (k[1] in j) and (k[2] in j) and (k[3] in j)):
                        output += "9"
                        break
                    else:
                        output += "0"
                        break

    print(output)
    total += int(output)
print(total)
