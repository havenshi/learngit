class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.unique(m,n,obstacleGrid,path={})

    def unique(self,m,n,obstacleGrid,path):
        if m == 1 and n == 1 and obstacleGrid[m-1][n-1] == 0:  # base statement
            return 1
        elif m >= 1 and n >=1 and obstacleGrid[m-1][n-1] == 1:   # pay attention to -1
            path[m, n] = 0
            return 0
        elif m == 0 or n == 0:   # range
            return 0
        else:
            if (m-1,n) in path:
                ver = path[(m-1,n)]
            else:
                ver = self.unique(m - 1, n, obstacleGrid, path)
            if (m,n-1) in path:
                hor = path[(m,n-1)]
            else:
                hor = self.unique(m, n - 1, obstacleGrid, path)
            step = ver + hor
            path[m,n] = step
            return step


if __name__ == "__main__":
    answer=Solution()
    print answer.uniquePathsWithObstacles([
[0,0]
])
