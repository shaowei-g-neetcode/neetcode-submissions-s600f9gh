class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from boundary to search
        rows, cols = len(heights), len(heights[0])

        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        
        
        def dfs(starts):
            stack = list(starts)
            reachable = set()

            for cell in starts:
                reachable.add(cell)

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr , c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and  (nr,nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                        reachable.add((nr, nc))
                        stack.append((nr, nc))
            return reachable
        
        pStarts, aStarts = [], []
        for r in range(rows):
            pStarts.append((r, 0))
            aStarts.append((r, cols - 1))
        for c in range(cols):
            pStarts.append((0, c))
            aStarts.append((rows-1, c))

        p = dfs(pStarts)
        a = dfs(aStarts)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in p and (r,c) in a:
                    res.append([r, c])

        return res
