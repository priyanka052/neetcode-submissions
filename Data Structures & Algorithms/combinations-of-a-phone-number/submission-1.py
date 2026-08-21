class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return []
        phone = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        def backtrack(start, path):
            if start >= len(digits):
                result.append(''.join(path))
                return
            #conditions
            latters = phone[digits[start]]
            for latter in latters :
                path.append(latter)
                backtrack(start+1, path)
                path.pop()
        backtrack(0, [])
        return result