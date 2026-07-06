class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means s[j:i] in words
        # trans: dp[j] == true and s[j:i] in words
        # dp[0] = true

        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        words = set(wordDict)

        for i in range(1, n):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
