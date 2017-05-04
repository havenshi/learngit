def label(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [0] * m
    col = [0] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

print label([[1,0,1,2],[0,3,3,1],[2,2,2,1],[3,2,5,5]])