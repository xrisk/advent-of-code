import parseutils
import sets

let f = open("input.txt")
var vec: seq[int]
var t: int = 0
while not f.endOfFile():
    let s = f.readLine()
    var i: int
    discard parseInt(s, i)
    add(vec, i)
    t += i
echo t
t = 0
var idx = 0
var lookup = initSet[int]()
while true:
    t += vec[idx]
    if lookup.contains(t):
        echo t
        break
    lookup.incl(t)
    idx = (idx + 1) mod len(vec)
