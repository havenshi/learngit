class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = " ".join(s.split())  # replace interval with only one space. Create a new array! can't use it!
        s = s + ' '  # if not add ' ', the last word can not be extracted
        for i in range(len(s)):
            if s[i] != " ":      # 1.find start which is not " "
                start = i
                break
        else:
            return ""

        for i in range(start + 1, len(s)):
            if s[i] == " ":
                end = i
                s = s[start:end+1] + s[:start] + s[end+1:]

                start = i + 1           # 2.find the next start which is not " "
                while start < len(s) and s[start] == " ":
                    start += 1

        s = s[:-1]   # remove the ' ' at the end of the s, it is with the original first word
        return s

if __name__ == '__main__':
    answer = Solution()
    print answer.reverseWords("the  sky  is blue")