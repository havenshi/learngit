# The password generated
from __future__ import print_function
a = 1
b = 7
x = 1
y = 4

list, ans, a = [], [], a%b
while (a, b) not in list:
    list.append((a, b))
    ans.append(a // b)
    a = (a % b)*10

nolooplen = list.index((a, b)) # when the iteration appears
looplen = len(ans) - nolooplen # how many after iteration

# print(list, ans, nolooplen, looplen)
for i in range(x, y + 1):
    if i < len(ans):
        print(ans[i], end='')
    else:
        print(ans[(i - nolooplen) % looplen + nolooplen], end='') # (remove first)%loop length+first
print('')