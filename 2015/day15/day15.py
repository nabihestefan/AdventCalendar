## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

ingredients = []
for i in lines:
    name = i[0:i.index(" ")]
    capacity = i[i.index("capacity")+9: i.index(", durability")]
    durability = i[i.index("durability")+11: i.index(", flavor")]
    flavor = i[i.index("flavor")+7: i.index(", texture")]
    texture = i[i.index("texture")+8: i.index(", calories")]
    calories = i[i.index("calories")+9:]
    amount = 0
    ingredient = [name, int(capacity), int(durability), int(flavor), int(texture), int(calories), int(amount)]
    ingredients.append(ingredient)

def getScore(bs, cin, choc, candy):
    ing = [bs, cin, choc, candy]
    if sum(ing) == 100:
        capacity = sum([ingredients[i][1]*ing[i] for i in range(len(ing))])
        if capacity < 0:
            capacity  = 0
        durability = sum([ingredients[i][2]*ing[i] for i in range(len(ing))])
        if durability < 0:
            durability  = 0
        flavor = sum([ingredients[i][3]*ing[i] for i in range(len(ing))])
        if flavor < 0:
            flavor  = 0
        texture = sum([ingredients[i][4]*ing[i] for i in range(len(ing))])
        if texture < 0:
            texture  = 0
        #Part 2
        calories = sum([ingredients[i][5]*ing[i] for i in range(len(ing))])
        if calories == 500:
            score = capacity * durability * flavor * texture
            return score
        else:
            return 0
    else:
        return 0

for i in ingredients:
    print(i)


best = 0
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l = 100-i-j-k
            best = max(best, getScore(i,j,k,l))

print(best)
