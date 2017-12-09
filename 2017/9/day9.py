import sys

line = sys.stdin.read()
score = 0
depth = 0

in_garbage = False
to_skip = False

for char in line:

    if to_skip:
        to_skip = False
        continue

    if in_garbage:
        if char == '!':
            to_skip = True
        if char == '>':
            in_garbage = False
    else:
        if char == '<':
            in_garbage = True
        elif char == '{':
            depth += 1
            score += depth
        elif char == '}':
            depth -= 1


print(score)
