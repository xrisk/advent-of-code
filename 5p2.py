import itertools
import string
counter = 0
while True:
    s = raw_input()
    two = map(lambda x: ''.join(x),
              itertools.product(string.ascii_lowercase, repeat=2))
    try:
        for i in two:
            if s.count(i) >= 2:
                for i in range(0, len(s) - 2):
                    if s[i] == s[i+2]:
                        counter += 1
                        raise Exception
    except Exception:
        print counter
