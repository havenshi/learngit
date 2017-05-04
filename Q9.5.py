# -*- coding:utf8 -*-
def search(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right)/2
        while array[mid] == '' and mid <= right: # 如果出现空，则mid向右移动
            mid += 1
        if mid > right:
            right = mid - 1 # 如果超出右边，则范围选择左边
        else:
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print search(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'ball')