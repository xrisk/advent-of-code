from itertools import cycle

lookup = set([])
vec = []
tmp = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        vec.append(int(line))
        tmp += vec[-1]
print(tmp)
tmp = 0
for x in cycle(vec):
    tmp += x
    if tmp in lookup:
        print(tmp)
        break
    else:
        lookup.add(tmp)
