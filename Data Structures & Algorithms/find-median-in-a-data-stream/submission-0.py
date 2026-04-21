class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        small, large = self.small, self.large

        heapq.heappush(small, -num)
        # make sure every num small is <= every num large
        if (small and large and -small[0] > large[0]):
          val = heapq.heappop(small)
          heapq.heappush(large, -val)
        
        # balance size
        if len(small) > len(large) + 1:
          val = heapq.heappop(small)
          heapq.heappush(large, -val)
        if len(large) > len(small) + 1:
          val = heapq.heappop(large)
          heapq.heappush(small, -val)

        

    def findMedian(self) -> float:
        small, large = self.small, self.large

        if len(small) > len(large):
          return -small[0]
        if len(large) > len(small):
          return large[0]
        return (-small[0] + large[0]) / 2
        