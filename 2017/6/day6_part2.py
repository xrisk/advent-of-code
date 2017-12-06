blocks = [int(x) for x in input().split()]

look = {}
look[tuple(blocks)] = 0

cnt = 0
while True:

    max_val = -1111111
    max_pos = -1

    for i, j in enumerate(blocks):
        if j > max_val:
            max_val = j
            max_pos = i

    blocks[max_pos] = 0

    while max_val != 0:
        max_pos = (max_pos + 1) % len(blocks)
        blocks[max_pos] += 1
        max_val -=1

    cnt += 1

    if tuple(blocks) in look:
        print(cnt - look[tuple(blocks)])
        break
    else:
        look[tuple(blocks)] = cnt




