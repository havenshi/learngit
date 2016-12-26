[2, 1, 5, 6, -1, 43, 7]
8

def two_sum(nums, target):
    my_dict = {}
    for i in nums:
        if my_dict.get(i):
            return i, my_dict[i]
        my_dict[target - i] = i
