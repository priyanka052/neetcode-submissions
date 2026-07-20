class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for c in s:
            if c in openToClose:
                if stack and stack[-1] == openToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack