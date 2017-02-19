class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            curr=nums[0]
            largest=nums[0]
            for item in nums[1:]:
                curr=max(item,curr+item)
                largest=max(largest,curr)
        return largest

if __name__ == "__main__":
    answer=Solution()
    print answer.maxSubArray([1,-1,4])