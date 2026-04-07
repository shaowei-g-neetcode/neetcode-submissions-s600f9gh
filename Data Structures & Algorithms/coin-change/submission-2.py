class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      # dp[i] = amount, the i th make up by amount coin.
      # dp[i] = min dp[amount-coin] + 1, dp[i]  for coin in coins
      # dp[0] = 0

      dp = [float("inf")] * (amount + 1)
      dp[0] = 0


      for a in range(1, amount + 1):
        for coin in coins:
          if  a - coin >= 0:
            dp[a] = min(dp[a - coin] + 1, dp[a])
      
      return dp[amount] if dp[amount] != float("inf") else -1