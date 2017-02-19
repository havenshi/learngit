class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        l = list(range(1, n + 1))
        for i in range(n):
            self.createcombine([l[i]],l[i+1:],k)
        return self.result

    def createcombine(self, pre, cur, k):
        if len(pre) == k and pre not in self.result:
            self.result.append(pre)
        else:
            for i in range(len(cur)):
                copypre = pre[:] + [cur[i]]
                self.createcombine(copypre, cur[i+1:], k)

        # method2
        # if k == 0:
        #     return [[]]
        # return [pre + [i] for i in range(1, n + 1) for pre in self.combine(i - 1, k - 1)]

        # method3
        # from itertools import combinations
        # return list(combinations(range(1, n + 1), k))

if __name__ == "__main__":
    answer=Solution()
    print answer.combine(20,16)
