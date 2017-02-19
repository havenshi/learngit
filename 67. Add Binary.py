class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alist = [int(i) for i in list(str(a))]
        blist = [int(i) for i in list(str(b))]

        lengtha = len(alist)
        lengthb = len(blist)
        if lengtha < lengthb:
            alist, blist = blist, alist
            lengtha, lengthb = lengthb, lengtha

        c=''
        carry = 0
        for i in range(lengthb):
            if alist[::-1][i] + blist[::-1][i] + carry >= 2:
                tmp = str(alist[::-1][i] + blist[::-1][i] + carry - 2)
                c += tmp
                carry = 1
            else:
                tmp = (alist[::-1][i] + blist[::-1][i] + carry)
                tmp = str(tmp)
                c += tmp
                carry = 0

        if carry == 1:
            for i in range(lengthb,lengtha):
                if alist[::-1][i] + carry == 2:
                    c += '0'
                    carry = 1
                else:
                    tmp = (alist[::-1][i] + carry)
                    tmp = str(tmp)
                    c += tmp
                    carry = 0
            if carry == 1:
                c += '1'

        else:
            for i in range(lengthb,lengtha):
                c += str(alist[::-1][i])

        return c[::-1]

if __name__ == "__main__":
    answer=Solution()
    print answer.addBinary('101111','10')
