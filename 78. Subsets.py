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

    # jiuzhang
    # def search(self, nums, S, index):
    #     if index == len(nums):
    #         self.results.append(S)
    #         return
    #
    #     self.search(nums, S + [nums[index]], index + 1)
    #     self.search(nums, S, index + 1)
    #
    # def subsets(self, nums):
    #     self.results = []
    #     self.search(sorted(nums), [], 0)
    #     return self.results