import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0])//.split(separator = "\n")

var floor = 0
var partTwo = true
for (i,c) in data.enumerated() {
	if c == "(" {floor += 1}
	if c == ")" {floor -= 1}
	if floor == -1 && partTwo {
		print("Part 2: \(i+1)")
		partTwo = false
	}
}

print("Part 1: \(floor)")
