# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        start = lower
        end = start
        while end < min(nums[-1],upper):
            while start in nums:
                start += 1
            end = start
            while end + 1 not in nums and end < upper:
                end += 1
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(end))
            start = end + 1
            end = start
        if nums[-1] < upper:
            res.append(str(nums[-1] + 1) + '->' + str(upper))
        return res
if __name__ == "__main__":
    print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)
    print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 60)