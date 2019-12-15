import string
from random import choices

f = open('sample.txt', 'w')
f.close()
for x in range(1000):
    n = 1000
    res = ''.join(choices(string.ascii_letters +
                          string.digits, k=n))
    f = open('sample.txt', 'a+')
    f.write(str(res))
    f.close()
