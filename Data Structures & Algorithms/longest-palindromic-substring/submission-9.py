class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        # dp , s[i] = s[j] and i -j + 1 <=3 or d[i+1][j-1]
        n = len(s)
        dp = [ [False] * n for _ in range(n)]

        for i in range(n-1, -1, -1 ):
          for j in range(i, n):
            if s[i] == s[j] and (i+j<=2 or dp[i+1][j-1]):
              dp[i][j] = True
              if (i+j-1) > resLen:
                resIdx = i
                resLen = i+j-1
        return s[resIdx:resIdx+resLen]