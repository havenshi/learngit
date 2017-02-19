class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        return len(l[-1]) if len(l)>0 else 0

if __name__ == "__main__":
    answer=Solution()
    print answer.lengthOfLastWord("Hello World")