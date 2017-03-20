def answer(array):

    result = [i for i in array if i%3 ==0]   # i%3 ==0 means it's divisible by 3, append to result firstly
    list1 = [i for i in array if i % 3 == 1]
    list2 = [i for i in array if i % 3 == 2]
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    # then we try to find the longest len of array(from big to small), their sum should be divisible by 3

    # 1.result, first find (1,1,1) and (2,2,2) triple, then find (1,2)pair
    triple1 = len(list1)/3            # how many (1,1,1)triple
    result += list1[:len(list1)/3*3]  # append (1,1,1)triple to result
    remain1 = list1[triple1*3:]       # remain1
    triple2 = len(list2) / 3          # how many (2,2,2)triple
    result += list2[:triple2 * 3]     # append (2,2,2)triple to result
    remain2 = list2[triple2 * 3:]     # remain2
    pair12 = min(len(remain1),len(remain2))  # how many (1,2) pair do remain1 and remain1 have
    result += remain1[:pair12] + remain2[:pair12] # append (1,2) pair to result

    result2 = []  # 2.result2, first find find (1,2)pair, then (1,1,1) and (2,2,2) triple
    pair = min(len(list1),len(list2))
    result2 += list1[:pair] + list2[:pair]
    remaining1 = list1[pair:]
    remaining2 = list2[pair:]
    triple11 = len(remaining1) / 3 * 3
    triple22 = len(remaining2) / 3 * 3
    result2 += remaining1[:triple11] + remaining2[:triple22]


    result.sort(reverse=True)   # it's possible that current result is not in order
    answer = 0
    for i in (range(len(result))):
        answer = answer*10 + result[i]
    result2.sort(reverse=True)  # it's possible that current result2 is not in order
    answer2 = 0
    for i in (range(len(result2))):
        answer2 = answer2 * 10 + result2[i]

    return max(answer,answer2)   # compare result or result2 is greater


print answer([1,1,1,4,4,2,2])