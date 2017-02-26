class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) <= 1:
        #     return nums
        # newnums = [nums[0]]
        # comp = nums[0]
        # count = 1
        # for item in nums[1:]:
        #     if item == comp:
        #         count += 1
        #         if count > 2:
        #             continue
        #         else:
        #             newnums.append(item)
        #     else:
        #         comp = item
        #         count = 1
        #         newnums.append(item)
        # return newnums

        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i
if __name__ == "__main__":
    answer=Solution()
    print answer.removeDuplicates([1,1,1,2,2,3])