class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in range(1, len(board) - 1):  # begin from top left 1, bottom right -1
            for j in range(1, len(board[0][0]) - 1):
                if self.dfs(board, i, j):
                    tmp = board[i][0][:j] + 'X' + board[i][0][j+1:]
                    board[i] = [tmp]
        return board

    def dfs(self, board, i, j):
        if board[i][0][j] == 'X':
            return True
        if board[i][0][j] == 'O':
            if i == len(board) - 1 or j == len(board[0][0]) - 1:
                return False
            else:
                return self.dfs(board, i + 1, j) and self.dfs(board, i, j + 1)

if __name__ == '__main__':
    answer = Solution()
    print answer.solve([["XXXX"],["XOOX"],["XXOX"],["XOXX"]])