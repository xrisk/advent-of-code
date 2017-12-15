import sys, re
reg = re.compile('(\d+)')
a_seed, b_seed = [int(reg.search(i).group()) for i in sys.stdin.readlines()]

mult_a = 16807
mult_b = 48271
MOD = 2147483647

def gen_a():
    a = a_seed
    while True:
        a = (a * mult_a) % MOD
        if a % 4 == 0:
            yield a

def gen_b():
    b = b_seed
    while True:
        b = (b * mult_b) % MOD
        if b % 8 == 0:
            yield b


def solve():
    LIM = int(5 * 1e6)
    a = gen_a()
    b = gen_b()
    cnt = 0
    for i in range(LIM):
        if (next(a) & 0xFFFF) == (next(b) & 0xFFFF):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()

