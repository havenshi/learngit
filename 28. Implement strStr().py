class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # # brute force
        # if needle == "":
        #     return 0
        # elif len(needle) <= len(haystack) and len(needle) > 0:
        #     for i in range(len(haystack)):
        #         if haystack[i] == needle[0]:
        #             for j in range(1, len(needle)):
        #                 if i + j <= len(haystack) - 1 and needle[j] == haystack[i + j]:
        #                     continue
        #                 else:
        #                     break
        #             else:
        #                 return i
        #     else:
        #         return -1
        # else:
        #     return -1

        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i + j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1

if __name__ == "__main__":
    answer=Solution()
    print answer.strStr("bbab","bab")
