from hashlib import md5
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    data =  f.readlines()[0].strip()

hashes = dict()
def isKey(num, part2):
    global hashes
    if num not in hashes.keys():
        string = data + str(num)
        hash = md5(string.encode()).hexdigest()
        if part2:
            for i in range(2016):
                hash = md5(hash.encode()).hexdigest()
        hashes[num] = hash
    else:
        hash = hashes[num]
    for i in range(len(hash)-2):
        if hash[i] == hash[i+1] == hash[i+2]:
            d = hash[i] * 5
            for n in range(num+1, num+1000):
                if n not in hashes.keys():
                    string = data + str(n)
                    testH = md5(string.encode()).hexdigest()
                    if part2:
                        for i in range(2016):
                            testH = md5(testH.encode()).hexdigest()
                    hashes[n] = testH
                else:
                    testH = hashes[n]
                if d in testH: return True
            break
    return False

def run(p2):
    keys = 0
    n=0
    while keys < 64:
        if isKey(n,p2):
            keys+=1
        n+=1
    return n-1

print("Part 1: ", run(False))
hashes = dict()
print("Part 1: ", run(True))
