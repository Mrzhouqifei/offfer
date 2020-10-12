"""
快慢指针
2m + 2a + 2sr =  m + a + fr
m = (f-s)r - a,从相遇点开始走正好在入口相遇
leetcode 面试题02.08
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
