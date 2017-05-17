class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n > 0:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) / 26
        return ans
if __name__ == "__main__":
    print Solution().convertToTitle(52)