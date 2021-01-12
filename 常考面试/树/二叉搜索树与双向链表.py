"""
剑指offer 36
将二叉搜索树转换成一个排序的循环双向链表
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

"""
面试题 04.05. 合法二叉搜索树

实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

中序遍历 （从小到大）
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = float('-inf')

        def search(root):
            nonlocal inorder
            if not root:
                return True

            if not search(root.left):
                return False
            if root.val <= inorder:
                return False
            inorder = root.val
            if not search(root.right):
                return False
            return True

        return search(root)

