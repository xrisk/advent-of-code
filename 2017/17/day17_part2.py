import sys

if sys.version_info.major == 3:
    skip = int(input())
else:
    skip = int(raw_input())

list_size = 1
pos = 0
ITER = int(50e6)
sol = None

for i in range(1, ITER + 1):
    pos = (pos + skip) % list_size
    if pos == 0:
        sol = i
    list_size += 1
    pos += 1

print(sol)



