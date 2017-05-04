class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    # TLE
    #     if len(s) < len(p):
    #         return []
    #     result = []
    #     l = [0] * 26
    #     for i in range(len(p)):
    #         l[ord(p[i]) - ord('a')] += 1
    #     p = "".join([l[i] * chr(i + ord('a')) for i in range(len(l))])
    #     for i in range(len(s) - len(p) + 1):
    #         if self.match(s[i:i + len(p)], p):
    #             result.append(i)
    #     return result
    #
    # def match(self, item, sample):
    #     l = [0] * 26
    #     for i in range(len(item)):
    #         l[ord(item[i]) - ord('a')] += 1
    #     newitem = "".join([l[i] * chr(i + ord('a')) for i in range(len(l))])
    #     return sample == newitem

        if len(s) < len(p):
            return []
        samplewindow = [0] * 26  # create sample window
        for item in p:
            samplewindow[ord(item) - ord('a')] += 1

        result = []
        window = [0] * 26
        for i in range(len(p)):
            window[ord(s[i]) - ord('a')] += 1  # create first window
        i = 0
        while i <= len(s) - len(p):
            if window == samplewindow:
                result.append(i)
            # slice window
            window[ord(s[i]) - ord('a')] -= 1  # first position remove 1
            i += 1
            if i + len(p) - 1 < len(s):  # last position add 1
                window[ord(s[i + len(p) - 1]) - ord('a')] += 1
        return result

if __name__ == '__main__':
    answer = Solution()
    print answer.findAnagrams( "cbaebabacd", "abc")