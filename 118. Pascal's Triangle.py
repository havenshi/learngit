class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            newRow = [1]
            for j in range(0, len(result[i - 2]) - 1):
                newRow.append(result[i - 2][j] + result[i - 2][j + 1])
            newRow.append(1)
            result.append(newRow)
        return result