#-*- coding:utf8 -*-
def removedup(string): # 不可以开数组
    for i in range(len(string)):
        j = i + 1
        while j < len(string):
            if string[j] == string[i]:
                if j + 1 < len(string):
                    string = string[:j] + string[j+1:]
                else:
                    string = string[:j]
                continue
            j += 1
    return string

def removedup2(string):  # 可以开一个固定大小，与问题规模(即字符串长度)无关的数组
    flag = []
    for i in range(len(string)):
        if string[i] in flag:
            continue
        flag.append(string[i])
    return ''.join(flag)


print removedup('abcdabcdcba')
print removedup2('abcdabcdcba')
