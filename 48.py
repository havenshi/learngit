# Weight problems 2
w=[2,5,11]
n=9
L=len(w)
s=[-1 for i in range(n+1)]
s[0]=0
print s
for i in range(L):
    for j in range(1,n+1):
        if j-w[i]>=0 and s[j-w[i]]!=-1: # n>=each weight, their difference value should be possible(not -1)
            s[j]=1
    print s
if s[n]!=-1:
    print 'Yes'
else:
    print "No"
print s