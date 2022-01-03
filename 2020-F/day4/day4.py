files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip()+" " for a in f.readlines()]
lines.append(" ")



hcl = lambda x: 1920 <= x and x <= 2002
pid = lambda x: 1920 <= x and x <= 2002

class Passport():
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None,
        ecl=None, pid=None, cid=None):
        self.byr=byr
        self.iyr=iyr
        self.eyr=eyr
        self.hgt=hgt
        self.hcl=hcl
        self.ecl=ecl
        self.pid=pid
        self.cid=cid


    def validPt1(self):
        if None in [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl,\
                    self.pid]:
            return False
        return True

    def validPt2(self):
        birth = lambda x: 1920 <= int(x) and int(x) <= 2002
        issue = lambda x: 2010 <= int(x) and int(x) <= 2020
        expiration = lambda x: 2020 <= int(x) and int(x) <= 2030
        def height(x):
            if x[-2:] == "cm": return 150 <= int(x[:-2]) and int(x[:-2]) <=193
            elif x[-2:] == "in": return 59 <= int(x[:-2]) and int(x[:-2]) <=76

        def hair(x):
            return x[0] == "#" and sum([True for a in x[1:] if a in ["0","1","2","3",\
                "4","5","6","7","8","9","a","b","c","d","e","f"]]) == 6

        eye = lambda x: x in ["amb","blu","brn","gry","grn","hzl","oth"]
        id = lambda x: len(x) == 9 and x.isdigit()

        if self.validPt1():
            if birth(self.byr) and issue(self.iyr) and expiration(self.eyr) \
                and height(self.hgt) and hair(self.hcl) and eye(self.ecl) \
                and id(self.pid):
                return True
        return False

passports = []
passport = Passport()

for i in lines:
    if i == " ":
        passports.append(passport)
        passport = Passport()
    else:
        while len(i)>1:
            if i[0:3] == "byr":
                passport.byr = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "iyr":
                passport.iyr = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "eyr":
                passport.eyr = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "hgt":
                passport.hgt = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "hcl":
                passport.hcl = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "ecl":
                passport.ecl = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "pid":
                passport.pid = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]
            if i[0:3] == "cid":
                passport.cid = i[4:i.index(" ")]
                i = i[i.index(" ")+1:]

validPt1 = 0
validPt2 = 0
for i in passports:
    if i.validPt1(): validPt1+=1
    if i.validPt2(): validPt2+=1

print("Part1: ", validPt1)
print("Part2: ", validPt2)
