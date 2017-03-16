class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)[::-1]
        if len(nums) < 4:
            return False
        if sum(nums) % 4 != 0:
            return False
        side = sum(nums) / 4
        self.setside(nums, side)
        # for i in range(3):
        #     self.removeside(nums,side) # remove 3 sides
        #     print nums
        # if sum(nums) == side:
        #     return True
        # else:
        #     return False

    def setside(self,nums,side):
        n = len(nums)
        res = [[False for j in range(side + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, side + 1):
                res[i][j] = res[i - 1][j] # 1.copy the last line
                if j == nums[i - 1]:
                    res[i][j] = nums[i - 1] # 2.put single item in the right position
                if nums[i - 1] + res[i - 1][j - nums[i-1]] <= side:# 3.i-1 is current item of nums. [i-1] upper row, [j-nums[i-1]] the column which delete current item.
                    res[i][j] = nums[i-1] + res[i-1][j-nums[i-1]]
        return res

                # if res[i][j] == side: # the first side appears, then stop
                #     while i >= 1 and j >= 0: # if greater than, remove item from nums list, if not, move to upper line
                #         if j >= nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1]) > res[i - 1][j]:
                #             j -= nums[i - 1]
                #             nums.remove(nums[i - 1])
                #         i -= 1

if __name__ == "__main__":
    answer=Solution()
    print answer.makesquare([1,1,1,2,2,2,2,3,3,3,5,5,10])
