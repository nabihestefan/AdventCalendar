## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    number = int(f.readlines()[0].strip())

print(number)

# #Part 1
# def get_factors(n):
#     x = 1
#     factors = []
#     while x ** 2 <= n:
#         if n % x == 0:
#             factors.append(x)
#             factors.append(n / x)
#         x += 1
#     return factors
#
# for n in range(6, 6000000, 6):
#     if(10 * sum(get_factors(n))) >= number:
#         print(n)
#         break

def get_factors(n):
    x = 1
    factors = []
    while x ** 2 <= n:
        if n % x == 0:
            factors.append(n / x)
        x += 1

        if x > 50:
            break
    return factors

for n in range(6, 6000000, 6):
    if(11 * sum(get_factors(n))) >= number:
        print(n)
        break
