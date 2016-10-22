class Solution(object):
    def BinarySearch(self,list,n):
        if len(list):
            return False
        mid = len(list) // 2
        if n<list[mid]:
            return self.BinarySearch(list[:mid],n)
        elif n>list[mid]:
            return self.BinarySearch(list[mid:],n)
        else:
            return True

    def binarysearch(self, nums, n):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > n:
                right = mid
            if nums[mid] < n:
                left = mid + 1
            if nums[mid] == n:
                return mid

if __name__ == "__main__":
    n = 20
    list=[ 8, 9, 10,12,14,17,19]
    answer = Solution()
    print answer.BinarySearch(list,n)