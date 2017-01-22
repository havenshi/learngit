class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False

        list = []
        l = ["(", "[", "{"]
        n = [")", "]", "}"]
        issy = True

        i = 0
        while i < len(s) and issy:
            if s[i] in l:
                list.append(s[i])
            elif len(list) != 0:
                firsti = list[-1]
                if l.index(firsti) == n.index(s[i]):
                    del list[-1]
                else:
                    issy = False
            else:
                issy = False

            i += 1

        if len(list) != 0:
            issy = False

        return issy

if __name__ == "__main__":
    s = "([})"
    answer = Solution()
    print answer.isValid(s)


# from pythonds.basic.stack import Stack
#
# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in "([{":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top,symbol):
#                        balanced = False
#         index = index + 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
# def matches(open,close):
#     opens = "([{"
#     closers = ")]}"
#     return opens.index(open) == closers.index(close)
#
#
# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))
