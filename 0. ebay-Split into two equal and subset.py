class Solution(object):
    def split(self,nums):
        total = sum(nums)
        if total%2==1:
            return False
        else:
            total/=2
            n=len(nums)
            nums=sorted(nums)
            res = [[0 for j in range(total + 1)] for i in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, total + 1):
                    res[i][j] = res[i - 1][j] # copy the last line
                    if j >= nums[i - 1] and res[i - 1][j] < nums[i-1]:  # item is max
                        res[i][j] = nums[i-1]
                    if (j-nums[i - 1]) in res[i-1] and nums[i-1] < j and res[i - 1][j] < j: # add item and (j-item) from the last line
                        res[i][j]=j
                    if (j-nums[i - 1])>0 and (j-nums[i - 1]) not in res[i-1]: # if j-nums[i - 1] is not 0, copy left of this line
                        res[i][j]=res[i][j-1]
            # now res is [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 4], [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9], [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 10], [0, 0, 2, 2, 4, 5, 6, 6, 8, 8, 10]]
            matrix=[]
            for i in range(1, n + 1):
                matrix+=res[i]
            return total in matrix
if __name__ == "__main__":
    nums = [2, 5, 2, 6, 5]
    nums2=[1,5,5,12]
    answer = Solution()
    print answer.split(nums)
    print answer.split(nums2)