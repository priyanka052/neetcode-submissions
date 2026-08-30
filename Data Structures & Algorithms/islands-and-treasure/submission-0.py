class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
    #put treasures in to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
    #Multi-Source Queue
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))