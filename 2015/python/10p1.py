n = raw_input()


def look_and_see_generator(seq):
    n = seq
    groups = []
    start = 0
    for i in range(1, len(n)):
        if n[i] != n[i-1]:
            groups.append(n[start:i])
            start = i
    groups.append(n[start:])
    ret = ''
    for i in groups:
        ret += str(len(i)) + i[0]
    return ret

for i in range(40):
    n = look_and_see_generator(n)
print len(n)
