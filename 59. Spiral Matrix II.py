class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        begin = 0
        nn=n*n
        nums=[]
        for i in range(nn,0,-1):
            nums.append(i)          # create a num list to use
        matrix=[[0 for x in range(n)] for y in range(n)]     # create an empty matrix. Attention! Don't use [[0]*n]*n!

        if n==0:
            return []
        else:
            return self.rotate(matrix,begin,n-1,nums)                     #-------|
                                                                          #|       |
    def rotate(self,cube,start,end,numslist):  # traversal each peering   #|-------|
                                               # base state
        if start<=end:       # don't forget this condition!
            if start==end:   # if the central is remain
                cube[start][start] = numslist.pop()
            else:
                for y in range(start,end+1):       # if last row, traversal the column
                    cube[start][y]=numslist.pop()
                for x in range(start+1,end+1):     # if 2nd column, traversal the row
                    cube[x][end]=numslist.pop()
                for y in range(end-1,start-1,-1):  # if 3rd row, traversal the column
                    cube[end][y]=numslist.pop()
                for x in range(end-1,start+1-1,-1):# if 4th column, traversal the row
                    cube[x][start]=numslist.pop()
                self.rotate(cube, start+1, end-1, numslist)  # peering next inside layer

        return cube


if __name__ == "__main__":
    answer=Solution()
    print answer.generateMatrix(3)
