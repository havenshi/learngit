# The least common multiple I

L=[2,8,3,50]
s=sorted(L)
min=s[-1]
max=s[0]
for i in range(1,len(s)):
    max=max*s[i]

lcm=min
for m in range(max,min,-1):
    for i in range(len(s)):
        if m%s[i]==0 and i!=len(s)-1:
            i+=1
        elif m%s[i]==0 and i==len(s)-1:
            lcm=m
        else:
            break
print lcm


def lcm(a, b):
    if a < b:
        a = a ^ b;
        b = a ^ b;
        a = a ^ b
    x = a;
    y = b
    while (y != 0):
        t = y
        y = x % y
        x = t
    return (a * b / x)


def xxoo(L1, last):
    if len(L1) == 1:
        return lcm(L1[0], last)
    return lcm(xxoo(L1[0:-1], L1[-1]), last)


print xxoo(L[0:-1], L[-1])