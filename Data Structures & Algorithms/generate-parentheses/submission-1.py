class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path: str, left: int, right: int):
            if len(path) == 2 * n:
                res.append(path)
                return

            if left < n: 
                dfs(path + "(", left + 1, right)

            if right < left:
                dfs(path + ")", left, right + 1)

        dfs("", 0, 0)
        return res
