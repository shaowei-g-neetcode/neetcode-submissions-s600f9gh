class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use bfs search
        # use queue
        # update 1 to 0 to prevent cycle
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    res += 1
                    grid[row][col] == '0'
                    q = deque([(row, col)])
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if not (0 <= nr < rows and 0<=nc<cols):
                                continue
                            if grid[nr][nc] != '1':
                                continue
                            grid[nr][nc] = '0'
                            q.append((nr, nc))
        return res

