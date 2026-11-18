class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        window = set()

        for r in range(len(s)):
            char = s[r]
            while char in window:
                window.remove(s[l])
                l += 1
               
            window.add(char)
            res = max(res, len(window))
        
        return res