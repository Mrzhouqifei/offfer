# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) == 0:
            return False
        for i in range(len(array)):
            if array[i][0] <= target and array[i][-1] >= target:
                for j in range(len(array[0])):
                    if array[i][j] == target:
                        return True
            if array[i][0] > target:
                break
        return False
