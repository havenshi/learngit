def queen(n):
    result = []
    for i in range(1, 1 + n):
        help(i, n, result, tmp = [])
    return result

def help(x, target, result, tmp):
    tmp += [x]
    if len(tmp) == target:
        result += [tmp]
        return
    xx = range(1, x-1) + range(x+2, target+1)
    for i in xx:
        if i not in tmp:
            copytmp = tmp[:]
            help(i, target, result, copytmp)

print queen(4)