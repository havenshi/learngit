def anagrams(str1, str2):
    map = [0] * 256
    for i in range(len(str1)):
        map[ord(str1[i]) - ord('a')] += 1
    for j in range(len(str2)):
        map[ord(str2[j]) - ord('a')] -= 1
    return sum(map) == 0

print anagrams('abcd', 'b3cad')
