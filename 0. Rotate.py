class Solution(object):
    def rotate(self, list):
        n=len(list)
        column_list=[[] for i in range(n)]
        new_list=[]

        for i in range(n):
            for j in range(n-1,-1,-1):
                column_list[i]+=[list[j][i]]
            new_list+=[column_list[i]]
        return new_list

if __name__ == "__main__":
    list=[[1,2,3],[4,5,6],[7,8,9]]
    list2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    answer = Solution()
    print answer.rotate(list)
    print answer.rotate(list2)