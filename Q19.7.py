def total(array):
    cursum = array[0]
    maxsum = array[0]
    for i in range(1, len(array)):
        cursum = max(cursum + array[i], array[i])
        maxsum = max(cursum, maxsum)
    return maxsum