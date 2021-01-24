"""
剑指 Offer 45. 把数组排成最小的数

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"
"""



class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 自定义排序
        nums_str = [str(x) for x in nums]

        def quick_sort(array):
            if len(array) <= 1:
                return array
            pivot = len(array) >> 1
            left, mid, right = [], [], []
            pivot_v = array[pivot]
            for x in array:
                if x + pivot_v < pivot_v + x:
                    left.append(x)
                elif x + pivot_v == pivot_v + x:
                    mid.append(x)
                else:
                    right.append(x)

            return quick_sort(left) + mid + quick_sort(right)

        nums_str = quick_sort(nums_str)
        res = ''
        for x in nums_str:
            res += x
        return res




