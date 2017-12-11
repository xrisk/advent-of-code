LEN = 256
line = [ord(ch) for ch in input().strip()]
line += [17, 31, 73, 47, 23]
xs = [i for i in range(LEN)]

cur_pos = 0
skip_size = 0

def _get(x):
    return xs[x % LEN]

def _set(x, k):
    xs[x % LEN] = k


def rev(a, b):
    while b > a:
        t = _get(b)
        _set(b, _get(a))
        _set(a, t)
        a += 1
        b -= 1

for _ in range(64):
    for num in line:
            s, e = cur_pos, (cur_pos + num - 1)
            rev(s, e)
            cur_pos = (cur_pos + num + skip_size) % LEN
            skip_size += 1

sparse = []
hsh = []
for i in range(16):
    x = 0
    for j in range(i * 16, (i + 1) * 16):
        x ^= xs[j]
    sparse.append(x)
    hsh.append("{:02x}".format(x))

print("".join(hsh))

