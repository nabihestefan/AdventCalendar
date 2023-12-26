#decoded asssembly by hand
num = 14*182
n = 1
while n < num:
    if n%2 == 0: n = n*2 + 1
    else: n *=2
print("Part 1: ", n-num)
