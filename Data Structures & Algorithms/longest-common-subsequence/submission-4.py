class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] i = text position , j = text2
        # dp[i][j] mean text before text1 i and text2 j common subsequence
        #  dp[i][j] = dp[i+1][j-1] if i == j else max(dp[i][j-1], dp[i+1][j])
        # basecase: dp[i][0] = 0  dp[0][j] = 0, empty string


        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 

        return dp[len(text1)][len(text2)]