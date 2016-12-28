class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        begin=0
        m=len(matrix)-1
        if m<0:
            return []
        else:
            n = len(matrix[0])-1
            return self.rotate(matrix,begin,m,n)

    def rotate(self,l,start,end1,end2):
        r = []
        if start<=end1 and start<=end2:
            if start==end1 and start!=end2:
                for y in range(start,end2+1):
                    r.append(l[start][y])
            elif start!=end1 and start==end2:
                for x in range(start,end1+1):
                  r.append(l[x][start])
            elif start==end1 and start==end2:
                r.append(l[start][start])
            elif start==end1+1 and start==end2+1:
                r=r+[l[start][start]]+[l[start][end1]]+[l[end1][start]]+[l[end1][end1]]

            else:
                for y in range(start,end2+1):
                    r.append(l[start][y])
                for x in range(start+1,end1+1):
                    r.append(l[x][end2])
                for y in range(end2-1,start-1,-1):
                    r.append(l[end1][y])
                for x in range(end1-1,start+1-1,-1):
                    r.append(l[x][start])
                r=r+self.rotate(l, start+1, end1-1, end2-1)
            return r

        else:
            return []

if __name__ == "__main__":
    answer=Solution()
    print answer.spiralOrder([[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]])
