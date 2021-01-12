"""
leetcode 面试题02.08 环路检测
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。

快慢指针
m: 链表起点到环路开头
a: 环路开头到快慢指针相遇点
c: 环路长度
s: 慢指针进行了几次环路
f: 快指针进行了几次环路
2m + 2a + 2sc =  m + a + fc
m + a = (f-s)c, 从相遇点开始走正好在入口相遇
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head  # 相遇的节点
        return None
