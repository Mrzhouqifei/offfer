# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        res = s.split(',')

        def deserialize(res):
            if len(res) == 0:
                return
            val = res.pop(0)
            root = None
            if val != '#':
                root = TreeNode(int(val))
                root.left = deserialize(res)
                root.right = deserialize(res)
            return root

        return deserialize(res)

