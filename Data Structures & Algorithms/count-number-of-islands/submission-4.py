class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use bfs to search island
        # if rc is '1', count += 1 and start bfs
        # update rc to '0' to prevent rc searched twice
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] = '0'
                
                    # bfs
                    q = deque([(r,c)])

                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                q.append((nx, ny))
        return islands

