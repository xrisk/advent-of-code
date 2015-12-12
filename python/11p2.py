import string


def increasing_seq(n):
    for i in range(1, len(n) - 1):
        if n[i - 1] + 1 == n[i] and n[i] + 1 == n[i + 1]:
            return True
    return False


def no_banned_letters(n):
    banned = set(map(lambda x: ord(x), "iol"))
    string_has = set(n)
    return len(banned.intersection(string_has)) == 0


def repeating(n):
    c = 0
    s = ''.join(map(lambda x: chr(x + ord('a')), n))
    for i in string.ascii_lowercase:
        c += s.count(i * 2)
    return c >= 2


def password_is_okay(s):
    return increasing_seq(s) and no_banned_letters(s) and repeating(s)

s = map(lambda x: ord(x) - ord('a'), raw_input())
s[-1] += 1
while not password_is_okay(s):
    s[-1] += 1
    for i in range(len(s) - 1, 0, -1):
        if s[i] >= 26:
            s[i-1] += (s[i] / 26)
            s[i] %= 26
    if s[0] >= 26:
        s.insert(0, s[0] / 26)
        s[1] %= 26

print ''.join(map(lambda x: chr(x + ord('a')), s))
