import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n").dropLast()

var pointDict: [String: Bool] = [:]

for line in data {
	let words = line.components(separatedBy: " ")
	var from: [String]
	var to: [String]
	if words[0] == "toggle" {
		from = words[1].components(separatedBy: ",")
		to = words[3].components(separatedBy: ",")
	}
	else {
		from = words[2].components(separatedBy: ",")
	    to = words[4].components(separatedBy: ",")
	}
	let bottomX = Int(from[0]) ?? 0
	let bottomY = Int(from[1]) ?? 0
	let topX = Int(to[0]) ?? 0
	let topY = Int(to[1]) ?? 0
	for x in bottomX...topX {
		for y in bottomY...topY {
			let coord = String(x) + "," + String(y)
			if words[1] == "on" { pointDict[coord] = true }
			if words[1] == "off" { pointDict[coord] = false }
			if words[0] == "toggle" {
				pointDict[coord] = !(pointDict[coord] ?? false)
			}
		}
	}
}

let pt1 = pointDict.filter { key, value in
	return value
}.count
print("Part 1: \(pt1)")

var pointDictPt2: [String:Int] = [:]

for line in data {
	let words = line.components(separatedBy: " ")
	var from: [String]
	var to: [String]
	if words[0] == "toggle" {
		from = words[1].components(separatedBy: ",")
		to = words[3].components(separatedBy: ",")
	}
	else {
		from = words[2].components(separatedBy: ",")
	    to = words[4].components(separatedBy: ",")
	}
	let bottomX = Int(from[0]) ?? 0
	let bottomY = Int(from[1]) ?? 0
	let topX = Int(to[0]) ?? 0
	let topY = Int(to[1]) ?? 0
	for x in bottomX...topX {
		for y in bottomY...topY {
			let coord = String(x) + "," + String(y)
			if words[1] == "on" { pointDictPt2[coord] = (pointDictPt2[coord] ?? 0) + 1}
			if words[1] == "off" { pointDictPt2[coord] = (pointDictPt2[coord] ?? 0) - 1}
			if words[0] == "toggle"  { pointDictPt2[coord] = (pointDictPt2[coord] ?? 0) + 2}
			if (pointDictPt2[coord] ?? 0) < 0 { pointDictPt2[coord] = 0 }
		}
	}
}

let pt2 = pointDictPt2.values.reduce(0,+)

print("Part 2: \(pt2)")
