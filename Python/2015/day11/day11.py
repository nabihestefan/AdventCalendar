## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    password =  [a for a in f.readlines()[0].strip()]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
banned = ['i', 'l', 'o']
len_password = 8
def find_next(current):
    new = current
    overflow = 0
    index = letters.index(current[len_password-1])

    if index >= 25:
        index = -1
        overflow = 1

    new[len_password-1] = letters[index+1]

    for i in range(1,len_password-1):
        if overflow == 1:
            index = letters.index(current[len_password-i-1])
            overflow = 0

            if index >=  25:
                index = -1
                overflow = 1

            new[len_password-i-1] = letters[index+1]

    return new

def valid(password):
    trio = False
    for i in range(len(password)-2):
        index = letters.index(password[i])
        if index < 24:
            if (password[i] == letters[index]) and (password[i+1] == letters[index+1]) and (password[i+2] == letters[index+2]):
                print(password[i])
                print(password[i+1])
                print(password[i+2])
                trio = True


    duos = 0
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            duos += 1
            i += 1
        i += 1

    ban = False
    for i in password:
        if i in banned:
            ban = True

    if trio and (duos >= 2) and not ban:
        return True
    else:
        return False

print(password)
# password = ['c','q','j','x','x','y','z','z']
password = find_next(password)
while not valid(password):
    print(password)
    password = find_next(password)

print(password)
