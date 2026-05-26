class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use two window need and window to compare
        # becasue question give lowercase alphabet
        # we can use list to count
        m, n = len(s1), len(s2)
        if m > n:
            return False
        need = [0] * 26
        window = [0] * 26

        def getCharIdx(s: str):
            return ord(s) - ord('a')

        for i in range(m):
            need[getCharIdx(s1[i])] += 1
            window[getCharIdx(s2[i])] += 1
        
        if need == window:
            return True
        
        for right in range(m, n):
            window[getCharIdx(s2[right])] += 1
            window[getCharIdx(s2[right - m])] -= 1
            if need == window:
                return True
        return False