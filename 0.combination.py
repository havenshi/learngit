# method 1
def combination(arry,n):
    total=[]
    for i in range(1,n+1):
        total+=combination_each(arry,i)
    return total

def combination_each(arry,n):
    result=[]
    if n==1:
        for i in range(len(arry)):
            result.append([arry[i]])
    else:
        for item in combination_each(arry,n-1):
            end=arry.index(item[-1])
            for i in arry[end+1:]:
                result.append(item+[i])
    return result

print combination([1,2,3],3)



# method 2
answer = []

def combination(array, n):
    for i in range(len(array)):
        recursive_comb([array[i]], array[i+1:], n)


def recursive_comb(temp_array, rest_array, n):
    if len(temp_array) == n:
        answer.append(temp_array)
    else:
        for i in range(len(rest_array)):
            temp_array2 = temp_array[:]    # must copy the temp, temp will change in this for loop
            temp_array2.append(rest_array[i])
            recursive_comb(temp_array2, rest_array[i+1:], n)


combination([1,2,3],2)
print answer