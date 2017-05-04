# method 1 可多次调用，用一个值记录每次状态122211201=1*3^8 + 2*3^7 +...+ 0*3^1 + 1*3^0，转换成对应位置

# method 2 只能调用一次，检查横纵和对角线
def haswon(board):  # 如果是矩阵
    n = len(board)
    for i in range(n):
        if sum(board[i]) == 3*board[i][0]: # check row
            return True
        if sum(board[j][i] for j in range(n)) == 3*board[0][i]: # check column
            return True
    if sum (board[i][i] for i in range(n)) == 3*board[0][0]: # check diagonal
            return True
    return False

def haswon2(board):  # 如果是数组
    n = pow(len(board), 0.5)
    for i in range(n):
        for j in range(n):
            k = i * n + j  # check row
            if board[i] != board[k]:
                break
            if j == n - 1:
                return True
    for i in range(n):
        for j in range(n):
            k = i + j * n  # check colomn
            if board[i] != board[k]:
                break
            if j == n - 1:
                return True
    for i in range(n):  # check diagonal
        k = i + i * n
        if board[0] != board[k]:
            break
        if k == len(board) - 1:
            return True

