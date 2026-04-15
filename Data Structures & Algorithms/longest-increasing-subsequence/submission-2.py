class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] the lis length end with nums[i]
        # use i , j. i = curr num, j = previous num 
        # trans nums[j] < nums[i] then dp[i] = max(dp[j] + 1, dp[i])
        # base dp[i] = 1

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return dp[-1]