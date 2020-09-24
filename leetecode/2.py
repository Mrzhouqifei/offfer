# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1, x2 = 0, 0
        i, j = 1, 1
        while l1:
            x1 += l1.val * i
            l1 = l1.next
            i*=10
        while l2:
            x2 += l2.val * j
            l2 = l2.next
            j *= 10
        x = x1 + x2
        head = l3 = ListNode(0)
        while x > 0:
            l3.next = ListNode(x%10)
            x = x//10
            l3 = l3.next
        return head.next

