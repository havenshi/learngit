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
                j=i%(2*numRows-2)     # which position (normal column or not)
                if j in range(0,numRows): # if position is in normal column
                    list[j] += s[i]       # append this item to this row
                else:
                    list[2*numRows-2-j] += s[i]  # find reversed row and append that item to this row

            newlist=""
            for i in range(len(list)):
                newlist+=''.join(list[i])
            return newlist

        else:
            return s

        # method 2
        # if numRows == 1 or numRows >= len(s):
        #     return s
        #
        # L = [''] * numRows
        # index, step = 0, 1
        #
        # for x in s:
        #     L[index] += x
        #     if index == 0:
        #         step = 1
        #     elif index == numRows -1:
        #         step = -1
        #     index += step
        #
        # return ''.join(L)

if __name__ == "__main__":
    answer = Solution()
    print answer.convert("PAYPALISHIRING", 3)