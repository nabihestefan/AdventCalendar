import Foundation
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0])


func part1(data:String) -> Int {
	var houses = Array<(Int, Int)>()
	var pos = (x:0, y:0)
	houses.append(pos)
	for c in data {
		switch(c){
		case ">": pos.x += 1
		case "<": pos.x -= 1
		case "v": pos.y += 1
		case "^": pos.y -= 1
		default: break
		}
		if !houses.contains(where:{$0==pos}) { houses.append(pos) }
	}
	return houses.count
}

func part2(data:String) -> Int {
	var houses = Array<(Int, Int)>()
	var Spos = (x:0, y:0)
	var RSpos = (x:0, y:0)
	var turn = true
	houses.append(Spos)
	for c in data {
		if turn {
			switch(c){
			case ">": Spos.x += 1
			case "<": Spos.x -= 1
			case "v": Spos.y += 1
			case "^": Spos.y -= 1
			default: break
			}
			if !houses.contains(where:{$0==Spos}) { houses.append(Spos) }
		}
		else {
			switch(c){
			case ">": RSpos.x += 1
			case "<": RSpos.x -= 1
			case "v": RSpos.y += 1
			case "^": RSpos.y -= 1
			default: break
			}
			if !houses.contains(where:{$0==RSpos}) { houses.append(RSpos) }

		}
		turn = !turn
	}
	return houses.count
}

print("Part 1: \(part1(data:data))")
print("Part 2: \(part2(data:data))")
