class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp1 = dp[i+1]、dp2 = dp[i+2]
        dp1 = 1
        dp2 = 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                current = 0
            
            else: 
                current = dp1
                
                if ( i + 1 < n and (s[i] == '1' or (s[i] =='2' and (s[i+1] <= '6')))):
                    current += dp2
            dp2 = dp1
            dp1 = current
        
        return dp1
            