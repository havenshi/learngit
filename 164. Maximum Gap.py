# -*- coding:utf8 -*-
# 基数排序
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        count = 0
        maxnum = max(nums)
        while maxnum > 0:
            count += 1
            maxnum /= 10
        for k in range(count): # 最大数有多少位就有多少轮
            s = [[] for _ in range(10)]
            for i in nums:
                s[i / (10 ** k) % 10].append(i) # 在第k位的数字是多少，放到对应的桶中
            nums = [a for b in s for a in b] # s矩阵中的数字遍历一遍
        start = 0
        end = 1
        gap = nums[end] - nums[start]
        while end < n - 1:
            start += 1
            end += 1
            gap = max(gap, nums[end] - nums[start])
        return gap
if __name__ == "__main__":
    print Solution().maximumGap([5,9,8,3,15])