d = {}

i = 0
j = 0
layercount = 0
num = 2

def perfect(x):
    from math import sqrt
    return int(sqrt(x)) ** 2 == x

def dist(x, y):
    return abs(x) + abs(y)

while num <= 368078:
    if perfect(num - 1):
        i += 1
        d[num] = dist(i, j)
        layercount += 1
        num += 1
    else:
        for it in range(2 * layercount - 1):
            j += 1
            d[num] = dist(i, j)
            num += 1
        for it in range(2 * layercount):
            i -= 1
            d[num] = dist(i, j)
            num += 1
        for it in range(2 * layercount):
            j -= 1
            d[num] = dist(i, j)
            num += 1
        for it in range(2 * layercount):
            i += 1
            d[num] = dist(i, j)
            num += 1

print(d[368078])




