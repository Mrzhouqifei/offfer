"""
【题目】
给定数组arr和整数num，共返回有多少个子数组满足如下情况：子数组中的最大值减去最小值小于或等于num。
　　要求，时间复杂度O(N)。

【基本思路】
首先明确两点：
　　1、如果子数组arr[i…j]满足条件，那么arr[i…j]中的子数组一定也满足条件。
　　2、如果子数组arr[i…j]不满足条件，那么包含arr[i…j]的子数组一定也不满足条件。
使用两个双端队列qmin和qmax，qmin用来维护子数组arr[i…j]的最小值更新，qmax用来维护子数组arr[i…j]的最大值更新。
队头表示的就是子数组arr[i…j]的最小（大）值。生成两个整型变量i和j，用于表示子数组的范围，即arr[i…j]。
整型变量res表示所有满足条件的子数组数量。初始时，i、j、res都为0。
令j不断向右移动，表示arr[i…j]一直向右扩张，并不断更新qmin和qmax。
一旦出现arr[i…j]不满足条件的情况，扩张停止，此时arr[i…j-1]、arr[i…j-2]、arr[i…j-3]…arr[i…i]一定满足条件。
即所有必须以arr[i]开头的满足条件的子数组数量为j - i。所以令 res += j - i。
向右扩张停止后，令i向右移动一个单位，表示开始考虑以arr[i+1]开头的满足条件的子数组数量，更新qmin、qmax。接下来的过程和上述一样。
"""


def getNum(arr, num):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:  # i开头的遍历完了，跳出i
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    return res