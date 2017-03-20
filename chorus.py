def sing(array):
    max = []
    for i in range(1, len(array)-1):
        l = i - 1
        r = i + 1
        flag1 = array[i]
        flag2 = array[i]
        left = []
        right = []
        while l >= 0:
            if array[l] < flag1:
                left.append(array[l])
                flag1 = array[l]
            l -= 1
        while r <= len(array) - 1:
            if array[r] < flag2:
                right.append(array[r])
                flag2 = array[r]
            r += 1
        minimum = min(len(left),len(right))
        tmp = left[-minimum:][::-1] + [array[i]] + right[:minimum]
        if len(max) < len(tmp):
            max = tmp
    return max
nums = [1,2,3,5,6,7,5,4,3,6,7,9,10,9,8,6,3,2]
print sing(nums)