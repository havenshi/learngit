class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in range(1, len(board) - 1):  # begin from top left 1, bottom right -1
            for j in range(1, len(board[0]) - 1):
                if self.dfs(board, i, j):
                    board[i][j] = 'X'
        return board

    def dfs(self, board, i, j):
        if i > len(board) - 1 or i < 0 or j > len(board[0]) - 1 or j < 0:
            return False
        if board[i][j] == 'X':
            return True
        board[i][j] = 'X'  # set the begin to 'X' temporarily
        res = self.dfs(board, i + 1, j) and self.dfs(board, i, j + 1) and self.dfs(board, i - 1, j) and self.dfs(board,
                                                                                                                 i,
                                                                                                                 j - 1)
        board[i][j] = 'O'  # return it back
        return res

if __name__ == '__main__':
    answer = Solution()
    print answer.solve([["O","O","O","O","X","X"],
                        ["O","O","O","O","O","O"],
                        ["O","X","O","X","O","O"],
                        ["O","X","O","O","X","O"],
                        ["O","X","O","X","O","O"],
                        ["O","X","O","O","O","O"]])