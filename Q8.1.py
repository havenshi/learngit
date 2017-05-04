#  -*- coding:utf8 -*-
def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    if n == 1 or n ==2:
        return 1
    a, b = 1, 1
    for i in range(3, n+1):
        tmp = a + b
        a = b
        b = tmp
    return b

def fib3(n):  # 运用[[1,1],[1,0]]矩阵
    if n == 1 or n == 2:
        return 1
    matrix = [[1,1],[1,0]]
    n = n - 2 # 矩阵需要相乘n-2次
    # 使用nlog(n)的方法
    res = [[1, 0], [1, 1]] # 注意初始res为对角线为1的矩阵，能保证res*matrix=matrix
    while n > 0:
        if n % 2 != 0:
            a = res[0][0] * matrix[0][0] + res[0][1] * matrix[1][0]
            b = res[0][0] * matrix[0][1] + res[0][1] * matrix[1][1]
            c = res[1][0] * matrix[0][0] + res[1][1] * matrix[1][0]
            d = res[1][0] * matrix[0][1] + res[1][1] * matrix[1][1]
            res = [[a, b], [c, d]]
        n /= 2
        a = matrix[0][0] * matrix[0][0] + matrix[0][1] * matrix[1][0]
        b = matrix[0][0] * matrix[0][1] + matrix[0][1] * matrix[1][1]
        c = matrix[1][0] * matrix[0][0] + matrix[1][1] * matrix[1][0]
        d = matrix[1][0] * matrix[0][1] + matrix[1][1] * matrix[1][1]
        matrix = [[a, b], [c, d]]
    return res[0][0] * 1 + res[0][1] * 1
print fib3(6)