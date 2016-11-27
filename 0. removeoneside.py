class Solution(object):
    def removeoneside(self,nums):
        total = sum(nums)
        if total%2==1:
            return False
        else:
            total/=2
            n=len(nums)
            nums=sorted(nums)
            res = [[0 for j in range(total + 1)] for i in range(n + 1)]
            # res[i][j] = max(res[i - 1][j],res[i-1][j-nums[i-1]]+nums[i-1])
            for i in range(1, n + 1):
                for j in range(1, total + 1):
                    res[i][j] = res[i - 1][j] # copy the last line
                    if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]: # greater than
                        res[i][j]=res[i-1][j-nums[i-1]]+nums[i-1]

                    if res[i][j]==total: # the first side appears, then stop
                        print res
                        while i>=1 and j>=0: # if greater than, remove item from nums list, if not, move to upper line
                            if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]:
                                j-=nums[i - 1]
                                nums.remove(nums[i - 1])
                            i-=1
                        return nums

if __name__ == "__main__":
    nums = [2, 5, 2, 6, 5]
    answer = Solution()
    print answer.removeoneside(nums)