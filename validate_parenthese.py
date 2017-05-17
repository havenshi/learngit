def validate(s):
    # stack = []
    # stackindex = []
    # n = len(s)
    # i = 0
    # while i < n:
    #     if s[i] == '(':
    #         stack.append(s[i])
    #         stackindex.append(i)
    #     if s[i] == ')':
    #         if stack:
    #             stack.pop()
    #             stackindex.pop()
    #         else:
    #             s = s[:i] + s[i+1:]
    #             n -= 1
    #             continue
    #     i += 1
    # s = list(s)
    # s = ''.join([s[i] for i in range(n) if i not in stackindex])
    #
    # return s

    res = []
    l = r = pair = 0
    for i in range(len(s)):
        if s[i] == '(':
            l += 1
        elif s[i] == ')' and l > r:
            r += 1
            pair += 1
    l = r = pair
    for i in range(len(s)):
        if s[i] == '(' and l > 0:
            res.append(s[i])
            l -= 1
        elif s[i] == ')' and r > l:
            res.append(s[i])
            r -= 1
            pair -= 1
        if pair == 0:
            break
    return ''.join(res)


print validate('(())((((()))')
print validate('(())((())))')