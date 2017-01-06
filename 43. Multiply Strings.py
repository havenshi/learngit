class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = list(num1)
        list2 = list(num2)

        int1 = 0
        for i in list1:
            int1 = int1 * 10 + (ord(i)-ord("0"))

        int2 = 0
        for j in list2:
            int2 = int2 * 10 + (ord(j) - ord("0"))

        return str(int1 * int2)

if __name__ == "__main__":
    answer=Solution()
    print answer.multiply("22","33")
