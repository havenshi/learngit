def newton(n):
    approx = 0.5 * n
    for i in range(500):
        better = 0.5 * (approx + n/approx)
        approx = better
    return better
print newton(2)