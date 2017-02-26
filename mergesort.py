def merge(array):
    if len(array) <= 1:  # base
        return array
    mid = len(array) / 2
    left = merge(array[:mid])  # sort left part
    right = merge(array[mid:])  # sort right part
    return merge_method(left, right)


def merge_method(left, right):
    l, r = 0, 0  # cursors of left and right part
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # append remaining part
    result += left[l:]
    result += right[r:]
    return result


print merge([7, 1, 2, 4, 6])
