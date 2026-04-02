class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = lengthOfLIS's last ele 
        # res max(dp[1...i])
        # dp[i] = dp[j] + 1 for 
        # dp[i] = 1

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] :
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)