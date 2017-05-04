def find(matrix, x):
    morigin, norigin = 0, 0
    m = len(matrix) - 1
    n = len(matrix[0]) - 1
    while morigin <= m and n >= 0:
        if x == matrix[morigin][n]:  # the most right top
            return [morigin, n]
        if x > matrix[morigin][n]:  # delete this row
            morigin += 1
        else:   # delete this column
            n -= 1
    return False

print find([[1,2,3],[2,4,6],[3,6,9]], 9)
