# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        stack = stack[::-1]

        curr = head
        i = 0

        for i in stack:
            if curr.val != i:
                return False
            curr = curr.next
        return True