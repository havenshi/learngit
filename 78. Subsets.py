class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total = [[]]
        for i in range(1, len(nums) + 1):
            total += self.subsets_each(nums, i)
        return total

    def subsets_each(self, arry, n):
        result = []
        if n == 1:
            for i in range(len(arry)):
                result.append([arry[i]])
        else:
            for item in self.subsets_each(arry, n - 1):
                end = arry.index(item[-1])
                for i in arry[end + 1:]:
                    result.append(item + [i])
        return result