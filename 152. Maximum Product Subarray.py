class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minproduct = nums[0]
        maxproduct = nums[0]
        totproduct = nums[0]
        for i in range(1, len(nums)):
            copymin = minproduct
            minproduct = min(minproduct * nums[i], maxproduct * nums[i], nums[i])
            maxproduct = max(copymin * nums[i], maxproduct * nums[i], nums[i])
            totproduct = max(totproduct, maxproduct)
        return totproduct