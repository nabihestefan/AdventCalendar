import hashlib

## Parsing
with open('day4.txt', 'r') as f:
    string =  f.readlines()[0].strip()

for i in range(10000000):
    choice = (string + str(i))
    encoded = hashlib.md5(choice.encode()).hexdigest()
    if encoded[0:6] == '000000':
        print(choice)
        break
