class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = sum(nums[:3])
        if len(nums) < 3:
            return 0
        elif list(set(nums)) == [0]:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if abs(total - target) < abs(ans-target):
                        ans=total
                    if total <= target:
                        left += 1
                    else:
                        right -= 1

        return ans

if __name__ == "__main__":
    answer=Solution()
    print answer.threeSumClosest([-1, 2, 1, -4],1)
