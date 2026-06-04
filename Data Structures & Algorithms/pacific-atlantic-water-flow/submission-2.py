class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from boundary to search
        
        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(starts):
            reachable = set()
            stack = list(starts)
            print(starts, stack)

            for cell in stack:
                reachable.add(cell)

            while stack:
                r, c = stack.pop()     

                for dr, dc in directions:
                    nr, nc = r + dr , c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if (nr, nc) in reachable:
                        continue
                    if heights[nr][nc] >= heights[r][c]:
                        reachable.add((nr, nc)) 
                        stack.append((nr, nc))

            return reachable
        pacificStarts = []
        atlanticStarts = []

        for r in range(rows):
            pacificStarts.append((r, 0))
            atlanticStarts.append((r, cols - 1))
            
        for c in range(cols):
            pacificStarts.append((0, c))
            atlanticStarts.append((rows - 1, c))
        
        pacific = dfs(pacificStarts)
        atlantic = dfs(atlanticStarts)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        
        return res
            
