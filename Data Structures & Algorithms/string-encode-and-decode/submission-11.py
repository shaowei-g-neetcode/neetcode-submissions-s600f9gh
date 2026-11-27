class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            start = r + 1
            res.append(s[start:start+length])
            l = r = start + length
        return res
