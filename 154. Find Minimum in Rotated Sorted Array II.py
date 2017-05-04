class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            if nums[left] == nums[right]:  # must be a horizontal line on the left
                value = nums[left]
                while nums[left] == value:
                    if left == right:
                        return value # all the item is same
                    left += 1
            mid = left + (right - left)/2
            if nums[mid] >= nums[left] and nums[mid] <= nums[right]:
                return nums[left]
            elif nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])