## Parsing
import json

files = ['input.txt', 'testInput.txt']
data = json.loads(open(files[0], 'r').read())

## Part 1
def sum_numbers(obj):
    if type(obj) == type(dict()):
        if "red" in obj.values():
            return 0
        return sum(map(sum_numbers, obj.values()))

    if type(obj) == type(list()):
        return sum(map(sum_numbers, obj))

    if type(obj) == type(0):
        return obj

    return 0

print(sum_numbers(data))
