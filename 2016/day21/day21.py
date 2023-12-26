## Parsing
files = ['input.txt', 'testInput.txt']
def swapPos(word,x,y):
    if y < x: x,y = y,x
    return word[:x] + [word[y]] + word[x+1:y] + [word[x]] + word[y+1:]

def swapVal(word,x,y): return swapPos(word,word.index(x),word.index(y))

def rotateDir(word,dir,x):
    x = x%len(word)
    if x == 0: return word
    if dir=="left": return word[x:] + word[:x]
    elif dir == "right": return word[-x:] + word[:len(word)-x]

def rotatePos(word,x):
    i = word.index(x)
    i += (2 if i>= 4 else 1)
    return rotateDir(word, "right", i)

def reverse(word,x,y):
    if y < x: x,y = y,x
    return word[:x] + word[x:y+1][::-1] + word[y+1:]

def move(word,x,y):
    a = word.pop(x)
    return word[:y] + [a] + word[y:]

def scramble(word):
    word = list(word)
    with open(files[0], 'r') as f:
        for line in f.readlines():
            words = line.strip().split()
            inst = words[0]
            if inst == "swap":
                if words[1] == "position":
                    word = swapPos(word,int(words[2]), int(words[-1]))
                else: word = swapVal(word,words[2], words[-1])

            if inst == "rotate":
                type = words[1]
                if type in ["left", "right"]: word = rotateDir(word,type,int(words[2]))
                else: word = rotatePos(word,words[-1])

            if inst == "reverse":
                word = reverse(word, int(words[2]), int(words[-1]))

            if inst == "move":
                word = move(word, int(words[2]), int(words[-1]))
    f.close()
    return "".join(word)

def permutations(word):
    word = list(word)
    if len(word) == 0: return[]
    if len(word) == 1: return [word]
    l = []
    for i,m in enumerate(word):
        rem = word[:i]+word[i+1:]
        for p in permutations(rem):
            l.append([m]+p)
    return l



def unscramble(word):
    for perm in permutations(word):
        if word == scramble(perm):
            return "".join(perm)


print("Part 1: ", scramble("abcdefgh"))
print("Part 2: ", unscramble("fbgdceah"))
