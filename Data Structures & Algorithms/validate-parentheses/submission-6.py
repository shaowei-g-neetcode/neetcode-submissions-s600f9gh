class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbolMap = {
          ')': '(',
          '}': '{',
          ']': '['
        }

        for c in s:
            if c in symbolMap:
                if symbolMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
                
        return True if not stack else False