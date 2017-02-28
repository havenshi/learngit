class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        if n == 0 or n == 1:
            return 1
        for i in range(2, n + 1):
            result = 0
            for j in range(0, i):
                result += nums[j] * nums[i - 1 - j]
            nums[i] = result
        return nums[n]

if __name__ == '__main__':
    answer = Solution()
    print answer.numTrees(3)