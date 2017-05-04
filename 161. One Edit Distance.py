# Given two strings S and T, determine if they are both one edit distance apart.

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = len(s)
        l2 = len(t)
        if not s and not t:
            return 0
        if not s:
            return l2
        if not t:
            return l1
        map = [[0 for j in range(l1+1)] for i in range(l2+1)]
        for i in range(l2+1):
            for j in range(l1+1):
                if i == 0:
                    map[0][j] = j
                elif j == 0:
                    map[i][0] = i
                elif s[j-1] == t[i-1]:
                    map[i][j] = map[i-1][j-1]
                else:
                    map[i][j] = min(map[i-1][j],map[i][j-1],map[i - 1][j - 1]) + 1
        return map[-1][-1] == 1


if __name__ == "__main__":
    print Solution().isOneEditDistance("teacher", "teachor")