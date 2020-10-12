"""
leetcode 215
利用快排思路求解
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSort(nums, k):
            pivot = nums[len(nums) // 2]
            left, mid, right = [], [], []

            for x in nums:
                if x < pivot:
                    left.append(x)
                elif x == pivot:
                    mid.append(x)
                else:
                    right.append(x)

            if len(left) >= k:
                res = quickSort(left, k)
            elif len(left) + len(mid) >= k:
                res = mid[0]
            else:
                res = quickSort(right, k - len(left) - len(mid))
            return res

        return quickSort(nums, len(nums) - k + 1)