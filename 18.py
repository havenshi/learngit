# The inverse solution of greatest common divisor and least common multiple
# x/a=m,y/a=n
# b/x=n,b/y=m
# m*n=b/a
# therefore, x*y==a*b

a=1200
b=120

if a<b:
    a,b=b,a

newx=b
newy=a
# x is divisor of a and multiple of b
for x in range(b,a+1):
    if x%b==0 and a%x==0:
        y=a*b/x
        if x+y<newx+newy:
            newx,newy=x,y

print newx,newy
