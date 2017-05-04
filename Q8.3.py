def subset(nums):
    result = [[]]
    for item in nums:
        tmp = []
        for res in result:
            tmp.append(res + [item])
        result += tmp
    return result
print subset([1, 2])

# recursion
def subset2(nums):
    if len(nums) == 1:
        return [[], nums]
    else:
        tmp = [[nums[0]] + item for item in subset2(nums[1:])]
        return subset2(nums[1:]) + tmp
print subset2([1, 2])