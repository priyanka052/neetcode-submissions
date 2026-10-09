class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return 
            board[r][c] = 'S'

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
            