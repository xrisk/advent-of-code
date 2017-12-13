import sys
from collections import OrderedDict, defaultdict

m = {}
config = []

for line in sys.stdin.readlines():
    l, r = map(int, line.split(': '))
    m[l] = r

num_layers = max(m) + 1

for k in range(num_layers):
    config.append(0 if k in m else -1)

def next(config, stroke):
    config = config[::]
    for i, j in enumerate(config):
        if j != -1:
            if stroke[i] == 'up':
                if j + 1 == m[i]:
                    config[i] = j - 1
                    stroke[i] = 'down'
                else:
                    config[i] = j + 1
            else:
                if j == 0:
                    config[i] = j + 1
                    stroke[i] = 'up'
                else:
                    config[i] = j - 1
    return config

def solve(config, stroke):
    penalty = 0
    stroke = stroke.copy()
    for i in range(num_layers):
        if config[i] == 0:
            return False
        config = next(config, stroke)
    return True

n = 0
stroke = defaultdict(lambda: 'up')
while True:
    if solve(config, stroke):
        print(n)
        break
    else:
        config = next(config, stroke)
        n += 1
