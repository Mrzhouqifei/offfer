# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0

        ans = ListNode(0)
        p = ans
        while l1 and l2:
            val = l1.val + l2.val + jinwei
            left = val % 10
            jinwei = int(val / 10)
            tmp = ListNode(left)
            p.next = tmp
            p = p.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + jinwei
            left = val % 10
            jinwei = int(val / 10)
            tmp = ListNode(left)
            p.next = tmp
            p = p.next
            l1 = l1.next

        while l2:
            val = l2.val + jinwei
            left = val % 10
            jinwei = int(val / 10)
            tmp = ListNode(left)
            p.next = tmp
            p = p.next
            l2 = l2.next
        return ans.next


