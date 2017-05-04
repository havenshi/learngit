class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.minv = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if len(self.nums) == 1:
            self.minv.append(x)
        else:
            newmin = min(self.minv[-1], x)
            self.minv.append(newmin)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.nums) > 0:
            del self.nums[-1]
            del self.minv[-1]
        else:
            pass

    def top(self):
        """
        :rtype: int
        """
        if len(self.nums) > 0:
            return self.nums[-1]
        else:
            pass

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.nums) > 0:
            return self.minv[-1]
        else:
            pass

if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    obj.getMin()
    obj.pop()
    obj.getMin()
    obj.pop()
    obj.getMin()
    obj.pop()
    obj.getMin()