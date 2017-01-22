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



# my method
def lengthOfLongestSubstring(s):
    l=[]
    start=0
    end=0
    for i in range(1,len(s)):
        if s[i] not in s[start:end+1]:
            end += 1
        else:
            l.append(s[start:end+1])
            start=i
            end=i

    m=len(l[0])
    for item in l[1:]:
        if len(item)>m:
            m=len(item)

    return m

print lengthOfLongestSubstring("abcabcbb")