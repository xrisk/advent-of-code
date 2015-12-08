s = raw_input()
p = 0
for i in range(len(s)):
    if s[i] == '(':
        p += 1
    else:
        p -= 1
    if p == -1:
        print i + 1
        break
