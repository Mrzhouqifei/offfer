"""
面试题 02.04. 分割链表
"""

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        flag = False
        p = head
        pre = None
        while p:
            if not flag and p.val >= x:
                    flag = True
                    pre = p
                    p = p.next
            elif flag and p.val < x:
                pre.next = p.next
                p.next = head
                head = p
                p = pre.next
            else:
                pre = p
                p = p.next
        return head