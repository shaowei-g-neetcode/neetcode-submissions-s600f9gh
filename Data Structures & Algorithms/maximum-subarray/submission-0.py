class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1]+dp[i], dp[i])

        cur = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cur = max(cur+nums[i], nums[i])

            res = max(res, cur)

        return res