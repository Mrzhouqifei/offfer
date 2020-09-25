# 剑指offer51 数组中的逆序对
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        if f:
            for i in range(1, len(nums)):
                tmp_num = 0
                for j in range(i):
                    if nums[j] > nums[i]:
                        tmp_num += 1
                f[i] = f[i-1] + tmp_num

            return f[len(nums)-1]
        else:
            return 0
        # 二叉搜索树与双向链表