def parentheses(n):
    if n == 1:
        return ['()']
    result = []
    for item in parentheses(n - 1):
        for i in range(2 * len(item)):
            tmp = '(' + item[:i] + ')' + item[i:]
            if tmp not in result:
                result.append(tmp)
    return result
print parentheses(3)