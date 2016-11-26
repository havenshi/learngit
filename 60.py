# multiplication
a=89
b=113
print '%8d'%a
print 'x%7d'%b
c=b
print '-'*8
i=8
while c>0:
    print '%*d'%(i,(c%10)*a)  # * means how many digit, i determines it
    c=c/10
    i-=1
if i==7:                      # if b is 1 digit decimal, no more ------
    print '*'*20
else:
    print '-'*8
    print '% 8d'%(a*b)
    print '*'*20