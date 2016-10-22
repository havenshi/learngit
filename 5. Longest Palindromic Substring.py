class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        long=""
        temp=""
        i=0
        gap = 2
        gap2=1

        if len(s)==1:
            return s

        while i < len(s)-gap:
            if s[i] == s[i+gap]:
                temp=s[i:i+gap+1]
                ii=i
                ii-=1
                gap+=2

                while 0<=ii<len(s)-gap and s[ii] == s[ii+gap]:
                    temp=s[ii:ii+gap+1]
                    ii -= 1
                    gap += 2

                if len(long)<len(temp):
                    long=temp

                temp=""
                i=i+1
                gap=2

            else:
                i+=1

        i=0

        while i < len(s) - gap2:
            if s[i] == s[i+gap2]:
                temp=s[i:i+gap2+1]
                ii=i
                ii-=1
                gap2+=2

                while 0<=ii<len(s)-gap2 and s[ii] == s[ii+gap2]:
                    temp=s[ii:ii+gap2+1]
                    ii -= 1
                    gap2 += 2

                if len(long)<len(temp):
                    long=temp

                temp=""
                i=i+1
                gap2 = 1

            else:
                i+=1

        temp=s[0]
        if len(long) < len(temp):
            long = temp

        return long

if __name__ == "__main__":
    answer = Solution()
    # s="abcbaabcdedcbafghiihgf"
    s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    print answer.longestPalindrome(s)
