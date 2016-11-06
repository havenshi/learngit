# Weight problems
w=[1,3]
n=[2,1]
W = [0]
L = [0]
for i,v in enumerate(n):
    for j in range(v+1):
        L.append(j * w[i])
    W = list(set([x+y for x in W for y in L]))
    print L
    print W
    L=[0]
print len(list(set(W)))
