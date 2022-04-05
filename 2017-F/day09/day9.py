with open('input.txt', 'r') as f: lines =  f.readlines()[0].strip()

def run():
    depth = garbage = total = i = 0
    valid = True
    while i < len(lines):
        if lines[i] == "!":
            i += 2
            continue
        if valid:
            if lines[i] == "<": valid = False
            if lines[i] == "{": depth += 1
            if lines[i] == "}":
                total += depth
                depth -= 1
        else:
            if lines[i] == ">": valid = True
            else: garbage += 1
        i += 1
    return total, garbage

print("Part 1 & 2: ", run())
