# The password generated

a = 1
b = 77
x = 1
y = 14

lister, ans, a = [], [], a%b
while a not in lister:
    lister.append(a)        # 1. already includes x of x.123456
    ans.append(a // b)
    a = (a % b)*10

nolooplen = lister.index(a) # when the iteration appears in ans
looplen = len(ans) - nolooplen # how many after iteration

print(lister, ans, nolooplen, looplen)
code=''
for i in range(x, y + 1):       # 2. no need to minus 1 from (x, y+1)
    if i in range(len(ans)):
        code += str(ans[i])
    elif (i - (nolooplen-1)) % looplen !=0:
        code += str(ans[(i - (nolooplen-1)) % looplen]) # (remove first)%loop length+first
    else:
        code += str(ans[-1])
print(code)


# my method
a = 1
b = 77
x = 1
y = 14

lister, ans, a = [], [], a%b*10
while a not in lister:
    lister.append(a)        # 1. not includes x of x.123456
    ans.append(a // b)
    a = (a % b)*10

nolooplen = lister.index(a) # when the iteration appears in ans
looplen = len(ans) - nolooplen # how many after iteration

print(lister, ans, nolooplen, looplen)
code=''
for i in range(x-1, y):       # 2. minus 1 from (x, y+1)
    if i in range(len(ans)):
        code += str(ans[i])
    else:
        code += str(ans[(i - nolooplen) % looplen]) # (remove first)%loop length+first

print(code)