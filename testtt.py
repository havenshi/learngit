# -*- coding: utf-8 -*-

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    global result
    result = []
    candidates.sort()
    for i in range(len(candidates)):
       recursive_comb([candidates[i]], candidates[i:], target)
    return result


def recursive_comb(temp_array, rest_array, target):
    if sum(temp_array) == target:
        if temp_array not in result:
            result.append(temp_array)
    else:
        for i in range(len(rest_array)):
            temp_array2 = temp_array[:]
            temp_array2.append(rest_array[i])
            if sum(temp_array2) <= target:
                recursive_comb(temp_array2, rest_array[i:], target)


print combinationSum([2, 3, 6, 7], 7)
