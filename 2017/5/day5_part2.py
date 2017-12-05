import sys
lines = [int(x) for x in sys.stdin.read().splitlines()]
index = 0
cnt = 0
while True:
    jmp = lines[index]
    if lines[index] >= 3:
        lines[index] -= 1
    else:
        lines[index] += 1
    index += jmp
    cnt += 1
    if index < 0 or index >= len(lines):
        print(cnt)
        break
