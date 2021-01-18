# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 栈的压入弹出序列

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        p = head
        # 先记录下一个，在将这一个的连接到前面，跟新前面，跟新当前
        while p:
            next = p.next
            p.next = pre
            pre = p
            p = next
        return pre