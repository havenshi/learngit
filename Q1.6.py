def rotate(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(i+1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    for i in range(m/2):
        for j in range(n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[m-1-i][j]
            matrix[m - 1 - i][j] = tmp
    return matrix

print rotate([[1,2,3],[4,5,6],[7,8,9]])