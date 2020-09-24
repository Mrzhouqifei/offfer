class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == 'c':
                if len(stack) < 2 or not (stack.pop() == 'b' and stack.pop() == 'a'):
                    return False
            else:
                stack.append(x)
        if stack or len(s) < 3:
            return False
        else:
            return True