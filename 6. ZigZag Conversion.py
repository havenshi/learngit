class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)!=1 and numRows!=1:
            list=[[] for i in range(numRows)]
            for i in range(0,len(s)):
                j=i%(2*numRows-2)
                div=i//(2*numRows-2)
                if j in range(0,numRows):
                    list[j] += s[i]
                if j in range(1,numRows-1) and ((2*numRows-2)*(1+div*2)-i)<len(s):
                    list[j]+=s[(2*numRows-2)*(1+div*2)-i]

            newlist=""
            for i in range(len(list)):
                for j in range(len(list[i])):
                    newlist+=list[i][j]
            return newlist

        else:
            return s
if __name__ == "__main__":
    answer = Solution()
    print answer.convert("ab", 3)