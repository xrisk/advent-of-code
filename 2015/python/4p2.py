import hashlib
for i in xrange(1, 100000000000000000):
    if i % 100000 == 0:
        print i
    if hashlib.md5('ckczppom' + str(i)).hexdigest().startswith('0' * 6):
        print i
        break
