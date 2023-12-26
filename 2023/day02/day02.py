files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

def run(data):
    p1, p2 = 0, 0
    for line in data:
        cubes = {"red" : 0, "blue": 0, "green": 0}
        for game in line.split(":")[1].split(";"):
            for cube in game.split(","):
                cubes[cube.split()[1]] = max(cubes[cube.split()[1]], int(cube.split()[0]))
        if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
            p1 += int(line.split(":")[0].split()[1])
        p2 += cubes["red"] * cubes["green"] * cubes["blue"]

    return p1, p2
            
print("Part 1 & 2: ", run(data))
