class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stepLst = [1] * (n+1)
        start = 2
        while start <= n:
            stepLst[start] = stepLst[start-1] + stepLst[start-2]
            start += 1
        return stepLst[n]

if __name__ == "__main__":
    answer=Solution()
    print answer.climbStairs(3)
