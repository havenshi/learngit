class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list

        # method 2
        # i=0
        # new=[]
        # while num>0:
        #     while i<len(values):
        #         if num>=values[i]:
        #             num-=values[i]
        #             new.append(numerals[i])
        #         else:
        #             i+=1
        # return new
if __name__ == "__main__":
    answer=Solution()
    print answer.intToRoman(1996)

