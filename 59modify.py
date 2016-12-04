# A square joining together
class Solution(object):
    def removeoneside(self,nums,side):
        n=len(nums)
        res = [[0 for j in range(side + 1)] for i in range(n + 1)]
        # res[i][j] = max(res[i - 1][j],res[i-1][j-nums[i-1]]+nums[i-1])
        for i in range(1, n + 1):
            for j in range(1, side + 1):
                res[i][j] = res[i - 1][j] # copy the last line
                if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]: # greater than
                    res[i][j]=res[i-1][j-nums[i-1]]+nums[i-1]

                if res[i][j]==side: # the first side appears, then stop
                    eachside=[]
                    while i>=1 and j>=0: # if greater than, remove item from nums list, if not, move to upper line
                        if j>=nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1])>res[i - 1][j]:
                            j-=nums[i - 1]
                            eachside.append(nums[i - 1])
                            nums.remove(nums[i - 1])
                        i-=1
                    print eachside
                    break
            else: continue
            break    # Jump out of the multilayer circulation
        return nums



    def square(self,lister):
        lister = sorted(lister)[::-1]
        total = sum(lister)
        if total % 4 != 0:
            return "No"
        else:
            for i in range(4):
                self.removeoneside(lister,total/4) # remove 4 sides

        if lister==[]:
            return "Yes"
        else:
            return "No"

if __name__ == "__main__":
    lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 32, 4, 32, 2, 34, 4, 3, 43, 43, 2, 2, 34, 43, 2, 34, 43, 2, 34, 43, 24, 3, 24, 32,
       3, 21, 64, 6, 5, 5, 3]
    answer = Solution()
    print answer.square(lister)