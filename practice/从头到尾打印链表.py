# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        # def search(node):
        #     if node:
        #         res.append(node.val)
        #         search(node.next)
        # search(listNode)

        head = listNode
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res
