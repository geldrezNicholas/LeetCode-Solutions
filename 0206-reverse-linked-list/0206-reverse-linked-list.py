# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = None
        q = None

        while head != None:
            p = q
            q = head
            head = head.next
            q.next = p
        return q