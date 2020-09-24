# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = res = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next

        h.next = l1 if l1 else l2
        return res.next