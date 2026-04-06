class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMap = set(wordDict)

        # dp[i] , dp[:j] = true and dp[j:i] is word
        # dp[0] = False
        # dp[i] = 

        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i):
                w = s[j:i]
                if dp[j] and w in wordMap:
                    dp[i] = True
        return dp[i] 