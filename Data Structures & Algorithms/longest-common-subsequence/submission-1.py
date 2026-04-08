class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = res, i position in text1 and j position in text2.
        # basecase, empty string. dp[i][0] = 0, dp[0][j] = 0
        # if text1[i-1] == text2[j-1] then dp[i][j] = dp[i-1][j-1] + 1
        # else max(dp[i][j-1l, dp[i-1][j]])

        t1Len = len(text1)
        t2Len = len(text2)

        dp = [[0] * (t2Len + 1) for _ in range(t1Len + 1)]

        for i in range(1, t1Len + 1):
          for j in range(1, t2Len + 1):
            if text1[i-1] == text2[j-1]:
              dp[i][j] = dp[i-1][j-1] + 1
            else:
              dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[t1Len][t2Len]