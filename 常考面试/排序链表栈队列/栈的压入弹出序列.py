# 剑指offer31
# 判断popped是否是pushed的一个弹出序列
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for x in pushed:
            stack.append(x)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

