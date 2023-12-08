import Foundation
let files = ["input.txt", "test.txt"]
var data = try String(contentsOfFile: files[0])
data.removeLast()

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

func expand(num:String) -> String {
	var cur = num[0]
	var times = 0
	var newNum: String = ""
	for i in num {
		if i != cur {
			newNum += String(times)
			newNum += String(cur)
			cur = i
			times = 1
		} else { times += 1 }
	}
	newNum += String(times)
	newNum += String(cur)
	return newNum
}

for _ in 0...39{
	data = expand(num:data)
}

print("Part 1: \(data.count)")

for _ in 0...9{
	data = expand(num:data)
}

print("Part 2: \(data.count)")
