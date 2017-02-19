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
        mapjudge = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in map:
                    map[board[i][j]] = [[i,j]]
                else:
                    map[board[i][j]] = map[board[i][j]] + [[i, j]]
                mapjudge[(i,j)] = 0   # label the map 0 if not used

        if word[0] not in map:
            return False
        else:
            if len(word) == 1:
                return True
            else:
                for position in map[word[0]]:
                    if self.existtest(position, word[1:], step, map):
                        return True
                return False

    def existtest(self, position, array, step, map):
        if len(array) == 1:
            for eachstep in step:
                if [position[0]+eachstep[0],position[1]+eachstep[1]] in map[array[0]]:
                    return True
            return False
        else:
            for eachstep in step:
                if [position[0]+eachstep[0],position[1]+eachstep[1]] in map[array[0]]:
                    copy_position = [position[0]+eachstep[0],position[1]+eachstep[1]]  # attention! use copy!
                    if self.existtest(copy_position, array[1:], step, map):  # attention! need 'if', or will return false even further option is true.
                        return True
            return False

if __name__ == "__main__":
    answer=Solution()
    print answer.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCEES")
