class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 0
        if n < 0:
            flag = 1
            n = abs(n)
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n >>= 1
        if flag:
            return 1/res
        else:
            return res

if __name__ == "__main__":
    answer=Solution()
    print answer.myPow(1.3, -2)
