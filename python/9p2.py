import itertools

n = 8
d = [[0] * n for _ in range(n)]
for i in range((n-1) * (n) / 2):
    u, v, w = map(int, raw_input().split())
    d[u][v] = w
    d[v][u] = w

best_so_far = -1
for i in itertools.permutations(range(n)):
    current = 0
    for j in range(1, n):
        current += d[i[j-1]][i[j]]
    best_so_far = max(best_so_far, current)

print best_so_far
