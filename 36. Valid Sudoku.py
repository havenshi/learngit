class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]!="." and not self.checkSudoku(i,j,board):
                    return False
        return True

    def checkSudoku(self,i,j,board):
        for compare in range(9):
            if board[i][j]==board[i][compare] and compare!=j or board[i][j]==board[compare][j] and compare!=i:
                return False
        for x in range(3):
            for y in range(3):
                if board[i][j]==board[i//3*3+x][j//3*3+y] and i!=i//3*3+x and j!=j//3*3+y:
                    return False
        return True

