class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp1 = dp[i+1]、dp2 = dp[i+2]
        dp1 = 1
        dp2 = 2

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                current = 0