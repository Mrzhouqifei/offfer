"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def zhongxu(node):
            if node:
                nonlocal first, last
                zhongxu(node.left)
                if last:
                    node.left = last
                    last.right = node
                else:
                    first = node
                last = node
                zhongxu(node.right)
        first, last = None, None
        zhongxu(root)
        first.left = last
        last.right = first
        return first
