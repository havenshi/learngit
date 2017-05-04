# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) == 0:
            return 0
        curlen = 1
        maxlen = 1
        flag = 0
        for i in range(1, len(s)):
            news = "".join(set(s[flag:i+1]))
            if len(news) <= 2:
                curlen += 1
                maxlen = max(maxlen, curlen)
            else:
                curlen = 1
                flag = i
        return maxlen

if __name__ == '__main__':
    answer = Solution()
    print answer.lengthOfLongestSubstringTwoDistinct('cecbaaa')

