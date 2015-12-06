counter = 0
while True:
    s = raw_input()
    try:
        import string
        v = 'aeiou'
        samecombos = map(lambda x: x * 2, string.ascii_lowercase)
        twocombos = ["ab", "cd", "pq", "xy"]
        assert sum(map(s.count, v)) >= 3
        assert sum(map(s.count, samecombos)) >= 1
        assert sum(map(s.count, twocombos)) == 0
        counter += 1
        print counter
    except AssertionError, e:
        pass
