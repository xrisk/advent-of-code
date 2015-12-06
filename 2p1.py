try:
    c = 0
    while True:
        l, w, h = map(int, raw_input().split('x'))
        areas = [l * w, w * h, h * l]
        c += 2 * sum(areas) + min(areas)
except EOFError:
    print c
