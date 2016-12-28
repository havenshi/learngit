class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        for i in range(n-1):
            s=self.generator(s)
        return s

    def generator(self,nums):
        flag = nums[0]
        count = 1
        newnums = ""
        for i in range(1, len(nums)):
            if nums[i] != flag:
                newnums += str(count) + str(flag)
                flag = nums[i]
                count = 1
            else:
                count += 1
        return newnums + str(count) + str(flag)

if __name__ == "__main__":
    answer=Solution()
    print answer.countAndSay(1)
