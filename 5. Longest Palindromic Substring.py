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
        start1, start2, length1, length2 = 0, 0, 1, 1
        length, start= 1, 0
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                length1=2
                start1=i
                ss = min(len(s[:i + 1]), len(s[i + 1:]))
                a, b = 1, 1
                while a < ss:
                    if s[i - a] == s[i + 1 + a]:  # to the left 1 pace, to the right 1 pace
                        b += 1  # use b to calculate length
                        start1 = i + 1 - b  # start = left
                        length1 = b * 2  # length = from left to right
                    else:
                        break
                    a += 1  # use a to count

            if length1>length:
                length=length1
                start=start1
        return s[start:start + length]

    def longestodd(self, s):
        start1, start2, length1, length2 = 0, 0, 1, 1
        length, start = 1, 0
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                length2=3
                start2 = i
                ss = min(len(s[:i]), len(s[i + 1:]))
                a, b = 1, 0
                while a <= ss:
                    if s[i - a] == s[i + a]:
                        b += 1
                        start2 = i - b
                        length2 = b * 2 + 1
                    else:
                        break
                    a += 1

            if length2 > length:
                length = length2
                start = start2
        return s[start:start + length]


if __name__=="__main__":
    answer=Solution()
    s="cbbd"
    print answer.longestPalindrome(s)