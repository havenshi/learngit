def search1(array,target):  # while
    array.sort()
    l, r = 0, len(array)-1
    while l <= r:
        mid = (l+r)/2
        if target == array[mid]:
            return True
        if target > array[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False

print search1([1,2,3,4,7,8,9,10],1)


def search2(array,target):  # recursion
    array.sort()
    if len(array) < 1:
        return False
    else:
        l, r = 0, len(array) - 1
        mid = (l+r)/2
        if target == array[mid]:
            return True
        elif target > array[mid]:
            return search2(array[mid + 1:], target)
        else:
            return search2(array[: mid], target)

print search2([1,2,3,4,7,8,9,10],7)