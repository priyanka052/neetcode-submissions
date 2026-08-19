class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(path, open, close):
            #base case
            if len(path) == 2*n:
                result.append(''.join(path[:]))
                return
            
            if open < n:
                path.append('(')
                backtrack(path, open+1, close)
                path.pop()
            if close < open:
                path.append(')')
                backtrack(path,open, close+1)
                path.pop()
        backtrack([], 0, 0)
        return result