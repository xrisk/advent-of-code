LEN = 256
line = [int(_.strip()) for _ in input().split(',')]
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

for num in line:
        s, e = cur_pos, (cur_pos + num - 1)
        rev(s, e)
        cur_pos = (cur_pos + num + skip_size) % LEN
        skip_size += 1

print(xs[0] * xs[1])

