import Foundation
import CryptoKit
let files = ["input.txt", "test.txt"]
let data = try String(contentsOfFile: files[0])

extension String {
var MD5: String {
        let computed = Insecure.MD5.hash(data: self.data(using: .utf8)!)
        return computed.map { String(format: "%02hhx", $0) }.joined()
    }
}
var i = 0
var string = data + String(i)
while String(string.MD%.prefix(5)) != "00000" {
    i += 1
    string = data + String(i)
}

print("Part 1: \(i)")

i = 0
string = data + String(i)
while String(string.MD%.prefix(6)) != "000000" {
    i += 1
    string = data + String(i)
}

print("Part 2: \(i)")
