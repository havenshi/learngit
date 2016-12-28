class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if target >0:
            if target in candidates:
                return [target]
            else:
                if target>=candidates[-1]:
                    list1=self.combinationSum2(candidates[:len(candidates)-1],(target-candidates[-1])).append(candidates[-1])
                    list2 = self.combinationSum2(candidates[:len(candidates) - 1], (target))
                    return [list1]+[list2]

if __name__ == "__main__":
    answer=Solution()
    print answer.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
