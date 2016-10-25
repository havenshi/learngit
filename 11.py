#The number of end 0

def count(num,i):
    if num==0:
        return 0
    if num%i==0:
        return 1+count(num/i,i)
    else:
        return 0

def countzero(list):
    count2=0
    count5=0
    for i in range(len(list)):
        count2 += count(list[i], 2)
        count5 += count(list[i], 5)

    if count2>count5:
        return count5
    else:
        return count2

print countzero([2,8,3,50])