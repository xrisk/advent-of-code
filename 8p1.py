try:
    c = 0
    while True:
        s = raw_input()
        c += len(s) - len(eval(s))
except EOFError:
    print c
