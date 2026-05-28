class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use slideingwindow and monotonic queue to get max value in a window
        q = deque()
        res = []

        for i in range(len(nums)):
            # remove left index
            while q and q[0] < i - k + 1:
                q.popleft()
            
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

            if i - k + 1 >= 0:
                res.append(nums[q[0]])
        
        return res 

