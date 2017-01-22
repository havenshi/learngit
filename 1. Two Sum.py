class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if target-nums[i]==nums[j]:
        #             return [i,j]

        m={}
        for i in range(len(nums)):
            if nums[i] in m:
                return [m[nums[i]],i]
            else:
                m[target-nums[i]]=i


if __name__ == "__main__":
    answer = Solution()
    nums=[0,2,3,0]
    target = 0
    print answer.twoSum(nums, target)

