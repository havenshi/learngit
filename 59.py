# A square joining together
class Solution(object):
    def removeoneside(self,nums,i):
        total = sum(nums)/i
        n=len(nums)
        res = [[0 for j in range(total + 1)] for i in range(n + 1)]
        # res[i][j] = max(res[i - 1][j],res[i-1][j-nums[i-1]]+nums[i-1])
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                res[i][j] = res[i - 1][j] # copy the last line
                if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]: # greater than
                    res[i][j]=res[i-1][j-nums[i-1]]+nums[i-1]

                if res[i][j]==total: # the first side appears, then stop
                    while i>=1 and j>=0: # if greater than, remove item from nums list, if not, move to upper line
                        if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]:
                            j-=nums[i - 1]
                            nums.remove(nums[i - 1])
                        i-=1
                    return nums

    def square(self,list):
        list = sorted(list)
        for i in range(4,0,-1):
            total = sum(list)
            if total % i != 0:
                return "No"
            else:
                self.removeoneside(list,i) # remove 4 sides

        if list==[]:
            return "Yes"
        else:
            return "No"

if __name__ == "__main__":
    list = [3,3,3,3,4]
    answer = Solution()
    print answer.square(list)