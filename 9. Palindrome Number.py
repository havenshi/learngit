class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        if len(y)==1:
            return True

        else:
            pal=True
            i=0

            while i < len(y)/2 and pal:
                if y[i]==y[len(y)-1-i]:
                    i+=1
                else:
                    pal=False
            return pal

if __name__=="__main__":
    answer=Solution()
    print answer.isPalindrome(123212)
