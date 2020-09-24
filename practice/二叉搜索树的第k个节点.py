# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or not k:
            return
        # write code here
        array = []
        def search(node):
            if len(array) >= k or not node:
                return
            search(node.left)
            array.append(node)
            search(node.right)
        search(pRoot)
        if len(array) >= k:
            return array[k-1]
        return
