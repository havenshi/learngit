# [1,2,3,4,5]抽到4以后交换1和4，抽出的牌逐渐换到前面，再从剩下的[2,3,1,5]抽
def shuffle(array, n):
    for i in range(n): # 抽n次
        j = rand() % (n - i) + i  # 从array[i]到最后这段随机抽
        array[i], array[j] = array[j], array[i]