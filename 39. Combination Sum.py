# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # method 1
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):  # 从前往后遍历，可以模拟不需要前几位元素的情况
            if target < candidates[i]:  # recursion时，仍然从序列的第i位开始，因为每个元素可以重复使用
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])

    # method 2
        self.result = []
        candidates.sort()
        for i in range(len(candidates)):
            self.recursive_comb([candidates[i]], candidates[i:], target)
        return self.result


    def recursive_comb(self, temp_array, rest_array, target):
        if sum(temp_array) == target:
            if temp_array not in self.result:
                self.result.append(temp_array)
        else:
            for i in range(len(rest_array)):
                temp_array2 = temp_array[:]
                temp_array2.append(rest_array[i])
                if sum(temp_array2) <= target:
                    self.recursive_comb(temp_array2, rest_array[i:], target)


if __name__ == "__main__":
    answer=Solution()
    print answer.combinationSum([2, 3, 6, 7], 7)
