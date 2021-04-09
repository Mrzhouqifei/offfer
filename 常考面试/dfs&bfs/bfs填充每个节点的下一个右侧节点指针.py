"""
leetcode 116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = [(root, 0)]
        pre, pre_index = None, -1
        while q:
            node, index = q.pop(0)
            if index == pre_index:
                pre.next = node
            else:
                pre_index = index
            if node.left:
                q.append((node.left, index+1))
            if node.right:
                q.append((node.right, index+1))
            pre = node
        return root
