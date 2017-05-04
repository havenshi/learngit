def find(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right)/2
        if array[mid] == x:
            return mid
        if array[mid] >= array[left]:
            if array[left] <= x < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if array[mid] < array[left]:
            if array[mid] < x <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print find([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 25)