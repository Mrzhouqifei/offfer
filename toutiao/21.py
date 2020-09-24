# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p = l1
            else:
                p = l2
        elif l1 is not None:
            p = l1
        else:
            p = l2
        head = p

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
            elif l1 is not None:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        return head


