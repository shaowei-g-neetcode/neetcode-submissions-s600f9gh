class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amount] = coin counts
        # dp[0] = 0


        dp = [float("inf")] * (amount + 1)  
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a-coin] + 1) 
        return dp[-1] if dp[-1] != float("inf") else -1