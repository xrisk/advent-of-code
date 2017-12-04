try:
    c = 0
    while True:
        s = raw_input()
        n = '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
        c += len(n) - len(s)
except EOFError:
    print c
