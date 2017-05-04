class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return self.search(nums, 0, size - 1)

    def search(self, nums, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return nums.index(max(nums[start], nums[end]))
        mid = (start + end) / 2
        if nums[mid] < nums[mid - 1]:
            return self.search(nums, start, mid - 1)
        if nums[mid] < nums[mid + 1]:
            return self.search(nums, mid + 1, end)
        return mid