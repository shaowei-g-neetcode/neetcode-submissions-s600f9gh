class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]

        for i in range(1,len(nums)):
            n = nums[i]
            curr = max(n, curr + n)
            res = max(res, curr)
        
        return res