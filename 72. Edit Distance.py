class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if not word1 and not word2:
            return 0
        if not word1:
            return l2
        if not word2:
            return l1
        map = [[0 for j in range(l1+1)] for i in range(l2+1)]
        for i in range(l2+1):
            for j in range(l1+1):
                if i == 0:
                    map[0][j] = j
                elif j == 0:
                    map[i][0] = i
                elif word1[j-1] == word2[i-1]:
                    map[i][j] = map[i-1][j-1]
                else:
                    map[i][j] = min(map[i-1][j],map[i][j-1],map[i - 1][j - 1]) + 1
        return map[-1][-1]

if __name__ == '__main__':
    answer = Solution()
    print answer.minDistance('a','b')