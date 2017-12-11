line = input().split(',')

x = 0
y = 0

def dist(x, y):
    x, y = abs(x), abs(y)
    return int(x / 2 + y)

def move(d):
    global x, y
    if d == 'n':
        y += 1
    elif d == 'ne':
        x, y = x + 1, y + 1/2
    elif d == 'se':
        x, y = x + 1, y - 1/2
    elif d == 's':
        y -= 1
    elif d == 'sw':
        x, y = x - 1, y - 1/2
    elif d == 'nw':
        x, y = x - 1, y + 1/2
    return dist(x, y)


print(max(move(d) for d in line))


