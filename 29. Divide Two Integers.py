class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX=(1<<31)-1
        if divisor==0:
            return INT_MAX
        else:
            symbol = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
            count=0
            shift=31
            dividend,divisor=abs(dividend),abs(divisor)
            while shift>=0:
                while dividend>=divisor<< shift:
                    count+=1<< shift
                    dividend-=divisor<< shift
                shift-=1
            if symbol:
                return -count
            elif count > INT_MAX:
                return INT_MAX
            else:
                return count
if __name__ == "__main__":
    answer=Solution()
    print answer.divide(0,1)
