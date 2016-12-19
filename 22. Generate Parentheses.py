class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mylist=[]
        if n == 0:
            return []
        else:
            if n == 1:
                return ["()"]
            else:
                for item in self.generateParenthesis(n-1):
                    for i in range(0,(n-1)*2):
                        newp="("+item[:i]+")"+item[i:]
                        if newp not in mylist:
                            mylist.append(newp)
                return mylist

if __name__ == "__main__":
    answer=Solution()
    print answer.generateParenthesis(3)
