class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] means how many ways can decode s[:i]
        # trans: 
        # single char: dp[i] += dp[i-1]
        # two char: dp[i] += dp[i-2]
        # base: dp[0] = 1 , empty string = 1 way
        n = len(s) + 1
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]