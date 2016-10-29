#The number of common divisor
a=24
b=60
if a<b:
    smaller=a
else:
    smaller=b

count=0
for i in range(1,smaller+1):
    if a%i==0 and b%i==0:
        count+=1

print count