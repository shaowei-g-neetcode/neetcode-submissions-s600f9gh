class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[m][n] = result
        # dp[m][0] = 1 dp[0][n] = 1
        # dp[m][n] = dp[m-1][n] + dp[m][n-1]

        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]

        return dp[-1]