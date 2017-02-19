class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # method1 time limit exceeded
    #     m = len(grid)
    #     n = len(grid[0])
    #     return self.unique(m, n, grid, path={})
    #
    # def unique(self, m, n, grid, path):
    #     if m == 1 and n == 1:
    #         path[(m, n)] = grid[m - 1][n - 1]
    #         return grid[m - 1][n - 1]
    #     else:
    #         step = sum(sum(i) for i in grid)  # sum elements in matrix
    #         if m > 1 and n > 1:
    #             if (m - 1, n) in path:
    #                 ver = path[(m - 1, n)] + grid[m - 1][n - 1]
    #             else:
    #                 ver = self.unique(m - 1, n, grid, path) + grid[m - 1][n - 1]
    #             if (m, n - 1) in path:
    #                 hor = path[(m, n - 1)] + grid[m - 1][n - 1]
    #             else:
    #                 hor = self.unique(m, n - 1, grid, path) + grid[m - 1][n - 1]
    #             step = min(ver, hor)
    #         elif m == 1 and n > 1:
    #             if (m, n - 1) in path:
    #                 step = path[(m, n - 1)] + grid[m - 1][n - 1]
    #             else:
    #                 step = self.unique(m, n - 1, grid, path) + grid[m - 1][n - 1]
    #         elif n == 1 and m > 1:
    #             if (m - 1, n) in path:
    #                 step = path[(m - 1, n)] + grid[m - 1][n - 1]
    #             else:
    #                 step = self.unique(m - 1, n, grid, path) + grid[m - 1][n - 1]
    #         path[m, n] = step
    #         return step

        # method2
        m = len(grid)
        n = len(grid[0])

        if m < 2 or n < 2: return sum([sum(i) for i in grid])  # single row or column

        for i in xrange(1, m):             # set first column
            grid[i][0] += grid[i - 1][0]
        for i in xrange(1, n):             # set first row
            grid[0][i] += grid[0][i - 1]

        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] += grid[i - 1][j] if grid[i - 1][j] < grid[i][j - 1] else grid[i][j - 1]

        return grid[-1][-1]
if __name__ == "__main__":
    answer=Solution()
    print answer.minPathSum([
[1,2],[4,5]
])
