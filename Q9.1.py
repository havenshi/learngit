def merge(a, b): # O(m+n), no addition space
    while b:
        bitem = b.pop()
        a.append(bitem)
        for i in range(len(a) - 1, -1, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
            else:
                break
    return a

# def merge2(a, b): # O(m+n), no addition space. java的指针方法
#     i = len(a) - 1
#     j = len(b) - 1
#     k = i + j - 1
#     while i >= 0 and j >= 0:
#         if a[i] > b[j]:
#             a[k] = a[i]
#             i -= 1
#         else:
#             a[k] = b[i]
#             j -= 1
#         k -= 1

print merge([1,2,4,5,7,8,10], [3,6,9])