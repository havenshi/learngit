def bunny(n):
    matrix = [[0 for j in range(n+1)] for i in range(n/2+1)]
    matrix[1][1] = 1
    for i in range(n/2+1):
        for j in range(i+1, n+1):
            if i == 1 or i == 2:
                matrix[i][j] = 1
            matrix[i][j] = matrix[i][j - i] + (matrix[i - 1][j - 1] - find1(j - 1, i - 1))  # dp[n][k] = dp[n - k][k] + (dp[n - 1][k - 1] - find1[n - 1][k - 1])
    print matrix
    return sum([matrix[i][n] for i in range(2, n/2+1) if matrix[i][n] > 0])

def find1(n,k):
    if n == 0 or n == 1 and k >= 2 or n == 2 and k == 2:
        return 0
    if n == 1 and k == 1 or n > 2 and k == 2:
        return 1
    if k <= 1:
        return 0
    if k == 3:
        return (n-2-1)/2
    result = 0
    start = 2
    while start + (k-3) < (n - 1 - (start+start+(k-3))*(k-2)/2):
        result += ((n - 1 - (start+start+(k-3))*(k-2)/2) - (start + (k-3)) + 1)/2
        start += 1
    return result


print bunny(9)
