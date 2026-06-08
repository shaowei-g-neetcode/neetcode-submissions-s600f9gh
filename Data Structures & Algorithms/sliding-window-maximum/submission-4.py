class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use monotonic queue to save max
        # q[0] is always max
        res = []
        q = deque()

        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)

            if i - k +  1 >= 0:
                res.append(nums[q[0]])
        
        return res

