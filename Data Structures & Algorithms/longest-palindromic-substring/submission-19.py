class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand around center
        # use two pointer expand from i index
        # two ways to reslove odd and even char
        resIndex = 0
        resLen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIndex = l
                r += 1
                l -= 1
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIndex = l
                r += 1
                l -= 1
        return s[resIndex:resIndex+resLen]