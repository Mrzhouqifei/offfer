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
