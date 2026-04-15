class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means dp[:i] can be break
        # transitions dp[i] = dp[j] and dp[j:i] in wordDict
        # if dp[:i] and dp[i:] in wordDict, res = true
        # base dp[0] = true empty string

        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return  dp[-1]

