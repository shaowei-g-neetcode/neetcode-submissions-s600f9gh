class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] means s[:i] has n ways to make up decoding
        # trans: 
        # single char: dp[i] += dp[i - 1]
        # two char:dp[i] += dp[i - 2]
        # base case dp[0] = 1, empty string
        n = len(s) + 1
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]