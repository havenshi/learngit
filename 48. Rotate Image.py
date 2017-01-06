# -*- coding: utf-8 -*-
#首先沿逆对角线翻转一次，然后按x轴中线翻转一次。
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(n-i-1):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        for i in range(n/2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        return matrix

if __name__ == "__main__":
    answer=Solution()
    print answer.rotate([[1,2],[3,4]])
