with open('input.txt','r') as f: lines = [a.strip().split() for a in f.readlines()]

def run():
    regs, maxTotal = dict(), 0
    for words in lines:
        if eval(str(regs.get(words[4], 0)) + words[5] + words[6]):
            val = int(words[2]) * -1 if words[1] == "dec" else int(words[2])
            regs[words[0]] = regs.get(words[0], 0) + val
            m\axTotal = max(maxTotal, regs[words[0]])
            
    return max(regs.values()), maxTotal

print("Part 1 & 2: ", run())
