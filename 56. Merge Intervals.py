# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort() # sort, firstly sort start, then end, example [2,19],[15,18]

        if len(intervals)<=1:
            return intervals if len(intervals)==1 else []

        l=[intervals[0]]
        for key,val in enumerate(intervals[1:]):
            if l[-1].end < val.start:
                l.append(val)
            else:
                l[-1].end=max(l[-1].end,val.end)
        return l


if __name__ == "__main__":
    answer=Solution()
    print answer.merge([Interval(1,4),Interval(2,5)])