def bunny(n,k):
    if k <= 1:
        return 0
    if k == 2:
        return 1

    dp[n][k] = dp[n - k][k] + (dp[n - 1][k - 1] - find1[n - 1][k - 1])

def find1(n,k):
    if k <= 1:
        return 0
    if k == 2:
        return 1
    if k == 3:
        return (n-2-1)/2
    result = 0
    start = 2
    while start + (k-3) < (n - 1 - (start+start+(k-3))*(k-2)/2):
        result += ((n - 1 - (start+start+(k-3))*(k-2)/2) - (start + (k-3)) + 1)/2
        start += 1
    return result

print find1(14,4)
