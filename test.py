
# -*- coding:utf8 -*-
from itertools import product
from fractions import Fraction
from functools import reduce


# this is for matrix inversion
def invert(matrix):  # 求逆矩阵
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)  # 先把对角线变成1/1
    for i in range(n):  # 如matrix对角线为0，False； ratio = matrix[j][i]/对角线，
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse


# finding sum of a row in matrix
def sumRow(m, r):  # 求矩阵第几行的元素和
    return sum(m[r])


# subtracting two matrices
def substract(matr_a, matr_b):  # 求两个矩阵相减后的矩阵
    output = []
    for i in range(len(matr_a)):
        tmp = []
        for valA, valB in zip(matr_a[i], matr_b[i]):
            tmp.append(valA - valB)
        output.append(tmp[:])
    return output[:]


# matrix multiplication
def matrixmult(matr_a, matr_b):  # 求两个矩阵相乘后的矩阵
    # cols = len(matr_b[0])
    rows = len(matr_b)
    if rows is not 0:
        cols = len(matr_b[0])
    else:
        cols = 0
    resRows = range(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    if cols is not 0:
        return rMatrix
    else:
        return 0
        # return rMatrix


# gcd to find lcm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# lcm to find last value of the output
def lcm(a, n):
    ans = a[0]
    for i in range(1, n):
        ans = (a[i] * ans) // gcd(a[i], ans)
    return ans


# main function
def answer(m):
    num = len(m)
    # if num >= 3: # 如果加上这一段，9failed
    #     for i in range(1, num):
    #         if sum([1 for item in m[i] if item != 0]) == 1:
    #             m[i] = [0] * num

    f = []
    # finding zero rows
    for i in range(0, num):
        j = []
        j.append(sumRow(m, i))
        j.append(i)
        f.append(j)
    k = 0;
    # Fraction Conversion
    for i in range(0, num):
        for j in range(0, num):
            if f[i][0] != 0:
                m[i][j] = Fraction(m[i][j], f[i][0])
    j = []
    for i in range(0, len(f)):
        if f[i][0].numerator == 0:
            j.append(i)
            del m[f[i][1] - k]
            k = k + 1
    q = m
    k = []
    t = 0
    e = m
    # print(m) # 此时m为所有元素化为最简分数的矩阵，且不含全部为0的那些行

    q = []
    for i in range(0, len(m)):
        row = []
        for r in range(0, len(m[0])):
            for t in range(0, len(j)):
                if j[t] is r:
                    row.append(m[i][r])
        q.append(row)
        # print(q), q = [[], [], []]

    t = 0;
    w = 0;
    e = []
    for i in range(0, len(m)):
        row = []
        flag = 1
        for r in range(0, len(m[0])):
            for t in range(0, len(j)):
                if j[t] is r:
                    flag = 0
                    break
            if flag is 1:
                row.append(m[i][r])
        e.append(row)
    # print(e)，e与m差不多，只是如果m[i][j]指向的j行如果全部为0，则不考虑这个m[i][j]

    l = []
    for i in range(0, len(e)):
        k = []
        for b in range(0, len(e)):
            if i == b:
                k.append(1)
            else:
                k.append(0)
        l.append(k)
    # print(l) #单位矩阵
    # print(e) #仍为e

    l = substract(l, e)
    # print(l) # 可能为[]或者行列不相等的矩阵！


    if l == []:
        return 0

    if len(l) != len(l[0]):
        return 0

    l = invert(l)
    r = matrixmult(l, q)
    # print(r)
    if r == 0:
        return 0
    else:
        m = r[0]
    e = []
    for i in range(0, len(m)):
        e.append(m[i].denominator)
    k = lcm(e, len(e))
    e = []
    for i in range(0, len(m)):
        e.append((m[i].numerator * k) // m[i].denominator)
    e.append(k)
    # print(e)
    return e
m =[[0,1],[1,0]]
print answer(m)