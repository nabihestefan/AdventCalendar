import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n")

struct Box {
	let l: Int
	let w: Int
	let h: Int

	var surfaceArea: Int {
		return 2*(l*w) + 2*(l*h) + 2*(w*h) + [l*w, l*h, w*h].min()!
	}

	var ribbon: Int {
		let sTwo = [l,w,h].sorted(by: <)[0..<2]
		return sTwo[0] + sTwo[0] + sTwo[1] + sTwo[1] + (l*w*h)
	}
}

var boxes: [Box] = []
for line in data.dropLast() {
	let dims = line.components(separatedBy:"x").map {Int($0) ?? 0}
	boxes.append(Box(l:dims[0], w:dims[1], h:dims[2]))
}

let totalSA = boxes.map { $0.surfaceArea }.reduce(0, +)
print("Part 1: \(totalSA)")
let totalRibbon = boxes.map { $0.ribbon }.reduce(0, +)
print("Part 1: \(totalRibbon)")
