class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        d = {}
        res = []
        for i in range(n):
            substr = s[i:i + 10]
            d[substr] = d.get(substr, 0) + 1
        for key, val in d.items():
            if val > 1:
                res.append(key)
        return res
if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")