import sys

line = sys.stdin.read()

in_garbage = False
to_skip = False

garbage_cnt = 0

for char in line:

    if to_skip:
        to_skip = False
        continue

    if in_garbage:
        if char == '!':
            to_skip = True
        elif char == '>':
            in_garbage = False
        else:
            garbage_cnt += 1
    else:
        if char == '<':
            in_garbage = True

print(garbage_cnt)
