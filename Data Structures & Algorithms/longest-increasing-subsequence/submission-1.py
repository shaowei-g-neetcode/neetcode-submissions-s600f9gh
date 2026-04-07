class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

      # dp[i] = c , to last i, how many lits 
      # basecase dp[i] = 1
      n = len(nums)
      dp = [1] *  n

      for i in range(n):
        for j in range(i):
          if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])

      return max(dp)