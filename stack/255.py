class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        curMax = -999999
        for x in preorder:
            if len(stack) > 0 and x > stack[-1]:
                curMax = stack.pop()
            elif x < curMax:
                return False
            else:
                stack.append(x)
        return True