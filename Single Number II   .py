# -*- coding:utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0
        for i in range(len(nums)):
            two |= nums[i] & one  # two为1时，不管A[i]为什么，two都为1
            one = nums[i] ^ one  # 异或操作，都是1就进位
            three = ~(one & two)  # 以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three
            two &= three
        return one

if __name__ == "__main__":
    answer = Solution()
    print answer.singleNumber([1,1,1,2,2,2,3,4,4,4])