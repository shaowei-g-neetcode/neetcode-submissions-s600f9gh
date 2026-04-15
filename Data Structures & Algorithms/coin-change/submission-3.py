class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state dp[i] = n means dp[i](amount) can make up by n coins
        # transition dp[amount] = dp[amount-coin] + 1 if amount-coin >= 0
        # base dp[i] = float("inf")

        dp = [float("inf")] * (amount+1) 
        dp[0] = 0

        for  a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1