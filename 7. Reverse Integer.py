class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x)!=x:
            a=-1
        else:
            a=1

        x=abs(x)
        total=0
        while x>0:
            n=x%10
            total=total*10+n
            x=x//10

        return total*a
if __name__ == "__main__":
    answer = Solution()
    print answer.reverse(321)