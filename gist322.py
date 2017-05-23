# -*- coding:utf8 -*-

def answer(m):
    n = len(m)
    if n == 1:
        return [0]
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
    # 求伴随矩阵，注意先删j行，再删i列
    for i in range(length):
        for j in range(length):
            copy = IminusQ[:j]+IminusQ[j+1:]
            for x in range(len(copy)):
                copy[x] = copy[x][:i]+copy[x][i+1:]
            F[i][j] = [MatrixGetDet(copy) * pow(-1,i+j), denominator] # 不用除以A，保证全部是整数。F=[[[18, 14], [9, 14]], [[8, 14], [18, 14]]]
    if len(F) == 1:
        F = [[1]]

    # 第二步求FR
    R = [[0 for j in range(gap+1)] for i in range(length)]
    for i in range(length):
        for j in range(gap+1):
            row = newl[gap + 1 + i]
            col = newl[j]
            R[i][j] = [m[row][col], sum(m[row])] # 2.R = [[[0, 2], [0, 2], [0, 2], [1, 2]], [[0, 9], [3, 9], [2, 9], [0, 9]]]
    if F == [[1]]:
        new = [R[0][i][0] for i in range(len(R[0]))]
        return new+[sum(new)]


    F = F[0]
    for i in range(len(F)):
        tmp = hcf(F[i][0], F[i][1])
        F[i] = [F[i][0] / tmp, F[i][1] / tmp]  # 1.F = [[9, 7], [9, 14]]
    FR = [0 for i in range(gap + 1)]
    for j in range(gap + 1):
        FR[j] = multiply(F[0], R[0][j])
        for i in range(1, length):
            tmp = multiply(F[i], R[i][j])
            if tmp[0] == 0:
                continue
            FR[j] = add(FR[j], tmp)  # FR=[[0, 0], [3, 14], [1, 7], [9, 14]]
    common = reduce((lambda x, y: lcm(x, y)),
                    [FR[i][1] for i in range(len(FR)) if FR[i][0] != 0])  # common = 14
    new = []
    for i in range(len(FR)):
        if FR[i][0] == 0:
            new.append(0)
        else:
            new.append(FR[i][0] * (common / FR[i][1]))
    return new + [sum(new)]


def add(x, y):
    if x[0] == 0 and y[0] == y:
        return [0, 0]
    if x[0] == 0:
        return y
    if y[0] == 0:
        return x
    den = lcm(x[1], y[1])
    num = x[0] * (den / x[1]) + y[0] * (den / y[1])
    tmp = hcf(num, den)
    return [num / tmp, den / tmp]

def multiply(x, y):
    if x[0] == 0 or y[0] == 0:
        return [0, 0]
    den = x[1] * y[1]
    num = x[0] * y[0]
    tmp = hcf(num, den)
    return [num / tmp, den / tmp]

# 最大公约数
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# 最小公倍数
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    lcm = x*y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

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
