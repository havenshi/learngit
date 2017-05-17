# -*- coding:utf8 -*-
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = ''
        while nums:
            item = nums.pop(self.help(nums))
            res += str(item)
        if (res[0]=='0'):
            return '0'
        return res

    def help(self, nums):  # 如果a＋b串大于b＋a串，那么a比较大，反之b比较大。
        strnums = [str(x) for x in nums]
        index = 0
        for i in range(1, len(strnums)):
            if int(strnums[i] + strnums[index]) > int(strnums[index] + strnums[i]):
                index = i
        return index

if __name__ == "__main__":
    print Solution().largestNumber([1,4,7,2,5,8,0,3,6,9])


