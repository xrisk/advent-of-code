import sys
f = sys.stdin.read().splitlines()
cnt = 0

for line in f:
    words = [''.join(sorted(list(x))) for x in line.split()]
    if len(set(words)) == len(words):
        cnt += 1

print(cnt)

