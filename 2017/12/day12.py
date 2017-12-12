import sys
from collections import defaultdict

visited = set([])
adj = defaultdict(list)
cnt = 0

def dfs(x):
    global cnt
    if x not in visited:
        cnt += 1
        visited.add(x)
        for r in adj[x]:
                dfs(r)

for line in sys.stdin.readlines():
    l, r = line.split('<->')
    l = int(l)
    for x in r.split(', '):
        adj[l].append(int(x))

dfs(0)
print(cnt)
