files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]

def mix(secret, num): return secret ^ num
def prune(secret): return secret % 16777216
def nextSecret(secret):
    secret = prune(mix(secret, secret*64))
    secret = prune(mix(secret, secret//32))
    secret = prune(mix(secret, secret*2048))
    return secret

def run(nums, partTwo=False):
    difs = [[] for _ in nums]
    prevPrices = [i%10 for i in nums]
    seqs = [set() for _ in nums]
    seqPrices = dict()
    for trial in range(2000):
        newNums = []
        prevPrices = prices
        prices = []

        for n in range(len(nums)):
            newNums.append(nextSecret(nums[n]))
            prices.append(newNums[-1]%10)
            difs[n].append(prices[n] - prevPrices[n])

            if trial >= 3:
                seq = tuple(difs[n][-4:])
                if seq in seqs[n]: continue
                seqs[n].add(seq)
                seqPrices[seq] = seqPrices.get(seq, 0) + prices[-1]

        nums = newNums

    return sum(nums), max(seqPrices.values())
    
print("Part 1&2: ", run(data))
