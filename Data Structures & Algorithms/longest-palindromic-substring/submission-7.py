class Solution:
    def longestPalindrome(self, s: str) -> str:
      resIndex = 0
      resLen = 0

      n = len(s)
      
      for i in range(n):
        print(i)
        l, r = i , i
        while l >= 0 and r < n and s[l] == s[r]:
          print(l,r)
          if (r - l + 1) > resLen:
            resLen = r - l + 1
            resIndex = l
          r += 1
          l -= 1
          
        l, r = i , i + 1
        while l >= 0 and r < n and s[l] == s[r]:
          if (r - l + 1) > resLen:
            resLen = r - l + 1
            resIndex = l
          r += 1
          l -= 1
      return s[resIndex:resIndex + resLen]
        
          

