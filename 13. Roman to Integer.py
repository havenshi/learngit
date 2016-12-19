class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        sum = 0
        s = s[::-1]
        while s != "":
            if s[:2][::-1] in numerals:
                sum += values[numerals.index(s[:2][::-1])]
                s = s[2:]
            elif s[:1] in numerals:
                sum += values[numerals.index(s[:1])]
                s = s[1:]
        return sum

if __name__ == "__main__":
    answer=Solution()
    print answer.romanToInt("MCMXCVI")

