class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use monotonic queue to save max
        # q[0] is always max

        q = deque()
        res = []

        for i in range(len(nums)):
            while q and i - k >= q[0]:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

            if i - k + 1 >= 0:
                res.append(nums[q[0]])

        return res


                
