import hashlib
for i in xrange(1, 100000000000000000):
    if hashlib.md5('ckczppom' + str(i)).hexdigest().startswith('0' * 5):
        print i
        break
