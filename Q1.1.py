def judge(string):
    sample = [False] * 256
    for i in range(len(string)):
        if sample[ord(string[i])-ord('a')] == True:
            return False
        sample[ord(string[i]) - ord('a')] = True
    return True

print judge('abac')