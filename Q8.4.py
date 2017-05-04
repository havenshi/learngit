def permutation(nums):
    result = []
    for i in range(len(nums)):
        help([nums[i]], nums[:i] + nums[i+1:], len(nums), result)
    return result

def help(before, after, target, result):
    if len(before) == target:
        result.append(before)
    else:
        for i in range(len(after)):
            help(before + [after[i]], after[:i] + after[i+1:], target, result)

print permutation([1,2,3])