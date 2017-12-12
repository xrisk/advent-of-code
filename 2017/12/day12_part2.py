import sys
from collections import defaultdict

visited = set([])
adj = defaultdict(list)
cnt = 0

def dfs(x):
    if x not in visited:
        visited.add(x)
        for r in adj[x]:
                dfs(r)

for line in sys.stdin.readlines():
    l, r = line.split('<->')
    l = int(l)
    for x in r.split(', '):
        adj[l].append(int(x))

for i in range(max(adj.keys())):
    if i not in visited:
        cnt += 1
        dfs(i)

print(cnt)
