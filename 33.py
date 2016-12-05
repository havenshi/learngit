# Big power operation

a=9
n=50
def pow_mod(a,n,mod):  # a**50=(a**2)**25, a**25=(a**2)**12*a,
    res = 1
    while n > 0 :
        if n % 2 == 1:  # if n is odd, extract new_a%mod and multiply res
            res = res * a % mod
        a = a * a % mod # 1.a=new_a**2%d
        n >>= 1         # 2.n//2
        print n,a,res   # when n//2, new_a=a**2.then res=old_remain*one_a(as new_remain)
    return res
print pow_mod(a,n,7)
# a**15=a*(a**2)*(a**4)*(a**8)