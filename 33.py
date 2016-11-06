# Big power operation

def pow_mod(a,n,mod):
    res = 1
    while n > 0 :
        if n % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res
print pow_mod(a,n,20132013)