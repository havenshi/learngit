# The arrangement of the god

N=1000
# god=0
# for n in range(1,N+1):
#     godn=0
#     for m in range(2,n):
#         if m*(m-1)*2==n*(n-1):
#             godn+=1
#             print m,n
#     god+=godn
# print god                  # timeout


# find if n*(n-1)/2 can be separated into two adjacent numbers
def adjacent(num):
    a=round(num**(1/2.0),0)
    if a*(a+1)==num:
        return True

god_num = 0
for n in range(2,N+1):
    if adjacent(n*(n-1)/2):
        god_num+=1
        print n
print(god_num)


# L = [[5,1],[17,3]]
# L1 = [4,21,120]
# #N = 1000
# if N < 4:
#     print 0
# elif N>=4 and N<21:
#     print 1
# else:
#     while L1[-1]<N:
#         L.append([L[-2][-2]*6-L[-2][-1],L[-2][-2]])
#         L1.append(L1[-1]*L[-1][0]/L[-1][1]+1)
#     print len(L1) if L1[-1]<=N else len(L1)-1
# other's code which could pass