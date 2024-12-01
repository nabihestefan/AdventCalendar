## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
IPs = []
for i in lines:
    ip, single = [], ""
    for j in i:
        if j == "[" or j == "]":
            ip.append(single)
            single = ""
        else: single += j

    ip.append(single)
    IPs.append(ip)

def hasABBA(str):
    abba = False
    for i in range(len(str)-3):
        if str[i] == str[i+3] and str[i+1] == str[i+2] and str[i] != str[i+1]:
            abba = True
    return abba

supported = 0

for ip in IPs:
    hasAbbaOutside = False
    hasAbbaInside = False
    for ind,str in enumerate(ip):
        if ind%2 == 0: hasAbbaOutside = hasAbbaOutside or hasABBA(str)
        else: hasAbbaInside = hasAbbaInside or hasABBA(str)
    if hasAbbaOutside and not hasAbbaInside: supported += 1

print("PART1")
print(supported)

def supportsSSL(ip):
    abas = []
    for i in range(0, len(ip), 2):
        for j in range(len(ip[i])-2):
            if ip[i][j] == ip[i][j+2] and ip[i][j] != ip[i][j+1]:
                abas.append(ip[i][j:j+3])

    expected_babs = ["".join([i[1],i[0], i[1]]) for i in abas]

    for i in range(1, len(ip), 2):
        for j in expected_babs:
            if j in ip[i]: return True
    return False


supported = 0

for ip in IPs:
    if supportsSSL(ip):
        supported += 1


print("PART2")
print(supported)
