class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0

        charSet = set()
        while r < len(s):
            if s[r] in charSet:
                charSet = set()
                l = r
            else:
                charSet.add(s[r])
                res = max(res, len(charSet))
            r += 1
        return res