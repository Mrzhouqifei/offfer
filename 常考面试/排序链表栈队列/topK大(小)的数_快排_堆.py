"""
leetcode 215  数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。
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

        return quickSort(nums, len(nums) - k + 1)   # 转化成第 len(nums) - k 小元素

"""
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
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
            q.put(x)
        res = []
        for i in range(k):
            res.append(q.get())
        return res
