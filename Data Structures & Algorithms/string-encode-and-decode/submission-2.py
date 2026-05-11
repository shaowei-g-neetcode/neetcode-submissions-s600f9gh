class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        lenS = ''
        while i < len(s):
            c = s[i]
            if c== '#':
                length = int(lenS)
                i += 1
                res.append(s[i:i+length])
                i += length
                lenS = ''
            else:
                lenS += c
                i += 1
        return res