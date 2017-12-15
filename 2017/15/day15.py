import sys, re
reg = re.compile('(\d+)')
a, b = [int(reg.search(i).group()) for i in sys.stdin.readlines()]

mult_a = 16807
mult_b = 48271
MOD = 2147483647

def cmp(a, b):
    for i in range(16):
        d1, d2 = a % 2, b % 2
        if d1 != d2:
            return False
        a //= 2
        b //= 2
    return True

cnt = 0

# for i in range(int(40 * 1e6)):
LIM = int(40 * 10**6)
for i in range(LIM):
    a = (a * mult_a) % MOD
    b = (b * mult_b) % MOD
    if cmp(a, b):
        cnt += 1

print(cnt)

