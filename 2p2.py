try:
    c = 0
    while True:
        s = map(int, raw_input().split('x'))
        s.sort()
        c += 2 * (s[0] + s[1]) + reduce(lambda x, y: x * y, s)
except EOFError:
    print c
