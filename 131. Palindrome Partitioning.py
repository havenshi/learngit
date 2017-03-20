class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == "":
            return []
        result = []
        length = len(s)
        for i in range(len(s)):
            self.dfs(s[:i + 1], s[i + 1:], length, result, tmp=[])
        return result

    def dfs(self, before, after, length, result, tmp):
        if self.palindrome(before):
            tmp.append(before)
            if len(after) == 0 and sum(len(i) for i in tmp) == length:
                result.append(tmp)
            else:
                for i in range(len(after)):
                    copytmp = tmp[:]
                    self.dfs(after[:i + 1], after[i + 1:], length, result, copytmp)

    def palindrome(self, ss):
        for i in range(len(ss) / 2):
            if ss[i] != ss[len(ss) - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    answer = Solution()
    print answer.partition("aab")

