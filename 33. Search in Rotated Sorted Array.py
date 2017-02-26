class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1



if __name__ == "__main__":
    answer=Solution()
    print answer.search([15,16,19,20,25,1,3,4,5,7,10,14],25)