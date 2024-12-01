import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0]).components(separatedBy: "\n").dropLast()

extension Array {
    func decompose() -> (Iterator.Element, [Iterator.Element])? {
        guard let x = first else { return nil }
        return (x, Array(self[1..<count]))
    }
}

func between<T>(x: T, _ ys: [T]) -> [[T]] {
    guard let (head, tail) = ys.decompose() else { return [[x]] }
    return [[x] + ys] + between(x:x, tail).map { [head] + $0 }
}

var places: Set<String> = [data[0].components(separatedBy:" ")[0]]
for line in data {
	let words = line.components(separatedBy: " ")
	let source = words[0]
	let dest = words[2]
	places.insert(source)
	places.insert(dest)
}

var distances: [String:[String:Int]] = [:]
for source in places {
	var locations: [String:Int] = [:]
	for dest in places {
		if source != dest { locations[dest] = 0 }
	}
	distances[source] = locations
}

for line in data {
	let words = line.components(separatedBy: " ")
	let source = words[0]
	let dest = words[2]
	let dist = words[4]
	distances[source]![dest] = Int(dist)
	distances[dest]![source] = Int(dist)
}

func permutations<T>(xs: [T]) -> [[T]] {
    guard let (head, tail) = xs.decompose() else { return [[]] }
    return permutations(xs:tail).flatMap { between(x:head, $0) }
}

let p = permutations(xs:Array(places))
var shortest = 100000000
var longest = 0
for items in p {
	var dist = 0
	var i = 0
	while i < items.count-1 {
		dist += distances[items[i]]![items[i+1]]!
		i += 1
	}
	shortest = min(shortest, dist)
	longest = max(longest, dist)
}

print("Part 1: \(shortest)")
print("Part 2: \(longest)")
