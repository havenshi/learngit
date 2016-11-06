# Maximum not continuous subsequence

L = [2, -3, 3, 50]

for i in range(2,len(L)):
    L[i]=(max(max(L[0:i-1]),0)+L[i])

print max(L)