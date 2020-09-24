# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     def __lt__(self, other):
#         return self.val < other.val

# from queue import PriorityQueue
#
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put_nowait(l)
#         head = point = q.get_nowait()
#         q.put_nowait(head.next)
#         while not q.empty():
#             node = q.get_nowait()
#             point.next = node
#             next = node.next
#             point = point.next
#             if next:
#                 q.put_nowait(next)
#         return head



from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        index = 0
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put_nowait((l.val, index, l))
                index+=1
        head = point = ListNode(0)
        while not q.empty():
            val, _, node = q.get_nowait()
            point.next = ListNode(val)
            point = point.next
            if node.next:
                q.put_nowait((node.next.val, index, node.next))
                index+=1
        return head.next

