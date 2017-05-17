class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        array = list(s)
        res = 0
        for a in array:
            res = res * 26 + alpha.index(a) + 1
        return res