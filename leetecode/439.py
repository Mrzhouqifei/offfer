class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        condition = 0
        for i in range(len(expression), -1, -1):
            if expression[i] == ':':
                continue
            elif expression[i] == '?':
                condition = 1
            else:
                if condition == 1:
                    if expression[i] == 'F':
                        stack.pop()
                    condition = 0
                else:
                    stack.append(expression[i])
        return stack[-1]

