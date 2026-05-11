class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countsS, countsT = {}, {}

        for i in range(len(s)):
            countsS[s[i]] = 1 + countsS.get(s[i], 0)
            countsT[t[i]] = 1 + countsT.get(t[i], 0)
        
        for key, val in countsS.items():
            if countsS[key] != countsT.get(key, 0):
                return False
        return True

