def answer(array):
    result = [i for i in array if i%3 ==0]
    list1 = [i for i in array if i % 3 == 1]
    list2 = [i for i in array if i % 3 == 2]
    list1.sort()
    list1.reverse()
    list2.sort()
    list2.reverse()

    result2 = []
    pair = min(len(list1),len(list2))
    result2 += list1[:pair] + list2[:pair]
    remaining1 = list1[pair:]
    remaining2 = list2[pair:]
    triple11 = len(remaining1) / 3 * 3
    triple22 = len(remaining2) / 3 * 3
    result2 += remaining1[:triple11] + remaining2[:triple22]


    triple1 = len(list1)/3
    newlist1 = list1[:triple1*3]
    result += newlist1
    remain1 = list1[triple1*3:]

    triple2 = len(list2) / 3
    newlist2 = list2[:triple2 * 3]
    result += newlist2
    remain2 = list1[triple2 * 3:]

    triple3 = min(len(remain1),len(remain2))
    result3 = remain1[:triple3] + remain2[:triple3]
    result += result3


    result.sort()
    result.reverse()
    answer = 0
    for i in (range(len(result))):
        answer = answer*10 + result[i]

    result2.sort()
    result2.reverse()
    answer2 = 0
    for i in (range(len(result2))):
        answer2 = answer2 * 10 + result2[i]

    return max(answer,answer2)


print answer([4,1,4,2,2])