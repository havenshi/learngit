def validate(s):
    stack = []
    stackindex = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(':
            stack.append(s[i])
            stackindex.append(i)
        if s[i] == ')':
            if stack:
                stack.pop()
                stackindex.pop()
            else:
                s = s[:i] + s[i+1:]
                n -= 1
                continue
        i += 1
    s = list(s)
    s = ''.join([s[i] for i in range(n) if i not in stackindex])

    return s

print validate('(())((((()))')
print validate('(())((())))')