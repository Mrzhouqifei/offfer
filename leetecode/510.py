"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            next = node.right
            while next.left:
                next = next.left
            return next
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
