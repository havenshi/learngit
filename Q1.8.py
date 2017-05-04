def isSubstring(str1, str2):
    return str2 in str1

def rotation(str1, str2):
    return isSubstring(str1+str1, str2)

print rotation('erbottlewat', 'waterbottle')