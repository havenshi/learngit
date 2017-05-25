from fractions import Fraction
from copy import deepcopy

Q_size = 0


def hcf(a, b):
    if a == 0 or b == 0:
        return 1
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / hcf(a, b)


def convert_matrix(mat):
    global Q_size
    mat_len = len(mat)
    frac_mat = [[0 for i in range(mat_len)] for j in range(mat_len)]
    for i in range(mat_len):
        sum_line = sum(mat[i])
        if sum_line == 0:
            Q_size = i
            break
        else:
            for j in range(mat_len):
                if mat[i][j]:
                    frac_mat[i][j] = Fraction(mat[i][j], sum_line)
    return frac_mat


def get_Q(mat):
    global Q_size
    Q_mat = []
    for i in range(Q_size):
        Q_mat.append(mat[i][:Q_size])
    return Q_mat


def get_I(mat):
    global Q_size
    I_mat = [[0 for i in range(Q_size)] for j in range(Q_size)]
    for i in range(Q_size):
        I_mat[i][i] = 1
    return I_mat


def get_R(mat):
    global Q_size
    R_mat = []
    for i in range(Q_size):
        R_mat.append(mat[i][Q_size:])
    return R_mat


def get_I_minus_Q(mat):
    global Q_size
    mat_b = [[0 for i in range(Q_size)] for j in range(Q_size)]
    for i in range(Q_size):
        mat_b[i][i] = 1

    for i in range(Q_size):
        for j in range(Q_size):
            mat[i][j] = mat_b[i][j] - mat[i][j]

    return mat


def inverse_IQ(mat):
    global Q_size
    for i in range(Q_size):
        if mat[i][i] != 1:
            numerator = 1 / mat[i][i]
            for j in range(Q_size * 2):
                mat[i][j] = mat[i][j] * numerator
        for k in range(i + 1, Q_size):
            if mat[k][i] != 0:
                multiper_num = -mat[k][i]
                for j in range(Q_size * 2):
                    mat[k][j] = mat[i][j] * multiper_num + mat[k][j]
    for i in range(Q_size - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            if mat[k][i] != 0:
                multiper_num = -mat[k][i]
                for j in range(Q_size * 2):
                    mat[k][j] = mat[i][j] * multiper_num + mat[k][j]
    F_mat = []
    for i in range(Q_size):
        F_mat.append(mat[i][Q_size:])
    return F_mat


def get_F_R(F_mat, R_mat):
    if R_mat == []:
        return [0]
    F_R_mat = [0 for i in range(len(R_mat[0]))]
    for i in range(len(R_mat[0])):
        for j in range(len(F_mat[0])):
            F_R_mat[i] += F_mat[0][j] * R_mat[j][i]
    return F_R_mat


def answer(m):
    n = len(m)
    if n == 1 and m != [[0]]:
        return [0, 0]
    if n == 1 and m == [[0]]:
        return [1, 1]
    if n == 0:
        return [0, 0]
    for i in range(len(m)):
        sum_line = sum(m[i])
        if sum_line == 0:
            break
        if i == len(m) - 1:
            return [0, 0]
    flag = False
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != 0:
                if sum(m[j]) == 0:
                    flag = True
            if flag:
                break
    if flag is False:
        return [0, 0]
    check_list = [0]
    visited = []
    while check_list:
        current = check_list.pop()
        visited.append(current)
        for i in range(len(m)):
            if m[current][i] != 0 and i not in visited:
                check_list.append(i)
    flag = False
    for i in visited:
        if sum(m[i]) == 0:
            flag = True
    if flag is False:
        return [0, 0]

    frac_mat = convert_matrix(m)

    Q_mat = get_Q(frac_mat)

    I_mat = get_I(frac_mat)

    I_minus_Q = get_I_minus_Q(Q_mat)

    for i in range(Q_size):
        I_minus_Q[i].extend(I_mat[i])

    F_mat = inverse_IQ(I_minus_Q)

    R_mat = get_R(frac_mat)

    F_R_result = get_F_R(F_mat, R_mat)
    new = []
    common = F_R_result[0].denominator
    for i in range(1, len(F_R_result)):
        common = lcm(common, F_R_result[i].denominator)
    for i in range(len(F_R_result)):
        new.append(F_R_result[i].numerator * common / F_R_result[i].denominator)
    return new + [sum(new)]
test1 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
test2 = [[0,1],[0,0]]
test3 = [[0,1,0], [1,0,0], [0,0,0]]
test4 = [[0,1,1,0,0], [1,0,0,0,0], [0,1,0,0,0], [0,0,0,0,1],[0,0,0,0,0]]
print answer(test1)