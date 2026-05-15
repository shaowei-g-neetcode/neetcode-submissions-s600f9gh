class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charCount = {}
        maxFreq = 0

        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r],0) + 1
            maxFreq = max(maxFreq, charCount[s[r]])
            windowLen = r - l + 1
            if windowLen <= maxFreq + k:
                res = max(res, windowLen)
            else:
                charCount[s[l]] -= 1
                l += 1
        
        return res
