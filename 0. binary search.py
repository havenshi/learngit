# -*- coding: utf-8 -*-
class Solution(object):
    def BinarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:  # Tip1:相邻或交叉则跳出，不会产生死循环
            mid = left + (right - left)/2 # 防溢出，面试中的加分项
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid # Tip2:left或right直接等于mid即可，不用+-1
            else:
                left = mid
        if nums[left] == target: return left # Tip3:最后对比left和right两次
        if nums[right] == target: return right


    # def BinarySearch2(self, list, n): //recursion方法
    #     if len(list):
    #         return False
    #     mid = len(list) // 2
    #     if n < list[mid]:
    #         return self.BinarySearch(list[:mid], n)
    #     elif n > list[mid]:
    #         return self.BinarySearch(list[mid:], n)
    #     else:
    #         return True

if __name__ == "__main__":
    answer = Solution()
    print answer.BinarySearch([8,9,10,12,14,17,19], 14)