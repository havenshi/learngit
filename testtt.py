from __future__ import division
from itertools import compress
from itertools import starmap
from operator import mul
import fractions


def convertMatrix(transMatrix):
    probMatrix = []
    for i in range(len(transMatrix)):
        row = transMatrix[i]
        newRow = []
        rowSum = sum(transMatrix[i])
        if all([v == 0 for v in transMatrix[i]]):
            for j in transMatrix[i]:
                newRow.append(0)
            newRow[i] = 1
            probMatrix.append(newRow)
        else:
            for j in transMatrix[i]:
                if j == 0:
                    newRow.append(0)
                else:
                    newRow.append(j / rowSum)
            probMatrix.append(newRow)
    return probMatrix


def answer(m):
    # convert matrix numbers into probabilities
    probMatrix = convertMatrix(m)

    # find terminal states
    terminalStateFilter = []
    for row in range(len(m)):
        if all(x == 0 for x in m[row]):
            terminalStateFilter.append(True)
        else:
            terminalStateFilter.append(False)

    # multiply matrix by probability vector
    oldFirstRow = probMatrix[0]
    probVector = None
    for i in range(3000):
        probVector = [sum(starmap(mul, zip(oldFirstRow, col))) for col in zip(*probMatrix)]
        oldFirstRow = probVector

    # generate numerators
    numerators = []
    for i in probVector:
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)

    # generate denominators
    denominators = []
    for i in probVector:
        denominator = fractions.Fraction(i).limit_denominator().denominator
        denominators.append(denominator)

    # calculate factors to multiply numerators by
    factors = [max(denominators) / x for x in denominators]
    # multiply numerators by factors
    numeratorsTimesFactors = [a * b for a, b in zip(numerators, factors)]
    # filter numerators by terminal state booleans
    terminalStateNumerators = list(compress(numeratorsTimesFactors, terminalStateFilter))

    # append numerators and denominator to answer
    answerlist = []
    for i in terminalStateNumerators:
        answerlist.append(i)
    answerlist.append(max(denominators))

    return list(map(int, answerlist))


print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))



# 一稿，超时
def answer(m):
    n = len(m)
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

    # 第二步求FR
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


# 二稿，40行lcmvalue = IminusQ[0][0][1]IndexError

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
    # 求伴随矩阵，注意先删j行，再删i列
    for i in range(length):
        for j in range(length):
            copy = IminusQ[:j]+IminusQ[j+1:]
            for x in range(len(copy)):
                copy[x] = copy[x][:i]+copy[x][i+1:]
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
            FR[i] += F[0][j][0] * R[j][i][0]  # FR = [0, 54, 36, 162]
        FR[i] /= max(F[0][0][1], F[0][0][1])
    FR += [sum(FR)] # [0, 54, 36, 162, 252]
    return FR

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
    lcm = x*y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
