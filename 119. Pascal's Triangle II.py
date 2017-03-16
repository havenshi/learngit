class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        result = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            newRow = [1]
            for j in range(0, len(result[i - 1]) - 1):
                newRow.append(result[i - 1][j] + result[i - 1][j + 1])
            newRow.append(1)
            result.append(newRow)
        return result[rowIndex]