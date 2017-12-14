import day10_part2
import sys

if sys.version_info.major >= 3:
    key = input()
else:
    key = raw_input()

cnt = 0

for i in range(128):
    hsh = day10_part2.get_hash('{}-{}'.format(key, i))
    cnt += hsh.count('1')

print(cnt)
