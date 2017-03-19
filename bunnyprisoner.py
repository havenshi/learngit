def answer(x, y):
    # start = 1
    # step = 1
    # for i in range(2, y+1):
    #     start += step
    #     step += 1

    # start = 1 + (1+(y-1))*(y-1)/2

    # step2 = 2
    # for i in range(2, y+1):
    #     step2 += 1

    # step2 = 2+(y-1)

    # id = start
    # for i in range(2, x+1):
    #     id += step2
    #     step2 += 1

    # id = start + (x-1)*step2 + (1+(x-2))*(x-2)/2
    id = 1 + y*y/2 - 3*y/2 + x*x/2 - x/2 + x*y
    return id
print answer(1,3)