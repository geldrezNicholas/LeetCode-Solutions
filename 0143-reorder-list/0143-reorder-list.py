# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverseCurr = self.reverseList(slow.next)
        slow.next = None
        curr = head

        while reverseCurr:
            tmp1, tmp2 = curr.next, reverseCurr.next
            curr.next = reverseCurr
            reverseCurr.next = tmp1
            curr, reverseCurr = tmp1, tmp2
        
    def reverseList(self, head: Optional[ListNode]):

        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev