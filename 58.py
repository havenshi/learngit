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

