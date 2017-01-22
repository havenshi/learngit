class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        mylist = []
        if len(nums) < 4:
            return []
        else:
            for i in range(0,len(nums)-3):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                for j in range(i+1,len(nums)-2):
                    if j != i+1 and nums[j] == nums[j-1]:
                        continue
                    total = target - nums[i] - nums[j]
                    left, right = j + 1, len(nums) - 1
                    while left < right:
                        if nums[left] + nums[right] > total:
                            right -= 1
                        elif nums[left] + nums[right] < total:
                            left += 1
                        else:
                            mylist.append([nums[i], nums[j], nums[left], nums[right]])
                            right -= 1
                            left += 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                        # while left < right and left != j + 1 and nums[left] == nums[left - 1]:
                        #     left += 1
                        #     print "aaa"
                        # while left < right and right != (len(nums) - 1) and nums[right] == nums[right + 1]:
                        #     right -= 1
                        #     print "bbb"
                        # ! can't include outer part, only include inner part!


        return mylist

if __name__ == "__main__":
    answer=Solution()
    print answer.fourSum([1,1,-1,-1],0)
