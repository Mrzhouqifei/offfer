# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        res = set()
        while head:
            l1 = len(res)
            res.add(head)
            l2 = len(res)
            if l1 == l2:
                return True
            head = head.next
        return False