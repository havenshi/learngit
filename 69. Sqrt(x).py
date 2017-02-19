class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sr = x
        while sr**2 > x:
            better = (sr+x/sr)/2
            sr = better
        return sr

if __name__ == "__main__":
    answer=Solution()
    print answer.mySqrt(2)
