i = input()
print(sum(int(y) for x, y in enumerate(i) if i[(x + 1) % len(i)] == y))
print(sum(int(y) for x, y in enumerate(i) if i[(x + len(i) // 2) % len(i)] == y))
