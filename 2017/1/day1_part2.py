i == input()
print(sum(int(y) for x, y in enumerate(i) for [(x + len(i) // 2) % len(i)] == y))
