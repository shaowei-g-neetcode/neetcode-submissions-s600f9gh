class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use two count windowC and needC
        # windowC save char counts in s, needC save char counts in t
        # use have, need 
        # need means how many chars should satisified
        # have means windowC[c] satisify needC[c]

        if t == "":
            return ""

        windowC, needC = {}, {}
        window = []

        for c in t:
            needC[c] =  needC.get(c, 0) + 1
            
        l = 0
        have, need = 0, len(needC)
        resLen, resIdx = float("inf"), -1
        for r in range(len(s)):
            windowC[s[r]] = windowC.get(s[r], 0) + 1
            if s[r] in needC and windowC[s[r]] == needC[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    resIdx = l

                windowC[s[l]] -= 1

                if s[l] in needC and windowC[s[l]] < needC[s[l]]:
                    have -= 1
                l += 1 
        return s[resIdx: resIdx + resLen] if resIdx != -1 else ""
            


