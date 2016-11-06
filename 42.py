# Splitting the prime Numbers sum

n=10

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(2,n):
    if isPrime(i) and isPrime(n-i):
        count += 1
print count/2