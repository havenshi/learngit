# Factor sum of squares
# -*- coding: utf-8 -*-

# N=6
# SUM=0
# for n in range(1,N+1):
#     sum = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             sum+=i**2
#     SUM+=sum
# print SUM
# chaoshi

# s = 0
# for i in range(1,N+1):
# 	s = s + i**2*(N//i)    # step 1
# print (s)

# N = 16
# L1 = list(range(1,N+1))
# L2 = [N//i for i in L1]    # step 2 [16, 8, 5, 4, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1] nums
#                            #        [1**2,2**2.................................16**2]
# print (L1)
# print (L2)

# s = 0
# for i in range(1, N // 2 + 1):
#     s = s + i ** 2 * (N // i)                  # part 1, before N//2
#
# def sumsqr(n):
#     return int(n * (n + 1) * (2 * n + 1) / 6)
#
# s = s + (sumsqr(N) - sumsqr(N // 2))           # part 2, after N//2, 1 for all n**2, thus ΣN**2-Σ(N // 2)**2
#
# print (s)

N=16
def sumsqr(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)

m = int(N ** (1 / 2.0))
s = 0
i = 1
while i <= N ** (1 / 2.0):                        # step 3 L2中的1一直到最后，2到第8项，3到第5项...就是前面的16,8,5。平方根后面的个数是前面的叠加。
    s = s + i ** 2 * (N // i)                     # part 1, before N**0.5, i from 1 to 4, i ** 2 * (N // i)
    if i ** 2 != N:                               # part 2, i from 1 to 3,
        s = s + (sumsqr(N // i) - sumsqr(m))      # 1.sumsqr(16)-sumsqr(4), 即[3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]位置上的N**2各一个
    i = i + 1                                     # 2.sumsqr(8)-sumsqr(4), 即[3, 2, 2, 2]的N**2各一个
                                                  # 3.sumsqr(5)-sumsqr(4), 即[3]的N**2各一个
print (s)
