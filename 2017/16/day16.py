import string

ops = input().split(',')
penguins = list(string.ascii_lowercase[:16])

for op in ops:
    if op[0] == 's':
        n = int(op[1:])
        penguins = penguins[-n:] + penguins[:-n]
    elif op[0] == 'x':
        l, r = map(int, op[1:].split('/'))
        penguins[l], penguins[r] = penguins[r], penguins[l]
    elif op[0] == 'p':
        l, r = op[1:].split('/')
        p1, p2 = penguins.index(l), penguins.index(r)
        penguins[p1], penguins[p2] = penguins[p2], penguins[p1]

print(''.join(penguins))

