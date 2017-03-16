class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return 0
        n = len(triangle[-1])
        result = [0] * n
        result[0] = triangle[0][0]
        for i in range(1, m):
            for j in range(len(triangle[i])-1,-1,-1): # reversed order, or the value of result[j-1] will be changed
                if j == 0:
                    result[j] = result[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    result[j] = result[j - 1] + triangle[i][j]
                else:
                    result[j] = min(result[j - 1], result[j]) + triangle[i][j]
        return min(result)