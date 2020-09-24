class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '[' or x =='{':
                stack.append(x)
            elif len(stack) > 0:
                y = stack.pop()
                if not ((x == ')' and y =='(') or (x == ']' and y =='[') or (x == '}' and y =='{') ):
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
