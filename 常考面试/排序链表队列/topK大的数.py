"""
leetcode 215
利用快排思路求解,
利用小根堆求解
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

"""
面试题 17.14. 最小K个数
"""

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def quickSort(arr, k):
            if len(arr) == 0:
                return arr

            pivot = arr[len(arr) >> 1]
            left, mid, right = [], [], []

            for x in arr:
                if x < pivot:
                    left.append(x)
                elif x == pivot:
                    mid.append(x)
                else:
                    right.append(x)

            if len(left) >= k:
                res = quickSort(left, k)
            elif len(left) + len(mid) >= k:
                res = left + mid[:k-len(left)]
            else:
                res = left + mid + quickSort(right, k - len(left) - len(mid))
            return res
        return quickSort(arr, k)

# 大根堆，小根堆
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        q = PriorityQueue()
        for x in arr:
            q.put_nowait(x)
        res = []
        for i in range(k):
            res.append(q.get_nowait())
        return res
