# -*- coding:utf8 -*-
import numpy
def answer(m):
    n = len(m)
    oldl = [i for i in range(n)]
    newl = []
    for i in range(n):
        if list(set(m[i])) == [0]:
            newl.append(i)
    gap = len(newl)-1 # gap都是absorbing matrix, 对角线都为1. gap = 3
    for i in range(n):
        if i not in newl:
            newl.append(i)
    # 构造一个new matrix, 横纵坐标为[2, 3, 4, 5, 0, 1]
    matrix = [[0 for j in range(n)] for i in range(n)]
    # I块,O块，R和Q块
    # 求F = (I-Q)^-1
    # Q
    length = n-(gap+1)
    Q = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            row = newl[gap+1+i]
            col = newl[gap+1+j]
            Q[i][j] = [m[row][col],sum(m[row])]# Q = [[[0, 2], [1, 2]], [[4, 9], [0, 9]]]
    # I
    I = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            tmp = Q[i][0][1]
            if i == j:
                I[i][j] = [tmp, tmp]
            else:
                I[i][j] = [0,tmp] # I = [[[2, 2], [0, 2]], [[0, 9], [9, 9]]]
    # I-Q
    IminusQ = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            IminusQ[i][j] = [I[i][j][0] - Q[i][j][0],I[i][j][1]] # IminusQ = [[[2, 2], [-1, 2]], [[-4, 9], [9, 9]]]
    # 求(I-Q)的逆矩阵F
    # 先转成整数，记录最小公倍数lcmvalue。再求逆矩阵，记录行列式的值A
    lcmvalue = IminusQ[0][0][1]
    for i in range(1, length):
        lcmvalue = lcm(lcmvalue, IminusQ[i][0][1]) # lcmvalue = 18
    for i in range(length):
        for j in range(length):
            IminusQ[i][j] = IminusQ[i][j][0] * (lcmvalue / IminusQ[i][j][1]) # IminusQ = [[18, -9], [-8, 18]]
    A = MatrixGetDet(IminusQ) # A = 252
    denominator = A / lcmvalue # 14
    F = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            copy = IminusQ[:]
            copy = numpy.delete(copy, (j), axis=0)  # 注意先删j行，再删i列
            copy = numpy.delete(copy, (i), axis=1)
            F[i][j] = [MatrixGetDet(copy) * pow(-1,i+j), denominator] # 不用除以A，保证全部是整数。F=[[[18, 14], [9, 14]], [[8, 14], [18, 14]]]
    # 求FR
    R = [[0 for j in range(gap+1)] for i in range(length)]
    for i in range(length):
        for j in range(gap+1):
            row = newl[gap + 1 + i]
            col = newl[j]
            R[i][j] = [m[row][col], sum(m[row])] # R = [[[0, 2], [0, 2], [0, 2], [1, 2]], [[0, 9], [3, 9], [2, 9], [0, 9]]]
    # R的分母转化为相同值
    lcmvalue = R[0][0][1]
    for i in range(1, length):
        lcmvalue = lcm(lcmvalue, R[i][0][1])  # lcmvalue = 18
    for i in range(length):
        for j in range(gap+1):
            R[i][j] = [R[i][j][0] * (lcmvalue / R[i][j][1]), lcmvalue] # R = [[[0, 18], [0, 18], [0, 18], [9, 18]], [[0, 18], [6, 18], [4, 18], [0, 18]]]
    FR = [0 for i in range(gap+1)]
    for i in range(gap+1):
        FR[i] = F[0][0][0] * R[0][i][0]
        for j in range(1, length):
            FR[i] += F[0][j][0] * R[j][i][0] # FR = [0, 54, 36, 162]
    FR += [sum(FR)] # [0, 54, 36, 162, 252]
    res = FR[-1]
    for i in range(len(FR)-1,-1,-1):
        if FR[i] != 0:
            res = hcf(res,FR[i])
    for i in range(len(FR)):
        FR[i] /= res
    return FR

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

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

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


m= [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print answer(m)
m1 =  [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print answer(m1)
