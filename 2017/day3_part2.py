d = {(0, 0): 1}

import sys


i = 0
j = 0
max_n = -1


layercount = 0
num = 2

def get(x, y):
    return d.get((x, y), 0)

def calc(x, y):
    global max_n
    t = 0
    print("calc called with {} {}".format(x, y))
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            t += get(x + dx, y + dy)
    if t >= 368078:
        print(t)
        sys.exit(0)
    d[(x, y)] = t

def perfect(x):
    from math import sqrt
    return int(sqrt(x)) ** 2 == x

def dist(x, y):
    return abs(x) + abs(y)

while max_n <= 368078:
# while num <= 361527:
    if perfect(num - 1):
        i += 1
        calc(i, j)
        layercount += 1
        num += 1
    else:
        for it in range(2 * layercount - 1):
            j += 1
            calc(i, j)
            num += 1
        for it in range(2 * layercount):
            i -= 1
            calc(i, j)
            num += 1
        for it in range(2 * layercount):
            j -= 1
            calc(i, j)
            num += 1
        for it in range(2 * layercount):
            i += 1
            calc(i, j)
            num += 1

print(max_n)




