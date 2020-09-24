# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.all_list = []

    def Insert(self, num):
        # write code here
        self.all_list.append(num)
        self.all_list.sort()

    def GetMedian(self, fuck):
        # write code here
        length = len(self.all_list)
        if length % 2 == 1:
            return self.all_list[length//2]
        else:
            return (self.all_list[length//2] + self.all_list[length//2-1]) / 2.0
