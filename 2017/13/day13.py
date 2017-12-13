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
            penalty += i * m[i]
        config = next(config, stroke)
    return penalty

print(solve(config, defaultdict(lambda: 'up')))
