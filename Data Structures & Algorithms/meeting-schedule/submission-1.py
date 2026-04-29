"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        preEnd = intervals[0].end
        for i in range(1, len(intervals)):
            preEnd = intervals[i - 1].end
            start = intervals[i].start
            if start < preEnd:
                return False

        return True
