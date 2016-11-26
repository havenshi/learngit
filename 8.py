# 8.the median

L=[0,1,4,2,3,4]
L.sort()
if len(L)%2==1:
    print L[len(L)//2]
else:
    print (L[len(L)/2]+L[len(L)/2-1])/2.0