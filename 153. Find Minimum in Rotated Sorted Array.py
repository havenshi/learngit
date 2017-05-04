class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left)/2
            if nums[mid] > nums[left] and nums[mid] < nums[right]:
                return nums[left]
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
        return min(nums[left], nums[right])