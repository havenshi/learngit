# have to step (m-1) on horizontal axis, step (n-1) on vertical axis.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.unique(m,n,path={})   # must set path outside. can't set path inside a function, or it will initiate every time.

    def unique(self,m,n,path):
        if m == 1 or n == 1:
            return 1
        else:
            if (m-1,n) in path:
                ver = path[(m-1,n)]
            else:
                ver = self.unique(m - 1, n, path)
            if (m,n-1) in path:
                hor = path[(m,n-1)]
            else:
                hor = self.unique(m, n - 1, path)
            step = ver + hor
            path[m,n] = step
            return step


if __name__ == "__main__":
    answer=Solution()
    print answer.uniquePaths(33,12)
