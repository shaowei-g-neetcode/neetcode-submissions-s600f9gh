class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means the dp[j:i] is in wordDict
        # transition dp[i] = s[j:i] in wordDict
        # if s[i] = true and s[i:] is in wordDict, res = true
        # base dp[i] = false
        wordSet = set(wordDict)
        dp = [False] * len(s)

        for i in range(len(s)):
            for j in range(i):
                if s[j:i] in wordSet:
                    dp[i] = True
                    if s[i:] in wordSet:
                        return True
        return False

