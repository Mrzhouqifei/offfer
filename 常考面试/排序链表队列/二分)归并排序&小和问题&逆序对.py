# # 归并排序是典型的二分分治排序
n = int(input())
nums = list(map(int, input().split()))

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    L = mergeSort(nums[:mid])
    R = mergeSort(nums[mid:])

    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
    return nums
nums = mergeSort(nums)

"""
面试题 17.08. 马戏团人塔
"""
#
# class Solution:
#     import bisect
#     def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
#        dp=[]
#        for a,b in sorted(zip(height,weight),key = lambda x:[x[0],-x[1]]):
#            pos = bisect.bisect_left(dp,b)
#            dp[pos:pos+1] = [b]
#        return len(dp)

class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        if not height: return 0
        length = len(height)
        actors = [(height[i], weight[i]) for i in range(length)]
        actors.sort(key=lambda x:(x[0], -x[1]))
        tail = [0] * length
        size = 0
        for actor in actors:
            i, j = 0, size
            while (i != j):
                mid = (i + j) // 2
                if tail[mid] < actor[1]: i = mid + 1
                else: j = mid
            tail[i] = actor[1]
            if i == size: size += 1
        return size


"""
小和问题
最简单易懂的方法，就是依次遍历数组每一个位置 i，然后再遍历一次找到 i 左边所有小于或者等于 s[i] 的数，累加即可。
该时间复杂度为O(N^2)。

二分分治法（一个数被计算了几次，右侧比他大的有几个数）
我们可以换一种思路考虑这个问题，对于每一个位置 i 的值s[i]，我们计算它比右边的几个数小或者等于，假设这样的数有 num 个，
那么在最后的小和中，s[i]提供的值的总和就是s[i] * num。显而易见，将每一个位置的 s[i] * num 加起来就是最终的小和。
使用归并排序的过程可以达到这个目的，试想，在归并排序的组间合并过程中，左右两组都已经有序。假设左组为left[]，右组为right[]，
并分别从位置 i 和 j 开始比较。如果left[i] <= right[j]，可以肯定right数组 j 位置右边的所有位置（假设有n个）
的值都一定比left[i]大或等于，所以会产生一个小和left[i] * n。当然这时的n不是原数组中所有在left[i]右边比left[i]大或等于的数，
因为left和right只是原数组中的两个子数组。整个归并过程该怎么进行就怎么进行，排序过程没有任何变化，
只是在组间合并的时候计算所有产生的小和并累加起来就是最终的结果。整个过程时间复杂度O(NlogN)。
"""


def smallSum(nums, l, r):
    # 求范围上的小和，在原数组上进行操作，不用切片
    if l == r:
        return 0
    # 负责递归的终止条件，并且是最后一层子函数的返回值
    mid = (l + r) >> 1  # l+r)//2
    # 注意 （l+r)//2 比 len/2 少1
    left_sum = smallSum(nums, l, mid)
    right_sum = smallSum(nums, mid + 1, r)
    all_sum = calculate_sum(nums, l, mid, r)
    # 没一个子函数都包括三部分
    # 头两个负责给第三个产生下标没并且接受三个相加的值
    # 后一个负责在merge的过程中利用外排计算小河，
    # 并且在原数组进行操作，姚旭中间的参数才能找到第二个数组的第一个
    return left_sum + right_sum + all_sum
    # 作为出最后一层外所有子函数层的返回值


def calculate_sum(nums, l, mid, r):
    # 负责在和的过程中进行榨取小和
    left = l
    right = mid + 1
    res = []
    sum = 0
    while left <= mid and right <= r:
        if nums[left] <= nums[right]:
            res.append(nums[left])
            sum += nums[left] * (r - right + 1)
            left += 1
        else:
            res.append(nums[right])
            right += 1
    # 把余下的复制过来，并且改变一下原有数组
    res += nums[left:mid + 1]
    res += nums[right:r + 1]
    for i in range(l, r + 1):
        nums[i] = res.pop(0)
    return sum


def get_smallSum(nums):
    # 主函数
    if not nums or len(nums) < 2:
        return 0
    return smallSum(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    li = [1, 3, 4, 2, 5]
    print(get_smallSum(li))


"""
剑指offer 51
数组重的逆序对
"""
class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)



"""
leetcode 315. 计算右侧小于当前元素的个数

求解「逆序对」的思想：当其中一个数字放进最终归并以后的有序数组中的时候，这个数字与之前看过的数字个数（或者是未看过的数字个数）可以直接统计出来，而不必一个一个数。这样排序完成以后，原数组的逆序数也就计算出来了；
具体来说，本题让我们求「在一个数组的某个元素的右边，比自己小的元素的个数」，因此，需要在「前有序数组」的元素归并的时候，数一数「后有序数组」已经归并回去的元素的个数，因为这些已经出列的元素都比当前出列的元素要（严格）小；
但是在「归并」的过程中，元素的位置会发生变化，因此下一步需要思考如何定位元素；根据「索引堆」的学习经验，一个元素在算法的执行过程中位置发生变化，我们还想定位它，可以使用「索引数组」，技巧在于：「原始数组」不变，用于比较两个元素的大小，真正位置变化的是「索引数组」的位置；
「索引数组」技巧建立了一个一一对应的关系，记录了当前操作的数对应的「原始数组」的下标，「索引数组」技巧想法的来源是「索引堆」（《算法（第 4 版）》第 2.4 节 练习）；
「归并排序」还需要一个用于归并的辅助数组，这个时候拷贝的就是索引数组的值了。
"""

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        temp = [None for _ in range(size)]
        res = [0 for _ in range(size)]
        # 索引数组，作用：归并回去的时候，方便知道是哪个下标的元素
        indexes = [i for i in range(size)]

        self.__merge_and_count_smaller(nums, 0, size - 1, temp, indexes, res)
        return res

    def __merge_and_count_smaller(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = left + (right - left) // 2
        self.__merge_and_count_smaller(nums, left, mid, temp, indexes, res)
        self.__merge_and_count_smaller(nums, mid + 1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # [left,mid] 前有序数组
        # [mid+1,right] 后有序数组

        # 先拷贝，再合并
        for i in range(left, right + 1):
            temp[i] = indexes[i]

        i = left
        j = mid + 1
        for k in range(left, right + 1):
            if i > mid:
                indexes[k] = temp[j]
                j += 1
            elif j > right:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (right - mid)
            elif nums[temp[i]] <= nums[temp[j]]:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (j - mid - 1)
            else:
                indexes[k] = temp[j]
                j += 1


if __name__ == '__main__':
    nums = [5, 2, 6, 1]
    solution = Solution()
    result = solution.countSmaller(nums)
    print(result)

