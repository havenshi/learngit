# Back to the longest text string is not simple

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         long=""
#         temp=""
#         i=0
#         gap = 2
#         gap2=1
#
#         if len(s)==1:
#             return s
#
#         while i < len(s)-gap:
#             if s[i] == s[i+gap]:
#                 temp=s[i:i+gap+1]
#                 ii=i
#                 ii-=1
#                 gap+=2
#
#                 while 0<=ii<len(s)-gap and s[ii] == s[ii+gap]:
#                     temp=s[ii:ii+gap+1]
#                     ii -= 1
#                     gap += 2
#
#                 if len(long)<len(temp):
#                     long=temp
#
#                 temp=""
#                 i=i+1
#                 gap=2
#
#             else:
#                 i+=1
#
#         i=0
#
#         while i < len(s) - gap2:
#             if s[i] == s[i+gap2]:
#                 temp=s[i:i+gap2+1]
#                 ii=i
#                 ii-=1
#                 gap2+=2
#
#                 while 0<=ii<len(s)-gap2 and s[ii] == s[ii+gap2]:
#                     temp=s[ii:ii+gap2+1]
#                     ii -= 1
#                     gap2 += 2
#
#                 if len(long)<len(temp):
#                     long=temp
#
#                 temp=""
#                 i=i+1
#                 gap2 = 1
#
#             else:
#                 i+=1
#
#         temp=s[0]
#         if len(long) < len(temp):
#             long = temp
#
#         return long
#
# if __name__ == "__main__":
#     answer = Solution()
#     print answer.longestPalindrome(L)


L = "caayyhheehhbbbhhjhhyyaac"
start, length = 0, 0
for i in range(1,len(L)-1):
    if L[i] == L[i+1]:
        s = min(len(L[:i+1]),len(L[i+1:]))
        a, b = 1, 1
        while a < s:
            if L[i-a] == L[i+1+a]:      # to the left 1 pace, to the right 1 pace
                b += 1                  # use b to calculate length
                if b*2 > length:
                    start = i + 1 - b   # start = left
                    length = b * 2      # length = from left to right
            else:
                break
            a += 1                      # use a to count

    if L[i-1] == L[i+1]:
        s = min(len(L[:i]),len(L[i+1:]))
        a, b = 1, 0
        while a <= s:
            if L[i-a] == L[i+a]:
                b += 1
                if (b*2)+1 > length:
                    start = i - b
                    length = b * 2 + 1
            else:
                break
            a += 1
print L[start:start+length]