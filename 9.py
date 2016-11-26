# 9.greatest common divisor(gcd)
a=10
b=24
def fun(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            n=i
    return n
print (fun(a,b))