files = ['day10.txt', 'day10Test.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  f.readlines()
    positions = [x.split('')for x in f.readlines()]
