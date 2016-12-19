class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        count = 0
        for i in range(0, len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        return count

if __name__ == "__main__":
    answer=Solution()
    print answer.removeDuplicates([1,1,2])
