class Solution:
    def reverseParentheses(self, s: str) -> str:
        # s = "(u(love)i)"
        stack = ['']
        for x in s:
            if x == '(':
                stack.append('')
            elif x == ')':
                stack[-2] += stack[-1][::-1]
            else:
                stack[-1] += x
        return stack[-1]