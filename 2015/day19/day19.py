## Parsing
files = ['input.txt', 'testInput.txt']
replacements = []
for line in open(files[0], 'r'):
    sections = line.strip().split(" => ")
    if len(sections) == 1:
        if not line.strip():
            continue
        molecule = line.strip()
        continue
    replacements.append((sections[0], sections[1]))


new_molecules = set()

for source, replacement in replacements:
    ind = 0
    while source in molecule:
        ind = molecule.find(source, ind+1)
        if ind == -1:
            break
        new_molecules.add(molecule[:ind] + replacement + molecule[ind+len(source):])
print("PART1")
print(len(new_molecules))

mol = molecule
c = 0
while mol != 'e':
    for source, replacement in replacements:
        if replacement in mol:
            mol = mol.replace(replacement, source, 1)
            c += 1
print("PART2")
print(c)
