def answer(array):
    result = [i for i in array if i%3 ==0]
    list1 = [i for i in array if i % 3 == 1]
    list2 = [i for i in array if i % 3 == 2]

    list1.sort()
    triple1 = len(list1)/3
    newlist1 = list1[:triple1*3]
    result += newlist1
    remain1 = list1[triple1*3:]

    list2.sort()
    triple2 = len(list2) / 3
    newlist2 = list2[:triple2 * 3]
    result += newlist2
    remain2 = list1[triple2 * 3:]

    triple3 = min(len(remain1),len(remain2))
    result3 = remain1[:triple3] + remain2[:triple3]
    result += result3

    result.sort()
    answer = 0
    for i in (range(len(result))):
        answer = answer*10 + result[::-1][i]
    return answer


print answer([4,1,4])