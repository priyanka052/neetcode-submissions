import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x, y: x + y,
                     "-": lambda x,y: x - y,
                     "*": lambda x,y: x * y,
                     "/": lambda x,y: int(float(x) / y)}
        for token in tokens:
            if token in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                res = operators[token](n2, n1)
                stack.append(res)
                continue
            stack.append(int(token))
        return stack[0]