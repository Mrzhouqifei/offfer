"""
leetcode 116. 填充每个节点的下一个右侧节点指针

"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = []
        if root.left:
            q.append((root.left, 1))
        if root.right:
            q.append((root.right, 1))
        root.next = None
        pre, pre_index = root, 0
        while q:
            node, index = q.pop(0)
            if pre_index == index:
                pre.next = node
            else:
                pre.next = None
            pre, pre_index = node, index
            if node.left:
                q.append((node.left, index + 1))
            if node.right:
                q.append((node.right, index + 1))
        return root