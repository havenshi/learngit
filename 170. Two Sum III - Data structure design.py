# Time:  O(n)
# Space: O(n)

# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

class TwoSum(object):
    def __init__(self):
        self.dic = {}

    def add(self, number):
        if number not in self.dic:
            self.dic[number] = 1
        else:
            self.dic[number] += 1

    def find(self, value):
        dic = self.dic
        for num in dic:
            if (value - num) in dic and (value - num != num or dic[num] > 1):
                return True
        return False