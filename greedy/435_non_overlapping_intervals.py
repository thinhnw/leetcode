class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1])
        ans = 0
        current = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < current[1]:
                ans += 1
            else:
                current = intervals[i]
        return ans