class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new=""
        list=[]
        i=0
        while i<len(s):
            if s[i] not in new:
                new+=s[i]
                i+=1
            else:
                old=new
                list+=[old]
                ind=old.index(s[i])
                new=""
                for j in range(ind+1,len(old)):
                    new+=old[j]
                new+=s[i]
                i+=1
        list=list+[new]

        num=0
        for t in range(len(list)):
            if len(list[t])>num:
                num=len(list[t])
        return num

if __name__ == "__main__":
    answer = Solution()
    s="c"
    print answer.lengthOfLongestSubstring(s)