class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowC, needC = {}, {}

        for i in range(len(t)):
            needC[t[i]] = needC.get(t[i], 0) + 1

        resIdx, resLen = -1, float("inf")

        have, need = 0, len(needC)
        l = 0

        for r in range(len(s)):
            rc = s[r]
            windowC[rc] = windowC.get(rc, 0) + 1

            if rc in needC and windowC[rc] == needC[rc]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    resIdx = l

                lc = s[l]
                windowC[lc] -= 1

                if lc in needC and windowC[lc] < needC[lc]:
                    have -= 1

                l += 1

        return s[resIdx: resIdx + resLen] if resIdx != -1 else ""