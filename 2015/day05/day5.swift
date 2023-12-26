import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n").dropLast()

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

func isNicePt1(string:String) -> Bool {
	let v = Set(["a", "e", "i", "o", "u"])
	let vowels = string.filter { v.contains($0.lowercased()) }.count

	var illegal = false
	for i in ["ab", "cd", "pq", "xy"] {
		if string.contains(i) { illegal = true }
	}

	var double = false
	for (i,c) in string.dropLast().enumerated() {
		if c == string[i+1] { double = true}
	}

	if vowels >= 3 && !illegal && double {
		return true
	}

	return false
}

func isNicePt2(string:String) -> Bool {
	var paired = false
	var pair: String
	for (i,_) in string.dropLast().enumerated() {
		pair = String(string[string.index(string.startIndex, offsetBy:i)...string.index(string.startIndex, offsetBy:i+1)])
		let restI = string.index(string.startIndex, offsetBy:i+2)..<string.endIndex
		if String(string[restI]).contains(pair) {
			paired = true
			break
		}
	}

	var skipped = false
	for (i,c) in string.dropLast().dropLast().enumerated() {
		if c == string[i+2]{
			skipped = true
			break
		}
	}

	if paired && skipped {
		return true
	}

	return false
}

var nicePt1 = 0
var nicePt2 = 0
for line in data {
	if isNicePt1(string:line) { nicePt1 += 1 }
	if isNicePt2(string:line) { nicePt2 += 1 }
}

print("Part 1: \(nicePt1)")
print("Part 2: \(nicePt2)")
