class Solution:

    def encode(self, strs: List[str]) -> str:
      res = []
      
      for st in strs:
        length = len(st)
        res.append(str(length) + '#' + st)

      return ''.join(res)

    def decode(self, s: str) -> List[str]:
      res = []
      i = 0

      while i < len(s):
        if s[i] != '#':
          i += 1
          continue
        length = int(s[i-1])
        res.append(s[i+1:i+length+1])
        i += length + 1
      return res
        

        
      
        
