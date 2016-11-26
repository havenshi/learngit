# 3.Reverse a string
a="12345"

# method 1
print(a[::-1])

# method 2
from functools import reduce
print reduce((lambda x, y: y+x), a)   # reduce is [ func(func(s1, s2),s3), ... , sn ]

# method 3
print "".join(reversed(a))     # reversed(object) return a iterator, type 'reversed', join(iterable)