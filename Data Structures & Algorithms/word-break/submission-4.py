class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means s[:i] can be break 
        # base case: dp[0] = true
        # trans: 
        # if s[j:i] in word and d[j]: dp[i] = True
        words = set(wordDict)
        dp = [0] * (len(s) + 1) 
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
            