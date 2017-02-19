class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        reverse_digits = digits[::-1]
        if reverse_digits[0] + 1 != 10:
            reverse_digits[0] += 1
            return reverse_digits[::-1]
        else:
            carry = 1
            for pos, val in enumerate(reverse_digits):
                if val + carry == 10:
                    reverse_digits[pos] = 0
                    carry = 1
                else:
                    reverse_digits[pos] = val + carry
                    carry = 0
                    break
            if carry == 1:
                reverse_digits.append(1)
            return reverse_digits[::-1]

if __name__ == "__main__":
    answer=Solution()
    print answer.plusOne([1,2,9,9])
