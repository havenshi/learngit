# Maximum continuous subsequence

L = [2, -3, 3, 50]

max_sum = 0
tmp = 0

for i in L:
    if(tmp > 0):
        tmp += i
    else:
        tmp = i
    max_sum = max(max_sum, tmp)

print max_sum


# my method
maxim=0
sum=0
for i in range(len(L)):
    if L[i]<0:
        maxim=max(sum,maxim)
        sum=0
    else:
        sum+=L[i]

print max(sum,maxim) # don't forget the last one