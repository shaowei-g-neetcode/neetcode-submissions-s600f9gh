class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amount] = counts
        # amount < 0, return amount + 1 (infinite)
        # loop, dp[amount] = min(dp[amount-coinV] + 1, )
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
          for coin in coins:
            if a - coin >= 0:
              dp[a] = min(dp[a], dp[a - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1    


