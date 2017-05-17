class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(numbers)):
            if numbers[i] in m:
                return [m[numbers[i]]+1, i+1]
            else:
                m[target - numbers[i]] = i