# Gas Station

limit = [1,2,3,4]
cost = [4,2,1,3]

sum = 0
subsum = 0
ix = 0
for i in range(len(limit)):
    delta = limit[i] - cost[i]
    sum += delta
    subsum += delta

    if subsum < 0:
        ix = i + 1
        subsum = 0

if sum<0:
    print -1
else:
    print ix

