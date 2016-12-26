class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        lst_str = list(str.strip())
        sign = 1
        r_lst = []
        for i in lst_str:
            if i is '+':
                sign *= 1
            if i is '-':
                sign *= -1
            if i >= '0' and i <= '9':
                r_lst.append(i)
        if len(r_lst) == 0:
            return 0
        else:
            r_int = int(''.join(r_lst))
            r_int *= sign
        if r_int > (1 << 31) - 1 and r_int < (-1 << 31):
            return 0
        return r_int

    # def myAtoi(self, str):
    #     str = str.strip()
    #     if str == "":
    #         return 0
    #     i = 0
    #     sign = 1
    #     ret = 0
    #     length = len(str)
    #     MaxInt = (1 << 31) - 1
    #     if str[i] == '+':
    #         i += 1
    #     elif str[i] == '-':
    #         i += 1
    #         sign = -1
    #
    #     for i in range(i, length):
    #         if str[i] < '0' or str[i] > '9':
    #             break
    #         ret = ret * 10 + int(str[i])
    #         if ret > sys.maxint:
    #             break
    #     ret *= sign
    #     if ret >= MaxInt:
    #         return MaxInt
    #     if ret < MaxInt * -1:
    #         return MaxInt * - 1 - 1
    #     return ret

if __name__ == "__main__":
    answer = Solution()
    print answer.myAtoi("-123")