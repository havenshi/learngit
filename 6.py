# 6.To solve all the prime Numbers within 100

primes = []
for i in range(2, 101):
    for t in range(2, i):
        if i % t == 0:
            break
    else:
        primes.append(i)
print primes
print ' '.join(map(str, primes))

