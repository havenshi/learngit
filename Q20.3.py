def random():
    array = [x for x in range(1, n)]
    for i in range(m): # 抽m次
        j = rand() % (n - i) + i  # 从array[i]到最后这段随机抽
        array[i], array[j] = array[j], array[i]