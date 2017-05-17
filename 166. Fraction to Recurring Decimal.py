class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = 1
        if numerator * denominator < 0:
            flag = -1
            numerator = abs(numerator)
            denominator = abs(denominator)
        before = numerator/denominator
        remain = numerator - before * denominator
        if remain == 0:
            if flag == 1:
                return str(before)
            else:
                return '-' + str(before)
        else:
            after = []
            remain_array = [remain]
            while remain_array.count(remain) < 2:
                if remain == 0:
                    after = [str(x) for x in after]
                    if flag == 1:
                        return str(before) + '.' + ''.join(after)
                    else:
                        return '-' + str(before) + '.' + ''.join(after)
                remain *= 10
                quotient = remain / denominator
                after.append(quotient)
                remain -= quotient * denominator
                remain_array.append(remain)
            loop = remain_array.index(remain)
            after = [str(x) for x in after]
            if flag == 1:
                return str(before) + '.' + ''.join(after[:loop]) + '(' + ''.join(after[loop:len(after)]) + ')'
            if flag == -1:
                return '-' + str(before) + '.' + ''.join(after[:loop]) + '(' + ''.join(after[loop:len(after)]) + ')'
if __name__ == "__main__":
    print Solution().fractionToDecimal(1,-6)