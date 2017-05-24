
from itertools import product
from itertools import starmap
from operator import mul
import fractions

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
m = [1]
n = [2,3]
print matrixmult(m,n)