class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
    #     if s == '' or s[0] == '0':
    #         return 0
    #     return len(self.helper(s))
    #
    # def helper(self, s):
    #     code = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
    #     if len(s) == 1:
    #         return [[s]]
    #     before = s[:-1]
    #     after = s[-1]
    #     result = []
    #     for i in self.helper(before):
    #         temp = i[:]  # copy
    #         if after != '0':
    #             temp.append(after)
    #             result.append(temp)  # 1.append the last item
    #         if i[-1] + after in code:
    #             temp2 = i[:-1][:]  # copy
    #             temp2.append(i[-1] + after)
    #             result.append(temp2)  # 2.if (the last item of last layer + last item) belongs to code, append it
    #     return result

        # method 2
        code = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
        if s == "" or s[0] == '0':
            return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(len(s)):
            if s[i] != "0":  # exception is '0', since the number of 'X,X,X,0' is 0.
                dp[i+1] += dp[i+1-1]    # 1.append s[-1] to each item of last layer, number doesn't change.
            if s[i-1:i+1] in code:
                dp[i+1] += dp[i+1 - 2]  # 2.if the last two digit is in code, add its number
        return dp[len(s)]
if __name__ == '__main__':
    answer = Solution()
    print answer.numDecodings('101')