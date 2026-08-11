class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use two window to compare

        window = [0] * 26
        need = [0] * 26
    
        m, n = len(s1), len(s2)

        if m > n:
            return False


        def getCharIdx(s: str):
            return ord(s) - ord('a')

        for i in range(len(s1)):
            need[getCharIdx(s1[i])] += 1
            window[getCharIdx(s2[i])] += 1
        
        if need == window:
            return True
    

        for i in range(m, n):
            window[getCharIdx(s2[i])] += 1
            window[getCharIdx(s2[i - m])] -= 1

            if need == window:
                return True
            
        return False