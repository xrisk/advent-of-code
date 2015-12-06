try:
    while True:
        s = raw_input()
        x, y = 0, 0
        h = set()
        h.add((x, y))
        for i in s:
            if i == ">":
                x += 1
            elif i == "^":
                y += 1
            elif i == "<":
                x -= 1
            else:
                y -= 1
            h.add((x, y))
except EOFError, e:
    print len(h)
