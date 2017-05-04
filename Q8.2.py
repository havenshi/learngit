def robot(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[n-1][n-1]

# print robot(3)

# output is all possible path
def path(matrix):
    result = []
    help(matrix, 0, 0, (len(matrix)-1, len(matrix[0])-1), result, tmp = [(0, 0)])
    return result

def help(matrix, i, j, target, result, tmp):
    if tmp[-1] == target:
        result.append(tmp)
        return
    if i + 1 < len(matrix) and matrix[i+1][j] != 1:
        help(matrix, i+1, j, target, result, tmp + [(i+1, j)])
    if j + 1 < len(matrix) and matrix[i][j+1] != 1:
        help(matrix, i, j+1, target, result, tmp + [(i, j+1)])

print path([[0,0,0],[0,1,0],[0,0,0]])