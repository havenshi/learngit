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
        digit = 1
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
        return r_int