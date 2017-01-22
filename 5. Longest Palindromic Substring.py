class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(self.longesteven(s)) > len(self.longestodd(s)):
            return self.longesteven(s)
        else:
            return self.longestodd(s)

    def longesteven(self, s):
        start1, length1 = 0, 1
        start, length = 0, 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                length1 = 2
                start1 = i
                ss = min(len(s[:i + 1]), len(s[i + 1:]))
                a = 1
                while a < ss:
                    if s[i - a] == s[i + 1 + a]:  # to the left 1 pace, to the right 1 pace
                        start1 = i - a  # start = left
                        length1 = i + 1 + a - (i - a) + 1
                    else:
                        break
                    a += 1  # use a to count

            if length1 > length:
                length = length1
                start = start1
        return s[start:start + length]

    def longestodd(self, s):
        start2, length2 = 0, 1
        start, length = 0, 1
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                length2 = 3
                start2 = i - 1
                ss = min(len(s[:i]), len(s[i + 1:]))
                a = 1
                while a < ss:
                    if s[i - 1 - a] == s[i + 1 + a]:
                        start2 = i - 1 - a
                        length2 = i + 1 + a - (i - 1 - a) + 1
                    else:
                        break
                    a += 1

            if length2 > length:
                length = length2
                start = start2
        return s[start:start + length]


if __name__=="__main__":
    answer=Solution()
    s="ccc"
    print answer.longestPalindrome(s)