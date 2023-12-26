import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n").dropLast()

var wires: [String:String] = [:]
for line in data {
	let insts = line.components(separatedBy: " -> ")
	wires[insts[1]] = insts[0]
}

func isNumber(num:String) -> Bool {
	return num.range(of:"[^0-9]", options: .regularExpression) == nil
}

func not(val:Int) -> Int {
	var bin = String(val, radix:2)
	var newNum = ""
	for _ in bin.count...15 { bin = "0"+bin }
	for i in bin {
		if i == "0" { newNum += "1" }
		if i == "1" { newNum += "0" }
	}
	return Int(newNum, radix:2) ?? 0
}

func getValue(wire: String) -> Int {
	if isNumber(num: wire) {
		wires[wire] = wire
		return Int(wire) ?? 0
	}
	var wireVal = wires[wire] ?? "0"
	if isNumber(num: wireVal) { return Int(wireVal) ?? 0 }
	let words = wireVal.components(separatedBy: " ")
	if words.count == 1 {
		wires[wire] = String(getValue(wire:wireVal))
		return Int(wires[wire] ?? "0") ?? 0
	}
	var wire1 = words[0]
	var function = ""
	var wire2 = ""
	if wire1 == "NOT" {
		function = wire1
		wire1 = words[1]
	} else {
		function = words[1]
		wire2 = words[2]
	}

	if function == "AND" {
		wireVal = String(getValue(wire:wire1) & getValue(wire:wire2))
		wires[wire] = String(wireVal)
	} else if function == "OR" {
		wireVal = String(getValue(wire:wire1) | getValue(wire:wire2))
		wires[wire] = String(wireVal)
	} else if function == "NOT" {
		wireVal = String(not(val:getValue(wire:wire1)))
		wires[wire] = String(wireVal)
	} else if function == "LSHIFT" {
		let shift = Int(wire2) ?? 0
		wireVal = String(getValue(wire:wire1) << shift)
		wires[wire] = String(wireVal)
	} else if function == "RSHIFT" {
		let shift = Int(wire2) ?? 0
		wireVal = String(getValue(wire:wire1) >> shift)
		wires[wire] = String(wireVal)
	}

	return Int(wires[wire] ?? "0") ?? 0
}

let pt1 = getValue(wire:"a")
print("Part 1: \(pt1)")


wires = [:]
for line in data {
	let insts = line.components(separatedBy: " -> ")
	wires[insts[1]] = insts[0]
}
wires["b"] = String(pt1)
let pt2 = getValue(wire:"a")
print("Part 2: \(pt2)")
