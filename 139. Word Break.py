class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in wordDict:
            return True
        for i in range(len(wordDict)):
            if self.helper(wordDict[i], s):
                news = s.replace(wordDict[i], '', 1)  # 1 means remove substring from string just once
                print news
                if self.wordBreak(news, wordDict):
                    return True
        return False

    def helper(self, item, s):
        if len(s) >= len(item) and s[:len(item)] == item:
            return True
        else:
            return False


        # method2 DP
        # if s == '':
        #     return True
        # checklist = [False]*(len(s)+1)
        # checklist[len(s)] = True
        # for i in range(len(s)-1,-1,-1):
        #     for j in range(i,len(s)):
        #         if s[i:j+1] in wordDict and checklist[j+1]==True:
        #             checklist[i]=True
        # return checklist[0]

if __name__ == "__main__":
    answer = Solution()
    print answer.wordBreak("bb",["a","b","bbb","bbbb"])