def cent(n):
    cents = [1, 5, 10, 25]
    coinway = [0] * (n + 1)
    coinway[0] = 1
    for coin in cents:
        for i in range(1, n + 1):
            if i >= coin:
                coinway[i] += coinway[i - coin]
    return coinway[n]
print cent(10)
