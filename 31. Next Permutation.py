# 1. From right to left, find the first digit (PartitionNumber) which violate the increase trend.
# 2. From right to left, find the first digit which larger than PartitionNumber, call it ChangeNumber.
# 3. Swap the PartitionNumber and ChangeNumber.
# 4. Reverse all the digit on the right of partition index.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

                        # can't use nums[i+1:].reverse() to swap
                for j in range(0, (len(nums) - i) // 2):
                    nums[0 + j + (i + 1)], nums[len(nums) - 1 - (i + 1) - j + (i + 1)] = nums[len(nums) - 1 - (
                    i + 1) - j + (i + 1)], nums[0 + j + (i + 1)]
                break
        else:
            nums.reverse()


if __name__ == "__main__":
    answer=Solution()
    print answer.nextPermutation([1,3,2])
