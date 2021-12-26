## Parsing
from itertools import combinations
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines = f.readlines()

weapons = [line.split() for line in lines[1:6]]
armors = [line.split() for line in lines[8:13]]
rings = [line.split() for line in lines[15:21]]
boss = [line.split() for line in lines[22:]]
armors.append([0 for ring in range(4)])
rings.extend([[0 for ring in range(5)] for j in range(2)])

def damageToBoss(weapon, armor, ring):
    return max(1, int(weapon[2]) + int(ring[0][3]) + int(ring[1][3]) - int(boss[2][1]))

def damageToUser(weapon, armor, ring):
    return max(1, int(boss[1][1]) - int(armor[3]) - int(ring[0][4]) - int(ring[1][4]))


print("PART1")
print(min([int(weapon[1]) + int(armor[1]) + int(ring[0][2]) + int(ring[1][2])
           for weapon in weapons
           for armor in armors
           for ring in combinations(rings, 2)
           if ((int(boss[0][2])-1)//damageToBoss(weapon,armor,ring)) <= (99//damageToUser(weapon,armor,ring))]))

print("PART2")
print(max([int(weapon[1]) + int(armor[1]) + int(ring[0][2]) + int(ring[1][2])
           for weapon in weapons
           for armor in armors
           for ring in combinations(rings, 2)
           if ((int(boss[0][2])-1)//damageToBoss(weapon,armor,ring))-1 >= (99//damageToUser(weapon,armor,ring))]))
