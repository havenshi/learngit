class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method 1
        # length=len(nums)
        # l=[0]*length
        # for i in range(length-1,-1,-1):
        #     if nums[i]>=length:
        #         step=length                 # delete duplicate after 0~length-1 step
        #     else:
        #         step=nums[i]
        #     for j in range(step,-1,-1):
        #         flag=(i+j)%length
        #         if l[i]==1 or flag==length-1 or l[flag]==1:
        #             l[i]=1
        #             break
        # if l[0]>0:
        #     return True
        # else:
        #     return False

        # method 2
        length=len(nums)
        goal = length-1
        for i in range(length-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i    # change goal to the position
        return goal==0   # fist position is possible


if __name__ == "__main__":
    answer=Solution()
    print answer.canJump([0,1])