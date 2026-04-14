class Solution:
    def numDecodings(self, s: str) -> int:
        # state dp[i] = dp[i:] means there are how many ways there
        # basecase dp[n] = 1
        # transition single valid char: dp[i] += dp[i + 1]
        # twice valid char: dp[i] += dp[i + 2]
        n = len(s)

        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i + 1]
            if i + 1 < n  and '10' <= s[i:i+2] <= '26':
                dp[i] += dp[i + 2]

        return dp[0]
