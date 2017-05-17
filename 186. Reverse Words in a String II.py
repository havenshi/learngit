# Time: O(n)
# Space:O(1)
#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?
#

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.help(s, 0, len(s)-1)
        begin = 0
        i = 0
        while i <= len(s):
            if i == len(s) or s[i] == ' ':
                self.help(s, begin, i-1)
                begin = i+1
            i += 1

    def help(self, string, start, end):
        for i in range((end - start)/2+1):
            string[start+i], string[end-i] = string[end-i], string[start+i]

if __name__ == "__main__":
    print Solution().reverseWords(['t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'])
