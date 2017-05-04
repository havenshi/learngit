# -*- coding:utf8 -*-
def person(array):
    array.sort()  # 针对身高排序
    # 再找出体重递增的最长子序列
    result = [0] * len(array)
    result[0] = 1
    for i in range(1, len(array)):
        if array[i][1] > array[i - 1][1]:
            result[i] = result[i - 1] + 1
        else:
            result[i] = max(result[i - 1], 1)
    print result[len(array) - 1]

    personarray = []
    for i in range(len(array) - 1, 0, -1):
        if result[i] > result[i - 1]:
            personarray.insert(0, array[i])
    if result[1] == 2:
        personarray.insert(0, array[0])
    return personarray
print person([(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)])