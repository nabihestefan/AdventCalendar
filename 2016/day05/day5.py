from hashlib import md5
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    doorID =  f.readlines()[0].strip()

def findNextHash(base, num):
    while True:
        num += 1
        hashable = base+str(num)
        string = md5(hashable.encode()).hexdigest()
        if string[0:5] == "00000":
            return (string[5], num)


def findNextHashP2(base, num):
    while True:
        num += 1
        hashable = base+str(num)
        string = md5(hashable.encode()).hexdigest()
        validInd = ["0","1","2","3","4","5","6","7"]
        if string[0:5] == "00000" and string[5] in validInd and password[int(string[5])] == "_":
            return (string[5:7], num)

password = ""
num = 0
for i in range(8):
    solve = findNextHash(doorID, num)
    password += str(solve[0])
    num = solve[1]

print("PART1")
print(password)



password = ["_","_","_","_","_","_","_","_"]
num = 0
for i in range(8):
    solve = findNextHashP2(doorID, num)
    password[int(solve[0][0])] = str(solve[0][1])
    num = solve[1]

print("PART2")
print("".join(password))
