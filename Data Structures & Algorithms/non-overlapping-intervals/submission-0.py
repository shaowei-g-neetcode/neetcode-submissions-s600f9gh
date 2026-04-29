class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key = lambda interval: interval[1])
        preEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= preEnd:
                count += 1
                preEnd = end
        
        return len(intervals) - count