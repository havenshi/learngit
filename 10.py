# 10.lowest common multiple (lcm)
a=10
b=24
def fun(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            n=i
            break
    return n
print (fun(a,b))