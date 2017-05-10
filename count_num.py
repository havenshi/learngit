def count(array):
    map = {}
    if array[0] == array[-1]:
        map[array[0]] = len(array)
    else:
        map[array[0]] = 1
        map[array[-1]] = 1
        help(array, map)
    return map

def help(array, map):
    left = 0
    right = len(array) - 1
    while left + 1 < right:
        mid = left + (right - left)/2
        if array[mid] == array[left]:
            map[array[left]] += mid - left
            left = mid
        elif array[mid] == array[right]:
            map[array[right]] += right - mid
            right = mid
        else:
            map[array[mid]] = 1
            help(array[left: mid+1], map)
            help(array[mid: right+1], map)
            break

print count([1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3])
