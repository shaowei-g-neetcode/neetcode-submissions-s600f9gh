class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use sliding window to compare s1 need list and s2 window
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = [0] * 26
        window = [0] * 26

        def getAlphaInx(s:str):
            return ord(s) - ord('a')

        for i in range(m):
            need[getAlphaInx(s1[i])] += 1
            window[getAlphaInx(s2[i])] += 1

        if need == window:
            return True
        
        for right in range(m, n):
            window[getAlphaInx(s2[right])] += 1
            window[getAlphaInx(s2[right - m ])] -= 1

            if window == need:
                return True
        return False