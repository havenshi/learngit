# -*- coding:utf8 -*-
from fractions import Fraction
from itertools import product


def matrixmult(matr_a, matr_b):
    rows = len(matr_b)
    if rows != 0:
        cols = len(matr_b[0])
    else:
        cols = 0
    rMatrix = [0] * cols
    for j, k in product(range(cols), range(rows)):
        rMatrix[j] += matr_a[k] * matr_b[k][j]
    if cols != 0:
        return rMatrix
    else:
        return [0]

# 最大公约数
def hcf(a, b):
    if a == 0 or b == 0:
        return 1
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def lcm(a, b):
    return a * b / hcf(a, b)

# 求行列式的值
def MatrixGetDet(M):
    length = len(M)
    if length == 1:
        return M[0][0]
    if length == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    import itertools
    # sum positive
    positive = 0
    indexer1 = itertools.cycle(range(length))
    indexer2 = itertools.cycle(range(length))
    for index in range(length):
        indexer1.next()
        _tmp = 1
        for index in range(length):
            index1 = indexer1.next()
            index2 = indexer2.next()
            _tmp *= M[index1][index2]
        positive += _tmp
    # sum negative
    negative = 0
    indexer1 = itertools.cycle(range(length))
    indexer2 = itertools.cycle(range(length)[::-1])
    for index in range(length):
        indexer1.next()
        _tmp = 1
        for index in range(length):
            index1 = indexer1.next()
            index2 = indexer2.next()
            _tmp *= M[index1][index2]
        negative += _tmp
    # return
    return positive - negative

def answer(m):
    n = len(m)
    if n == 1 and m != [[0]]:
        return [0]
    if n == 1 and m == [[0]]:
        return [1]

    newl = []
    for i in range(n):
        if list(set(m[i])) == [0]:
            newl.append(i)
    gap = len(newl)-1 # gap都是absorbing matrix, 对角线都为1. gap = 3
    for i in range(n):
        if i not in newl:
            newl.append(i) # newl = [2, 3, 4, 5, 0, 1]

    # 构造一个new matrix, 横纵坐标为[2, 3, 4, 5, 0, 1]，分为I块,O块，R和Q块一共四块
    matrix = [[0 for j in range(n)] for i in range(n)]
    # 第一步求F = (I-Q)^-1

    # Q
    length = n-(gap+1)
    Q = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            row = newl[gap+1+i]
            col = newl[gap+1+j]
            Q[i][j] = Fraction(m[row][col],sum(m[row]))
    # I
    I = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            if i == j:
                I[i][j] = 1
            else:
                I[i][j] = 0

    # I-Q
    IminusQ = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            IminusQ[i][j] = I[i][j] - Q[i][j]
    # 求(I-Q)的逆矩阵F
    A = MatrixGetDet(IminusQ)
    F = [[0 for j in range(length)] for i in range(length)]
    # 求伴随矩阵，注意先删j行，再删i列
    if len(IminusQ) == 1:
        F = [[1]]
    else:
        for i in range(length):
            for j in range(length):
                copy = IminusQ[:j]+IminusQ[j+1:]
                for x in range(len(copy)):
                    copy[x] = copy[x][:i]+copy[x][i+1:]
                F[i][j] = Fraction(MatrixGetDet(copy) * pow(-1,i+j), A)
    # 第二步求FR
    R = [[0 for j in range(gap+1)] for i in range(length)]
    for i in range(length):
        for j in range(gap+1):
            row = newl[gap + 1 + i]
            col = newl[j]
            R[i][j] = Fraction(m[row][col], sum(m[row]))
    F = F[0]
    FR = matrixmult(F,R)
    if FR == []:
        return [0]
    new = []
    # 提取分数分母的最小公倍数
    common = FR[0].denominator
    for i in range(1, len(FR)):
        common = lcm(common, FR[i].denominator)
    for i in range(len(FR)):
        new.append(FR[i].numerator * common / FR[i].denominator)
    return new + [sum(new)]


m= [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print answer(m)
m1 =  [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print answer(m1)
m1 =  [[0, 1, 2], [0, 0, 0], [0, 0, 0]]
print answer(m1)
m1 =  [[0, 1], [0, 0]]
print answer(m1)
m1 =  [[0]]
print answer(m1)
