files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    recipeNum = int(f.readlines()[0].strip())


recipes = [3,7]
elf1 = 0
elf2 = 1


while str(recipeNum) not in "".join([str(a) for a in recipes[-7:]]):
    print(len(recipes))
    newRecipe = str(recipes[elf1] + recipes[elf2])
    for i in newRecipe: recipes.append(int(i))
    elf1  = (elf1 + 1+recipes[elf1])%len(recipes)
    elf2  = (elf2 + 1+recipes[elf2])%len(recipes)

recipeStr = "".join([str(a) for a in recipes])
print("Part 1: ", recipeStr[recipeNum:recipeNum+10])
print("Part 2: ", recipeStr.index(str(recipeNum)))
