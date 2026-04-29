"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)

        rooms = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if rooms and rooms[0].end <= start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, interval.end)
        
        return len(rooms)
