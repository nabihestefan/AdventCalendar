files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    line = f.readlines()[0].strip()

hexToBin = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100",
    "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010",
    "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

bitLine = ""
for i in line: bitLine += hexToBin[i]
versions = 0
partTwo = False
def unpack(bitLine):
    global versions
    i=0
    version = int(bitLine[i:i+3], 2)
    i+=3
    typeID = int(bitLine[i:i+3], 2)
    i+=3
    versions += version

    if typeID == 4:
        packets = ""
        while True:
            packet = bitLine[i: i+5]
            i += 5
            packets += packet[1:]
            if packet[0] == "0":
                break
        return int(packets, 2), bitLine[i:]
    else:
        packets = []
        I = int(bitLine[i])
        i+=1
        if I == 0: ##bit length
            length = int(bitLine[i:i+15], 2)
            i+=15
            data = bitLine[i:]
            sub = data[:length]
            rest = data[length:]
            while sub:
                ans, sub = unpack(sub)
                packets.append(ans)
            if not partTwo: return packets, rest
        else:
            subpackets = int(bitLine[i:i+11], 2)
            i+=11
            rest = bitLine[i:]
            for i in range(subpackets):
                ans, rest = unpack(rest)
                packets.append(ans)
            if not partTwo: return packets, rest


    if typeID == 0: #sum
        return sum(packets), rest

    elif typeID == 1: #product
        product = 1
        for i in packets:
            product *= i
        return product, rest

    elif typeID == 2: #minimum
        return min(packets), rest

    elif typeID == 3: #maximum
        return max(packets), rest

    elif typeID == 5: #greater than
        if packets[0] > packets[1]:
            return 1, rest
        else:
            return 0, rest

    elif typeID == 6: #less than
        if packets[0] < packets[1]:
            return 1, rest
        else:
            return 0, rest

    elif typeID == 7: #equal to
        if packets[0] == packets[1]:
            return 1, rest
        else:
            return 0, rest


unpack(bitLine)
print("Part 1: ", versions)
partTwo = True
print("Part 2: ", int(unpack(bitLine)[0]))
