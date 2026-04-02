class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # state: dp[i] mean the s[j:i] is wordDict
        # state change: dp[:j] = true， dp[j:i]
        # base case: dp[0] empty string, true
        # dp[len(s)+1] = true 
        n = len(s)
        dp = [False] * (n + 1)
        wordSet = set(wordDict)
        dp[0] = True

        for i in range(n+1):
          for j in range(i):
            if dp[j] == True and (s[j:i] in wordSet):
              dp[i] = True
        
        return dp[n]


