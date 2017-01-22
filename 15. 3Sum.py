class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # method 1 brute force
        # mylist=[]
        # if len(nums)<3:
        #     return []
        # else:
        #     for i in range(len(nums)):
        #         for j in range(len(nums[i + 1:])):
        #             if (0-nums[i]-nums[i + 1:][j]) in nums[i + 1:][j + 1:]:
        #                 sublist=[nums[i],nums[i + 1:][j],0-nums[i]-nums[i + 1:][j]]
        #                 if sorted(sublist) not in mylist:
        #                     mylist += [sorted(sublist)]
        #     return mylist

        # method 2
        nums=sorted(nums)
        mylist=[]
        if len(nums)<3:
            return []
        else:
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                target = nums[i]*(-1)
                left, right = i+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        sublist = [nums[i], nums[left], nums[right]]
                        if sorted(sublist) not in mylist:
                            mylist += [sorted(sublist)]
                            right -= 1
                            left += 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1

        return mylist

if __name__ == "__main__":
    answer=Solution()
    print answer.threeSum([0,0,0])
