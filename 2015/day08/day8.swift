import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n").dropLast()

var codeChars = 0
var memChars = 0
var expChars = 0

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

for line in data {
	codeChars += line.count
	memChars += line.count - 2
	expChars += line.count + 4
	var i = 0
	while i < line.count {
		if line[i] == "\\" {
			if line[i+1] == "x"{ memChars -= 3 }
			else {
				memChars -= 1
				i += 1
			}
		}
		i += 1
	}
	i = 0
	while i < line.count {
		if line[i] == "\\" {
			if line[i+1] == "x"{ expChars += 1 }
			else {
				expChars += 2
				i += 1
			}
		}
		i += 1
	}

}

print("Part 1: \(codeChars-memChars)")
print("Part 2: \(expChars-codeChars)")
