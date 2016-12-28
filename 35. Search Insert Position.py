class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <=nums[0]:
            return 0
        else:
            for i in range(len(nums)):
                if target>nums[i]:
                    continue
                else:
                    return i

            return len(nums)

if __name__ == "__main__":
    answer=Solution()
    print answer.searchInsert([1,3,5,6], 7)
