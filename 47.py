# Yang hui triangle

n=6
l0 = [1]
l1 = [1,1]
print " ".join([str(x) for x in l0])
print " ".join([str(x) for x in l1])
for i in range(2, n):
    lnew = [1]
    for j in range(1, len(l1)):
        lnew.append(l1[j-1]+l1[j])
    lnew.append(1)
    l1 = lnew
    print " ".join([str(x) for x in lnew])
