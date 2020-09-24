# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.array = []

    def push(self, node):
        # write code here
        self.array.append(node)
    def pop(self):
        # return xx

        return self.array.pop(0)