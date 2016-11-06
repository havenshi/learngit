# The Fibonacci sequence

a=[1,1]
for i in range(2,n):
    a.append(a[i-2]+a[i-1])
print a[n-1]%20132013