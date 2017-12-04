t = [[0] * 1000 for _ in range(1000)]


def update_util(x1, y1, x2, y2, f):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            t[i][j] = f(t[i][j])


try:
    while True:
        q = raw_input().split()
        if q[0] == 'toggle':
            x1, y1 = map(int, q[1].split(','))
            x2, y2 = map(int, q[3].split(','))
        else:
            x1, y1 = map(int, q[2].split(','))
            x2, y2 = map(int, q[4].split(','))
        if 'on' in q:
            update_util(x1, y1, x2, y2, lambda x: x + 1)
        elif 'off' in q:
            update_util(x1, y1, x2, y2, lambda x: max(0, x - 1))
        else:
            update_util(x1, y1, x2, y2, lambda x: x + 2)

except EOFError:
    c = 0
    for i in range(1000):
        for j in range(1000):
            c += t[i][j]
    print c
