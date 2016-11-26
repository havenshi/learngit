n=5   # how many items
c=10  # max weight of bag
w=[2,2,6,5,4] # weight of each item
v=[6,3,5,4,6] # value of each item

class Solution(object):
    def bag(self,n,c,w,v):
        res=[[-1 for j in range(c+1)] for i in range(n+1)]
        for j in range(c+1):
            res[0][j]=0
        for i in range(1,n+1):
            for j in range(1,c+1):
                res[i][j]=res[i-1][j]
                if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
                    res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
        return res
if __name__ == "__main__":
    answer = Solution()
    print answer.bag(n,c,w,v)