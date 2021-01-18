# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤m≤n≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        reverse_m = head
        i = 1

        while i < m:
            reverse_m = reverse_m.next
            i += 1

        pre, p = None, reverse_m
        while i <= n:
            next_tmp = p.next
            p.next = pre
            pre = p
            p = next_tmp
            i += 1

        reverse_m.next = p
        new_head = pre

        if m == 1:
            return new_head
        else:
            i = 1
            p = head
            while i < m - 1:
                p = p.next
                i += 1
            p.next = new_head
            return head