class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 9999999
        min_gap = 999999
        for i in range(n):
            left, right = 0, n-1
            while left < right:
                if left != i and right !=i:
                    sums = nums[i] + nums[left] + nums[right]
                    gap = abs(sums - target)
                    if gap < min_gap:
                        min_gap = gap
                        ans = sums
                    if sums == target:
                        return sums
                    elif sums < target:
                        left += 1
                    elif sums > target:
                        right -= 1
                elif left == i:
                    left += 1
                elif right == i:
                    right -= 1
        return ans
