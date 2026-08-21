class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        dig1 = set()
        dig2 = set()
        board = [['.']*n for _ in range(n)]
        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols:
                    continue
                if row-col in dig1:
                    continue
                if row+col in dig2:
                    continue
                #chooseeee
                board[row][col] = 'Q'
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                
                #exploreeee
                backtrack(row+1)

                #undoooooooooooo
                board[row][col] = '.'
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        backtrack(0)
        return result