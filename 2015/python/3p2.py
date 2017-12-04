try:
    while True:
        s = raw_input()
        xs, ys = 0, 0
        xr, yr = 0, 0
        c = 0
        h = set()
        h.add((0, 0))
        for i in s:
            if c % 2 == 0:
                if i == ">":
                    xs += 1
                elif i == "^":
                    ys += 1
                elif i == "<":
                    xs -= 1
                else:
                    ys -= 1
                h.add((xs, ys))
            else:
                if i == ">":
                    xr += 1
                elif i == "^":
                    yr += 1
                elif i == "<":
                    xr -= 1
                else:
                    yr -= 1
                h.add((xr, yr))
            c += 1
except EOFError, e:
    print len(h)
