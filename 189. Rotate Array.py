class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # san bu fanzhuan fa
        k %= len(nums)
        if k == 0:
            return
        start1= 0
        end1 = len(nums)-k-1
        for i in range((end1-start1)/2+1):
            nums[start1+i], nums[end1-i] = nums[end1-i], nums[start1+i]
        start2 = len(nums)-k
        end2 = len(nums)-1
        for i in range((end2-start2)/2+1):
            nums[start2+i], nums[end2-i] = nums[end2-i], nums[start2+i]
        print nums
        for i in range(len(nums)/2):
            nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]

if __name__ == "__main__":
    print Solution().rotate([1,2],1)