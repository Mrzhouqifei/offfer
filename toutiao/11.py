class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_value = 0
        while left != right:
            if height[left] < height[right]:
                tmp = height[left] * (right - left)
                left += 1
            else:
                tmp = height[right] * (right - left)
                right -= 1
            max_value = max(tmp, max_value)
        return max_value