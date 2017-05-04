def validate(s):
    stack = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(':
            stack.append(s[i])
        if s[i] == ')':
            if stack:
                stack.pop()
            else:
                s = s[:i] + s[i+1:]
                n -= 1
                continue
        i += 1
    return s

print validate('(())))((()))')