class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            i += 1
        return dp[-1]
if __name__ == "__main__":
    print Solution().rob([0,0,0])