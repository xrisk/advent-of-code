import sys
f = sys.stdin.read().splitlines()
cnt = 0
for line in f:
    words = line.split()
    if len(set(words)) == len(words):
       cnt += 1
print(cnt)
