def get_hash(line):
    LEN = 256
    line = [ord(ch) for ch in line]
    line += [17, 31, 73, 47, 23]
    xs = [i for i in range(LEN)]

    cur_pos = 0
    skip_size = 0

    for _ in range(64):
        for num in line:
                s, e = cur_pos, (cur_pos + num - 1)
                s %= LEN
                e %= LEN
                if e >= s:
                    xs[s: e + 1] = reversed(xs[s: e + 1])
                else:
                    tmp = xs[s:] + xs[:e+1]
                    tmp.reverse()
                    l1 = len(xs[s:])
                    xs[s:] = tmp[:l1]
                    xs[:e+1] = tmp[l1:]
                cur_pos = (cur_pos + num + skip_size) % LEN
                skip_size += 1

    hsh = ''
    for i in range(16):
        x = 0
        for j in range(i * 16, (i + 1) * 16):
            x ^= xs[j]
        hsh += "{:08b}".format(x)

    return hsh
