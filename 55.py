# Back to the longest text string is not simple
# -*- coding: utf-8 -*-

N=2
b=float(N)
a=0.0
i=b
while i > 0:
   a += N/i
   i -= 1
print "%.2f" % a
# 已经有n张卡片，得到下一张与手上不同的卡片的概率是N-n/N，期望是N/(N-n), 1+N/(N-1)+N/(N-2)+.......+N/(1)