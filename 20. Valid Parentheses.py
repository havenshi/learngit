class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        list = []
        l=["(","[","{"]
        n=[")","]","}"]
        issy=True

        if len(s) == 0:
            return False

        i=0
        while i<len(s) and issy:
             if s[i] in l:
                list.append(s[i])
             elif len(list)!=0:
                firsti=list[-1]
                if l.index(firsti)==n.index(s[i]):
                    del list[-1]
                else:
                    issy=False
             else:
                 issy=False

             i+=1

        if len(list)!=0:
            issy=False

        return issy

if __name__ == "__main__":
    s = "([})"
    answer = Solution()
    print answer.isValid(s)