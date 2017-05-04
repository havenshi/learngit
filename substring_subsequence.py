def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and string1[i + j] == string2[j]:
                match += string2[j]
            else:
                if len(match) > len(answer):
                    answer = match
                    break
    return answer

print longestSubstringFinder("apple pie available", "apple pies")


def subsequence(string1, string2):
    dp = [0 for i in range(len(string1))]
    flag = 0
    for i in range(len(string2)):
        for j in range(flag, len(string1)):
            if string2[i] == string1[j]:
                dp = dp[:j] + [item+1 for item in dp[j:]]
                flag = j + 1
                break
        print dp
    return dp[-1]

print subsequence('abcde', 'azbzdzczez')