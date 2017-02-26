import copy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(board)
        n = len(board[0])
        map = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in map:
                    map[board[i][j]] = [[i,j]]
                else:
                    map[board[i][j]] = map[board[i][j]] + [[i, j]]

        if m*n < len(word):   # judge if word length is greater than board
            return False

        if word[0] not in map:
            return False
        else:
            if len(word) == 1:
                return True
            else:
                for position in map[word[0]]:
                    copy_map = copy.deepcopy(map)   # use deep copy!
                    copy_map[word[0]].remove(position)  # remove the position it passes by, use copy! then we can return later.
                    if self.existtest(position, word[1:], step, copy_map):
                        return True
                return False

    def existtest(self, position, array, step, map):
        if len(array) == 1:
            for eachstep in step:
                if array[0] in map and [position[0]+eachstep[0],position[1]+eachstep[1]] in map[array[0]]:  # 'array[0] in map' is important!
                    return True
            return False
        else:
            for eachstep in step:
                if [position[0]+eachstep[0],position[1]+eachstep[1]] in map[array[0]]:
                    copy_position = [position[0]+eachstep[0],position[1]+eachstep[1]]  # attention! use copy!
                    copy_map = copy.deepcopy(map)
                    copy_map[array[0]].remove(copy_position)  # attention! use copy!
                    if self.existtest(copy_position, array[1:], step, copy_map):  # attention! need 'if', or will return false even further option is true.
                        return True
            return False


    # method2
    # def exist(self, board, word):
    #     if not board:
    #         return False
    #     for i in xrange(len(board)):
    #         for j in xrange(len(board[0])):
    #             if self.dfs(board, i, j, word):
    #                 return True
    #     return False
    #
    # # check whether can find word, start at (i,j) position
    # def dfs(self, board, i, j, word):
    #     if len(word) == 0: # all the characters are checked
    #         return True
    #     if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
    #         return False
    #     tmp = board[i][j]  # first character is found, check the remaining part
    #     board[i][j] = "#"  # avoid visit agian
    #     # check whether can find "word" along one direction
    #     res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    #     or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    #     board[i][j] = tmp  # return back
    #     return res

if __name__ == "__main__":
    answer=Solution()
    print answer.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCEESEC")
