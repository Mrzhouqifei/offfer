# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        start = 0
        end = start + size
        max_list = []
        if len(num) < size or size==0:
            return []
        while(end<=len(num)):
            max_list.append(max(num[start:end]))
            start = start + 1
            end = end + 1
        return  max_list

