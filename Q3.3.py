def hanoi(n, sou, bri, des):
    if n == 1:
        print 'from',sou,'to',des
    else:
        hanoi(n-1, sou, des, bri)
        print 'from',sou,'to',des
        hanoi(n - 1, bri, sou, des)

# print hanoi(2,'a','b','c')


# stack
def hanoi2(n, sou, bri, des):
    stack = []
    result = []
    stack.append([n, sou, bri, des])
    while stack:
        item = stack.pop()
        n = item[0]
        sou = item[1]
        bri = item[2]
        des = item[3]
        if n == 1:
            result.append(item)
        else:  # add to stack in reverse order
            stack.append([n-1, bri, sou, des])
            stack.append([1, sou, bri, des])
            stack.append([n-1, sou, des, bri])
    for item in result:
        print 'from '+item[1]+' to '+item[3]

print hanoi2(3,'a','b','c')
