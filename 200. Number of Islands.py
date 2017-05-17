class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        newgrid = [list(x) for x in grid]
        ans = 0
        if not len(newgrid):
            return ans
        m = len(newgrid)
        n = len(newgrid[0])
        for i in range(m):
            for j in range(n):
                if newgrid[i][j] == '1':
                    self.dfs(newgrid, i, j)
                    ans += 1
        return ans

    def dfs(self, map, x, y):
        if x > len(map) - 1 or x < 0 or y > len(map[0]) - 1 or y < 0:
            return
        if map[x][y] == '0':
            return
        map[x][y] = '0'
        self.dfs(map, x + 1, y)
        self.dfs(map, x, y + 1)
        self.dfs(map, x - 1, y)
        self.dfs(map, x, y - 1)

if __name__ == '__main__':
    print Solution().numIslands(["11110","11010","11000","00000"])

