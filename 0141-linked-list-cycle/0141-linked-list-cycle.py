# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pos = 0
        dict = {}
        curr = head
        while curr != None:
            if curr not in dict:
                dict[curr] = pos
            elif curr in dict:
                if pos > dict[curr]:
                    return True
            pos+=1
            curr = curr.next
        return False
        