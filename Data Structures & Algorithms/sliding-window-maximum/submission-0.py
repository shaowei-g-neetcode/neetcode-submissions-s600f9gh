class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use slide window and monotonic queue to save max num index
        q = deque()
        res = []

        for i, num in enumerate(nums):
            # i - k + 1 is left boundary
            # remove left num of left boundary
            while q and q[0] < i - k + 1:
                q.popleft()
            
            # pop num smaller then nums[i]
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)

            # append max num
            if i - k  + 1 >=0:
                res.append(nums[q[0]])

        return res