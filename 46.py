# Take stones game
# (1, 2) (3, 5) (4, 7) (6, 10) (8, 13) (9, 15) (11, 18) (12, 20) (14, 23) (16, 26) (17, 28) (19, 31)...
# a/b = (sqrt(5) - 1)/2 = 0.618

a=8
b=13
if a > b:
    a, b = b, a
k = b - a
c = k * 1.6180339887498949
if int(c) == a:
    print 'Loose'
else:
    print 'Win'