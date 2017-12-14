import day10_part2
import sys

graph = []

visited = set([])

def dfs(i, j):
    if i < 0 or i >= 128 or j < 0 or j >= 128:
        return
    if graph[i][j] == '0':
        return
    if (i, j) in visited:
        return
    visited.add((i, j))
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

def solve():
    cnt = 0
    for i in range(128):
        for j in range(128):
            if graph[i][j] == '1' and (i, j) not in visited:
                cnt += 1
                dfs(i, j)

    print(cnt)

if __name__ == '__main__':
    if sys.version_info.major >= 3:
        key = input()
    else:
        key = raw_input()
    for i in range(128):
        hsh = day10_part2.get_hash('{}-{}'.format(key, i))
        graph.append(hsh)

    solve()




