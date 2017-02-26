class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return True
            while start < mid and nums[start] == nums[mid]:  # tricky part
                start += 1
            if nums[mid] < nums[start]:   # right part is from small to large
                if nums[mid] < target <= nums[end]: # normal sequence
                    start = mid + 1
                else:
                    end = mid -1
            else:                         # left part is from small to large
                if nums[start] <= target < nums[mid]: # normal sequence
                    end = mid - 1
                else:
                    start = mid + 1
        return False


if __name__ == "__main__":
    answer=Solution()
    print answer.search([1,3,1,1,1],3)