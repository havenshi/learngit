# -*- coding:utf8 -*-
def longest(words):
    n = len(words)
    for i in range(n): # 按单词长度排列
        for j in range(1, n-i):
            if len(words[j-1]) > len(words[j]):
                words[j-1], words[j] = words[j], words[j-1]
    for i in range(n-1, -1, -1):
        if help(words[i], words[:i]+words[i+1:]): # 该单词可以由剩下的array组成
            return True
    return False

def help(word, array):
    n = len(word)
    result = [False] * (n + 1)
    result[n] = True
    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1):
            if result[j] and word[i:j - i] in array:
                result[i] = True
    return result[0]