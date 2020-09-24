class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: return 0
        stack = []  # 单调减栈
        res = 0
        for i in range(n):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                res += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])
            stack.append(i)
        return res