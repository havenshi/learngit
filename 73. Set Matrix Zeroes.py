class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]  # false * rownum
        col = [False for i in range(colnum)]  # false * colnum
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:   # set true to the corresponding row, col position.
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

if __name__ == "__main__":
    answer=Solution()
    print answer.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
